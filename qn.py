from qiniu import Auth, put_file
import item
import os
from config import *

def up(i):
    if not QINIU:
        return

    access_key = QINIU_ACCESS_KEY
    secret_key = QINIU_SECRET_KEY
    bucket_name = QINIU_BUCKET_NAME

    q = Auth(access_key, secret_key)

    localfile = i.pathDir() + os.sep + i.local_filename
    key = i.local_filename
    mime_type = "image/jpeg"
    params = {'x:a': 'a'}

    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
    # print(info)
