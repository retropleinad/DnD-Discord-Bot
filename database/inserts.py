from . import util

path = util.PATH


def insert_region(name, description):
    args = (name, description)
    query = """
            INSERT INTO region(name, description)
            VALUES (?, ?)
    """
    util.commit_query(query, args)


def insert_location(name, description, region="NULL"):
    args = (name, description, region)
    query = """
            INSERT INTO location(name, description, region)
            VALUES (?, ?, ?)        
    """
    util.commit_query(query, args)


def insert_organization(name, description, region, headquarters):
    args = (name, description, region, headquarters)
    query = """
            INSERT INTO organization(name, description, region, headquarters)
            VALUES (?, ?, ?, ?)
    """
    util.commit_query(query, args)


def insert_class(name, description, source, page):
    args = (name, description, source, page)
    query = """
            INSERT INTO class(name, description, source, page)
            VALUES (?, ?, ?, ?)
    """
    util.commit_query(query, args)


def insert_pcs(player, name, description, alive, dnd_class, origin, area):
    args = (player, name, description, alive, dnd_class, origin, area)
    query = """
            INSERT INTO pcs(player, name, description, alive, class, origin, area)
            VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    util.commit_query(query, args)


def insert_npcs(name, description, region, headquarters):
    args = (name, description, region, headquarters)
    query = """
            INSERT INTO npcs(name, description, region, headquarters)
            VALUES (?, ?, ?, ?)
    """
    util.commit_query(query, args)


def insert_item(name, description):
    args = (name, description)
    query = """
            INSERT INTO items(name, description)
            VALUES (?, ?)
    """
    util.commit_query(query, args)


def insert_owner(item, pc, npc, organization):
    args = (item, pc, npc, organization)
    query = """
            INSERT INTO item_owner(item, pc, npc, description)
            VALUES (?, ?, ?
    """
    util.commit_query(query, args)