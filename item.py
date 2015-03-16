import os
from pymongo import MongoClient
from config import *

class itemData(object):

    def __init__(self, urlDiscussion, urlTopic, urlPeople, title, author, urlPic, timeUp, local_filename, group):
        self.urlDiscussion = urlDiscussion
        self.urlTopic = urlTopic
        self.title = title
        self.author = author
        self.urlPeople = urlPeople
        self.urlPic = urlPic
        self.timeUp = timeUp
        self.timeDown = 'undefined'
        self.local_filename = local_filename
        self.group = group

    def pathDir(self):
        nameZu = self.urlDiscussion.split('/')[4]
        timeUp = self.timeUp.split()[0]
        path = os.getcwd() + os.sep + nameZu + os.sep
        return path

    def pathFile(self):
        path = self.pathDir() + os.sep + self.local_filename
        return path

    def checkDir(self):
        path = self.pathDir()
        if not os.path.exists(path):
            os.makedirs(path)

    def connectDB(self):
        client = MongoClient(MONGODB_SERVER, MONGODB_PORT)
        db = client[MONGODB_DB_NAME]
        collection = db[MONGODB_COLLECTION_NAME]
        return collection

    def inDB(self):
        collection = self.connectDB()
        if collection.find({"urlPic":self.urlPic}).count() != 0:
            return True
        else:
            return False

    def insertDB(self):
        collection = self.connectDB()
        collection.insert(self.var2dict())

    def var2dict(self):
        d = {key: value for key, value in self.__dict__.items() if (not key.startswith('__') and not callable(key))}
        return d

    def __str__(self):
        return "timeUp: %s\nurlTopic: %s\ntitle: %s\nauthor: %s\nurlPeople: %s\nnumPic: %d\n\n" % (self.timeUp, self.urlTopic, self.title, self.author, self.urlPeople, self.numPic)
