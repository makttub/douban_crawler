from datetime import datetime
import pytz
from random import randint
from datetime import timedelta
from config import *
import time

tz = pytz.timezone('Asia/Shanghai')

def echo(content, tag=1):
    if tag == 0:
        print echo_style(content, "red")
    elif tag == 1:
        print echo_style(content, "white")
    elif tag == 2:
        print echo_style(content, "blue")

def echo_style(s, t):
    color_tag = {"gray": "30", "red": "31", "green": "32", "yellow": "33", "blue": "34", "magenta": "35", "cyan": "36", "white": "37", "crimson": "38"}
    return '\033[1;' + color_tag[t] + 'm' + '[' + str(datetime.now(tz))[:19] + '] ' + '\033[1;m' + s

def sleep_random(start, end):
    t = randint(start, end)
    delta = timedelta(seconds=t)
    echo("Time of next waking up - " + str(datetime.now(tz)+delta), ECHO_TAG["NORMAL"])
    time.sleep(t)
