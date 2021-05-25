import sqlite3

from . import util

path = util.PATH

"""
This file contains functions to select rows from a table
"""


# Select everything from the table
# Returns column headers and rows
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


# Select a particular row from the table
def select(table, conditions):
    query = """
            SELECT * FROM {0}
            WHERE
    """
    query = query.format(table)
    query = util.add_conditions(query, conditions)
    return util.fetch(query)


# Select all characters (player and npc) in Drydock
def drydock_chars():
    query = """
        SELECT pc_id, name, player.name AS player_name
        FROM pcs
        INNER JOIN region
            ON pcs.region_id = region.region_id
        INNER JOIN players
            ON pcs.player_id = player.player_id
        WHERE region.region_id = (
            SELECT region.region_id
            FROM region
            WHERE region.name = Drydock
        )
        UNION
        SELECT npc_id, name
        FROM npcs
        INNER JOIN region
            ON npcs.region_id = region.region_id
        WHERE region.region_id = (
            SELECT region.region_id
            FROM region
            WHERE region.name = Drydock
        )
    """
    return util.fetch(query)


def list_dead():
    query = """
        SELECT pc_id, name, player.name
        FROM pcs
        INNER JOIN player
            ON pcs.player_id = player.player_id
        WHERE NOT alive
        UNION
        SELECT npc_id, name
        FROM npcs
        WHERE NOT alive;
    """
    return util.fetch(query)


def list_living():
    query = """
        SELECT pc_id, name, player.name
        FROM pcs
        WHERE alive
        INNER JOIN player
            ON pcs.player_id = player.player_id
        UNION
        SELECT npc_id, name
        FROM npcs
        WHERE alive;
    """
    return util.fetch(query)


# List all items owned by a particular character
def items_owned(owner_id=None, owner_name=None):
    if owner_id is None and owner_name is None:
        raise TypeError("Both owner_id and owner_name cannot be None")
    elif owner_name is None:
        query = """
            SELECT item_id, name 
            FROM items
            WHERE owner_id = {0}
        """.format(owner_id)
    else:
        query = """
            SELECT item_id, name
            FROM items
            WHERE owner_id = (
                SELECT pc_id FROM pcs
                WHERE pcs.name = {0}
            ) 
        """.format(owner_name)
    return util.fetch(query)


# List all characters belonging to a particular class
def class_chars(class_id=None, class_name=None):
    if class_id is None and class_name is None:
        raise TypeError("Both class_id and class_name cannot be None")
    elif class_name is None:
        query = """
            SELECT pc_id, name, player.name
            FROM pcs
            INNER JOIN player
                ON pcs.player_id = player.player_id
            WHERE class_id = {0}
        """.format(class_id)
    else:
        query = """
            SELECT pc_id, name, player.name 
            FROM pcs
            INNER JOIN player
                ON pcs.player_id = player.player_id
            WHERE class_id = (
                SELECT class_id FROM class
                WHERE class.name = {0}
            )
        """.format(class_name)
    return util.fetch(query)


def org_chars(org_id=None, org_name=None):
    if org_id is None and org_name is None:
        raise TypeError("Both org_id and org_name cannot be None")
    elif org_name is None:
        query = """
            SELECT pc_id, name, player.name
            FROM pcs
            INNER JOIN player
                ON pcs.player_id = player.player_id
            WHERE organization_id = {0}
            UNION
            SELECT npc_id, name
            FROM npcs
            WHERE organization_id = {0}
        """.format(org_id)
    else:
        query = """
            SELECT pc_id, name, player.name
            FROM pcs
            INNER JOIN player
                ON pcs.player_id = player.player_id
            WHERE organization_id = (
                SELECT organization_id FROM organization
                WHERE organization.name = {0}
            )
            UNION
            SELECT npc_id, name
            FROM npcs
            WHERE organization_id = (
                SELECT organization_id FROM organization
                WHERE organization.name = {0}
            )
        """.format(org_id)
    return util.fetch(query)


def total_owned(char_id=None, char_name=None):
    if char_id is None and char_name is None:
        raise TypeError("Both char_id and char_name cannot be None")
    elif char_name is None:
        query = """
            SELECT pcs.name AS name, COUNT(items.item_id)
            FROM items
            INNER JOIN pcs
                ON pcs.pc_id = items.pc_id
            WHERE pcs.pc_id = {0}
            GROUP BY items.pc_id
            ORDER BY COUNT(items.item_id) DESC
        """
    else:
        query = """
            SELECT pcs.name AS name, COUNT(items.item_id)
            FROM items
            INNER JOIN pcs
                ON pcs.pc_id = items.pc_id
            WHERE pcs.name = {0}
            GROUP BY items.pc_id
            ORDER BY COUNT(items.item_id) DESC
        """