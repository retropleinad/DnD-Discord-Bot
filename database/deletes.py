from . import util

path = util.PATH

"""
This file contains methods to delete entries from a particular table
"""


# Delete every entry in the table
def delete_all(table):
    query = """
            DELETE FROM {0}
    """
    query = query.format(table)
    util.commit_query(query)


# Delete particular entries from the table
def delete(table, conditions):
    query = """
            DELETE FROM {0} WHERE
    """
    query = query.format(table)
    query = util.add_conditions(query, conditions)
    util.commit_query(query)