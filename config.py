DEFAULT_LIST = {
                'leon-image': 3, # group url is http://www.douban.com/group/leon-image/
                'photoer': 3,
                'Microstockphoto': 3,
                'pentax-K5': 3
                }

# config for qiniu
QINIU = True
QINIU_ACCESS_KEY = ''
QINIU_SECRET_KEY = ''
QINIU_BUCKET_NAME = ''

# config for mongodb
MONGODB_SERVER = '' # localhost
MONGODB_PORT =  # 12345
MONGODB_DB_NAME = '' # db name
MONGODB_COLLECTION_NAME = '' # collection name

ECHO_TAG = {"ERROR": 0, "NORMAL": 1, "DOWN": 2}

# config for get request
HEADER_TAG = {
            # headers of visiting discussion page
            # example
            "discussion": {
                "Host": "www.douban.com",
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36",
                "DNT": "1",
                "Accept-Encoding": "gzip,deflate,sdch",
                "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
                "Cookie": "Your cookie of visiting discussion page, remember escape \" ", # Cookie
                "RA-Ver": "2.8.7",
                "RA-Sid": "79FAD30D-2114061d-12352c-42ce8b-792c6"
                },
            # headers of visiting topic page
            # example
            "topic": {
                "Host": "www.douban.com",
                "Connection": "keep-alive",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36",
                "DNT": "1",
                "Accept-Encoding": "gzip,deflate,sdch",
                "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
                "Cookie": "Your cookie of visiting discussion page, remember escape \" ", # Cookie,
                "RA-Ver": "2.8.7",
                "RA-Sid": "79FAD30D-20140619-123526-42ce88-792c6b"
                }
            }
