from . import util

path = util.PATH

"""
This file contains methods to insert data into different tables
"""


# Insert into the region table
def insert_region(name, description):
    args = (name, description)
    query = """
            INSERT INTO region(name, description)
            VALUES (?, ?)
    """
    util.commit_query(query, args)


# Insert into the location table
def insert_location(name, description, region):
    region_name = "SELECT region_id from region WHERE name = {0}".format(region)
    args = (name, description, region)
    query = """
            INSERT INTO location(name, description, region)
            VALUES (?, ?, ?)        
    """
    util.commit_query(query, args)


# Insert into the organization table
def insert_organization(name, description, region, headquarters):
    args = (name, description, region, headquarters)
    query = """
            INSERT INTO organization(name, description, region, headquarters)
            VALUES (?, ?, ?, ?)
    """
    util.commit_query(query, args)


# Insert into the class table
def insert_class(name, description, source, page):
    args = (name, description, source, page)
    query = """
            INSERT INTO class(name, description, source, page)
            VALUES (?, ?, ?, ?)
    """
    util.commit_query(query, args)


# Insert into the player characters table
def insert_pcs(player, name, description, alive, dnd_class, origin, area):
    args = (player, name, description, alive, dnd_class, origin, area)
    query = """
            INSERT INTO pcs(player, name, description, alive, class, origin, area)
            VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    util.commit_query(query, args)


# Insert into the npcs table
def insert_npcs(name, description, region, headquarters):
    args = (name, description, region, headquarters)
    query = """
            INSERT INTO npcs(name, description, region, headquarters)
            VALUES (?, ?, ?, ?)
    """
    util.commit_query(query, args)


# Insert into the items table
def insert_item(name, description):
    args = (name, description)
    query = """
            INSERT INTO items(name, description)
            VALUES (?, ?)
    """
    util.commit_query(query, args)


# Insert into the owner table
def insert_owner(item, pc, npc, organization):
    args = (item, pc, npc, organization)
    query = """
            INSERT INTO item_owner(item, pc, npc, description)
            VALUES (?, ?, ?
    """
    util.commit_query(query, args)