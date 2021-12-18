#!/usr/bin/python3
'''
get all cities module
'''

import MySQLdb
import sys


if __name__ == "__main__":
    HOST = 'localhost'
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]

    db = MySQLdb.connect(HOST, USER, PASSWD, DB)
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
            JOIN states ON state_id=states.id ORDER BY cities.id""")
    cities = cur.fetchall()
    for city in cities:
        print(city)
