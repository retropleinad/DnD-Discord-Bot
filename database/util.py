import sqlite3

PATH = "../database/campaign.db"


def commit_query(query, args=None):
    connection = sqlite3.connect(PATH)
    if args is None:
        connection.execute(query)
    else:
        connection.execute(query, args)
    connection.commit()
    connection.close()


def add_conditions(query, conditions):
    output = query
    index = 0
    for key, value in conditions.items():
        output += key + "=" + "\"" + str(value) + "\""
        index += 1
        if index != len(conditions.items()):
            output += " AND "
    return output

