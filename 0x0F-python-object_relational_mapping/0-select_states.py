#!/usr/bin/python3
'''
get all states module
'''

import MySQLdb
import sys

HOST = 'localhost'
USER = sys.argv[1]
PASSWD = sys.argv[2]
DB = sys.argv[3]

db = MySQLdb.connect(HOST, USER, PASSWD, DB)
cur = db.cursor()

cur.execute("SELECT * FROM states")
states = cur.fetchall()
for state in states:
    print(state)
