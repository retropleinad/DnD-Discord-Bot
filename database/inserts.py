from . import util

path = util.PATH

"""
This file contains methods to insert data into different tables
"""


# Add a new player to the campaign
def insert_player(name):
    args = (name,)
    query = """
            INSERT INTO players(name)
            VALUES (?)
    """
    util.commit_query(query, args)


# Insert into the region table
def insert_region(name, description="NULL"):
    args = (name, description)
    query = """
            INSERT INTO region(name, description)
            VALUES (?, ?)
    """
    util.commit_query(query, args)


# Insert into the location table
def insert_location(name, description="NULL", region="NULL"):
    region_name = "SELECT region_id from region WHERE name = {0}".format(region)
    args = (name, description, region)
    query = """
            INSERT INTO location(name, description, region)
            VALUES (?, ?, ?)        
    """
    util.commit_query(query, args)


# Insert into the organization table
def insert_organization(name, description="NULL", region="NULL"):
    args = (name, description, region)
    query = """
            INSERT INTO organization(name, description, region)
            VALUES (?, ?, ?, ?)
    """
    util.commit_query(query, args)


# Insert a new content source
def insert_source(title):
    args = (title,)
    query = """
            INSERT INTO source(title)
            VALUES (?)
    """
    util.commit_query(query, args)


# Insert into the class table
def insert_class(name, description="NULL", source="NULL"):
    args = (name, description, source)
    query = """
            INSERT INTO class(name, description, source)
            VALUES (?, ?, ?, ?)
    """
    util.commit_query(query, args)


# Insert into the player characters table
def insert_pcs(player, name, description="NULL", alive="TRUE", dnd_class="Null", origin="Null", area="Null"):
    args = (player, name, description, alive, dnd_class, origin, area)
    query = """
            INSERT INTO pcs(player, name, description, alive, class, origin, area)
            VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    util.commit_query(query, args)


# Insert into the npcs table
def insert_npcs(name, description="NULL", region="NULL", organization="NULL"):
    args = (name, description, region, organization)
    query = """
            INSERT INTO npcs(name, description, region, organization)
            VALUES (?, ?, ?, ?)
    """
    util.commit_query(query, args)


# Insert into the items table
def insert_item(name, description="NULL"):
    args = (name, description)
    query = """
            INSERT INTO items(name, description)
            VALUES (?, ?)
    """
    util.commit_query(query, args)