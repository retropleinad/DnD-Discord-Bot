import sqlite3

temp_path = "../bot/campaign.db"


def delete_all(table):
    query = """
            DELETE FROM {0}
    """
    query = query.format(table)
    connection = sqlite3.connect(temp_path)
    connection.execute(query)
    connection.close()