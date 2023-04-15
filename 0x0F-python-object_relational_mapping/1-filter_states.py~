#!/usr/bin/python3
"""
Thisodule prints all states in states table
"""
import MySQLdb
import sys
if __name__ == "__main__":
    """
    Cinnect to tgedatabase abd gets states
    """
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
        host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states_row = cur.fetchall()
    for states in states_row:
        print(states)
