#!/usr/bin/python3
"""
This module prints all states that matches tge 4th argument
"""
import MySQLdb
import sys
if __name__ == "__main__":
    """
    Connect to the database and gets states
    """
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
        host="localhost", port=3306)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' \
ORDER BY states.id ASC".format(sys.argv[4]))
    states_row = cur.fetchall()
    for states in states_row:
        print(states)
