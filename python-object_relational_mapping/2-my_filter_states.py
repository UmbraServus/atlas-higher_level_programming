#!/usr/bin/python3
"""
Module to lists states in a database by id where name is given as an argument
"""
import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        f"""
    SELECT id, name
    FROM states
    WHERE name = '{sys.argv[4]}'
    ORDER BY id ASC"""
    )
    list = cur.fetchall()

    for state in list:
        print(state)
