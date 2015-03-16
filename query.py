#! /usr/bin/python

from item import itemData
from pymongo import MongoClient
import commands
import sys
import datetime
from config import *

def openFile(url):
    com = "gnome-open \"" + url + "\""
    # print com
    commands.getoutput(com)

def getFiles(condition, item):
    client = MongoClient(MONGODB_SERVER, MONGODB_PORT)
    db = client[MONGODB_DB_NAME]
    results = []
    collection = db[MONGODB_COLLECTION_NAME]
    rs = collection.find({condition:item})
    for r in rs:
        results.append(r)
    return results

def getCount():
    client = MongoClient(MONGODB_SERVER, MONGODB_PORT)
    db = client[MONGODB_DB_NAME]
    results = {}
    total = 0
    collection = db[MONGODB_COLLECTION_NAME]
    n = collection.find().count()
    total += n
    results[collection_name] = n
    results['total'] = total
    return results

def handleResults(options, results):
    for result in results:
        if 'l' in options:
            for key in result:
                print key + ":",
                print result[key]
        if 't' in options:
            openFile(result['urlTopic'])

        if 'p' in options:
            openFile(result['urlPeople'])

def error():
    print "Exp: ./query [options] [filename]"
    print '''options:
    -f\tsearch by file name
    -a\tsearch by author name
    -t\topen topic in browser
    -l\tlist information about file(default)
    -p\topen people in browse
    -c\tcount images in each group'''

def argvHandle():
    options = ['l']
    items = []
    files = []
    authors = []
    for i in sys.argv[1:]:
        if i.startswith('-'):
            options.append(i[1:])
        else:
            items.append(i)

    if 'f' in options:
        condition = 'local_filename'
        for item in items:
            results = getFiles(condition, item)
            handleResults(options, results)

    elif 'a' in options:
        condition = 'author'
        for item in items:
            results = getFiles(condition, item)
            handleResults(options, results)

    elif 'c' in options:
        results = getCount()
        for key in results:
            print key + ": " + str(results[key])

    else:
        error()

if __name__ == '__main__':
    argvHandle()

