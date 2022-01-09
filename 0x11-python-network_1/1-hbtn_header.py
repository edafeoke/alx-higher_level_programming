#!/usr/bin/python3
'''0-hbtn_status module'''

from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
