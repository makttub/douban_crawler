#!/usr/bin/python
#coding: utf-8

import requests
from lxml import etree
import time, os, sys
from datetime import datetime
import pytz

from item import itemData
from qn import up
from config import *
from tool import *

tz = pytz.timezone('Asia/Shanghai')

class Html(object):
    def __init__(self, url, header={}, retry=3):
        self.url = url
        self.header = header
        self.response = self.req_get(retry)
        self.retry = retry

    def req_get(self, retry):
        for i in range(retry):
            try:
                return requests.get(self.url, headers=self.header)
            except:
                sleep_random(2, 5)

    def xpath(self, path):
        tree = etree.HTML(self.response.text)
        items = tree.xpath(path)
        return items

    def yell(self):
        if self.response.status_code == 200:
            echo("Successful visit - " + self.url, ECHO_TAG['NORMAL'])
        else:
            echo("Unsuccessful visit - " + self.url, ECHO_TAG['ERROR'])

# get group name and page range
def handle_argv():
    if '-h' in sys.argv or '-H' in sys.argv:
        print "python ./crawler.py\n\tGet crawl list from script(config.py)."
        print "python ./crawler.py <id> <total_page>\n\tGet crawl list from shell. id is id of xiaozu, total_page is number of pages you want to crawl."
        return

    if len(sys.argv) == 1:
        return DEFAULT_LIST
    else:
        name = sys.argv[1]
        total_page = int(sys.argv[2])
        return {name: total_page}

def handle_url_people(u):
    r = u.replace('/group', '')
    return r

def handle_imagefile(itemdata):
    if not itemdata.inDB():
        if download_image_file(itemdata):
            itemdata.insertDB()
            up(itemdata)
        else:
            echo("Download error - " + itemdata.local_filename, ECHO_TAG['ERROR'])
    else:
        echo("Image exists - " + itemdata.local_filename, ECHO_TAG['NORMAL'])

def download_image_file(itemdata):
    echo("Download Image File - " + itemdata.local_filename + " From " + itemdata.urlTopic, ECHO_TAG['DOWN'])
    itemdata.checkDir()
    itemdata.timeDown = datetime.now(tz)
    op = 3
    while op > 0:
        try:
            r = requests.get(itemdata.urlPic, stream=True)
            with open(itemdata.pathDir() + os.sep + itemdata.local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                f.close()
            return True
        except:
            echo("Download try again - " + itemdata.local_filename, ECHO_TAG['ERROR'])
            op -= 1
            time.sleep(2)

def crawl(name, total_page):
    for i in range(total_page):
        url_discussion = "http://www.douban.com/group/" + name + "/discussion?start=" + str(i*25)

        # visit discussion page
        h_discussion = Html(url_discussion, HEADER_TAG["discussion"])
        h_discussion.yell()

        path = "//*[@id=\"content\"]/div/div[1]/div[2]/table/tr"
        nodes = h_discussion.xpath(path)
        for node in nodes:
            url_topics = node.xpath('td/a/@href')
            authors = node.xpath('td/a/text()')

            # check and get url_topic
            if len(url_topics) == 2 and len(authors) == 2:
                url_topic = url_topics[0]
                url_people = handle_url_people(url_topics[1])
                title = authors[0].encode('utf-8')
                author = authors[1].encode('utf-8')

                # visit topic page
                h_topic = Html(url_topic, HEADER_TAG["topic"])
                h_topic.yell()
                time.sleep(1.5)

                path = "//*[@id=\"link-report\"]/div/div/img/@src"
                tnodes = h_topic.xpath(path)

                # check and get url_image
                try:
                    time_up = h_topic.xpath("//*[@id=\"content\"]/div/div[1]/div[1]/div[2]/h3/span[2]")[0].text
                except:
                    continue
                for url_image in tnodes:
                    local_filename = url_image.split('/')[-1]

                    # combine
                    itemdata = itemData(url_discussion, url_topic, url_people, title, author, url_image, time_up, local_filename, name)
                    handle_imagefile(itemdata)

def main():
    names = handle_argv()
    if not names:
        return

    while True:
        for name in names:
            crawl(name, names[name])
        sleep_random(3600, 3600+1800)

if __name__ == '__main__':
    main()
