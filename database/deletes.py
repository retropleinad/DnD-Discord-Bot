from . import util

path = util.PATH


def delete_all(table):
    query = """
            DELETE FROM {0}
    """
    query = query.format(table)
    util.commit_query(query)


def delete(table, **kwargs):
    query = """
            DELETE FROM {0} WHERE
    """
    query = query.format(table)
    query = util.add_conditions(query, **kwargs)
    util.commit_query(query)