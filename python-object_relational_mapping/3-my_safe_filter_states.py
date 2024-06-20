#!/usr/bin/python3
"""
Module to lists states in a database by id where name is given as an argument
but does it in a way that doesnt allow for SQL injections by parameterizing the query.
"""
import sys
import MySQLdb


if __name__ == "__main__":

    state_name = sys.argv[4]
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(query, (state_name,))

    list = cur.fetchall()

    for state in list:
        print(state)
