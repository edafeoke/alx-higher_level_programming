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
    state = sys.argv[4]

    db = MySQLdb.connect(HOST, USER, PASSWD, DB)
    cur = db.cursor()

    cur.execute("""
    SELECT cities.name
    FROM cities
    JOIN states
    ON state_id=states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id
    """, (state,))
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))
