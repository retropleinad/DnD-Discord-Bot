import sqlite3

PATH = "../database/campaign.db"

"""
Contains helper methods for the database
"""


# Takes a query and runs it
def commit_query(query, args=None):
    connection = sqlite3.connect(PATH)
    if args is None:
        connection.execute(query)
    else:
        connection.execute(query, args)
    connection.commit()
    connection.close()


def fetch(query):
    connection = sqlite3.connect(PATH)
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data


# Takes a dict of conditions (such as "name":"Alex") and formats it into an SQL query
def add_conditions(query, conditions):
    output = query
    index = 0
    for key, value in conditions.items():
        output += key + "=" + "\"" + str(value) + "\""
        index += 1
        if index != len(conditions.items()):
            output += " AND "
    return output


# Adds a join to a query
def add_join(conditions, table):
    join = "INNER JOIN " + table
    for key, value in conditions.items():
        join += key
