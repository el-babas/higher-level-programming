#!/usr/bin/python3
""" Functions:
        a) mysqlconnect
"""
import sys
import MySQLdb


def mysqlconnect(username, password, database, port=3306):
    """
    Function:
        Connect to MySQL.

    Args:
        username (str): username to connect to MySQL.
        password (str): password to connect to MySQL.
        database (str): database to connect to MySQL.
        port (int): port to connect to MySQL.

    Return:
        Connect to MySQL.
    """
    db_connection = MySQLdb.connect(
                        user=username,
                        passwd=password,
                        db=database,
                        port=port)

    return db_connection


if __name__ == '__main__':
    db_connection = mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3])
    db_cursor = db_connection.cursor()
    db_cursor.execute('''
    SELECT * FROM states
    WHERE name = %(filter1)s ORDER BY id;
    ''', {'filter1': sys.argv[4]})

    states = db_cursor.fetchall()
    for state in states:
        print(state)

    db_cursor.close()
    db_connection.close()
