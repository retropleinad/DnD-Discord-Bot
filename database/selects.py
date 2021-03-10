import sqlite3

from . import util

path = util.PATH


def select_all(table):
    query = """
            SELECT * FROM {0}
    """
    query = query.format(table)

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(query)

    data = cursor.fetchall()
    titles = [description[0] for description in cursor.description]
    connection.close()

    return {
        "titles": titles,
        "data": data
    }


def select(table, conditions):
    query = """
            SELECT * FROM {0}
            WHERE
    """
    query = query.format(table)
    query = util.add_conditions(query, conditions)

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(query)

    data = cursor.fetchall()
    return data