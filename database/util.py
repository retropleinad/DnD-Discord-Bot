import sqlite3

PATH = "../bot/campaign.db"


def commit_query(query, args=None):
    connection = sqlite3.connect(PATH)
    if args is None:
        connection.execute(query)
    else:
        connection.execute(query, args)
    connection.commit()
    connection.close()


def add_conditions(query, **kwargs):
    output = query
    index = 0
    for key, value in kwargs.items():
        output += key + "=" + "\"" + str(value) + "\""
        index += 1
        if index != len(kwargs.items()):
            output += " AND "
    return output

