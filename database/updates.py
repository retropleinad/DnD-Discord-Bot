from database import util


def update(table, changes, conditions):
    query = "UPDATE {0} SET".format(table)
    query = add_set(query, changes)
    query += " WHERE "
    query = util.add_conditions(query, conditions)
    util.commit_query(query)


def add_set(query, changes):
    output = query
    index = 0
    for key, value in changes.items():
        output += " {0} = \"{1}\" ".format(key, value)
        index += 1
        if len(changes.items()) != index:
            output += ","
    return output