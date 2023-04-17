#!/usr/bin/python3
"""
This module prints all cities
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
        "SELECT cities.name  \
FROM cities JOIN states ON cities.state_id \
        = states.id WHERE states.name LIKE BINARY %(name)s \
 ORDER BY cities.id ASC", {'name': sys.argv[4]})
    cities_row = cur.fetchall()
    if cities_row is not None:
        print(", ".join([row[0] for row in cities_row]))
