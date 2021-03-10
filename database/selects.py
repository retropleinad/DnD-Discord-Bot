import sqlite3

temp_path = "../bot/campaign.db"


def select_all(table):
    query = """
            SELECT * FROM {0}
    """
    query = query.format(table)

    connection = sqlite3.connect(temp_path)
    cursor = connection.cursor()
    cursor.execute(query)

    data = cursor.fetchall()
    titles = [description[0] for description in cursor.description]
    connection.close()

    return {
        "titles": titles,
        "data": data
    }


def select(table, condition):
    query = """
            SELECT * FROM {0}
            WHERE 
    """