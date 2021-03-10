from . import util

path = util.PATH


def delete_all(table):
    query = """
            DELETE FROM {0}
    """
    query = query.format(table)
    util.commit_query(query)


def delete(table, conditions):
    query = """
            DELETE FROM {0} WHERE
    """
    query = query.format(table)
    query = util.add_conditions(query, conditions)
    util.commit_query(query)