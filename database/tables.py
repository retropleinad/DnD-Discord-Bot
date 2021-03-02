import sqlite3

temp_path = "database/campaign.db"

"""
This file holds the CREATE TABLE sqlite commands to build the database. 

Tables:
1.) Region
2.) Specific locations
3.) Organizations
4.) Classes
5.) Player characters
6.) NPCs


"""


def create_location():
    region_table = """
        CREATE TABLE region (
            region_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
    """
    location_table = """
        CREATE TABLE location (
            location_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            region INTEGER,
            FOREIGN KEY(region) REFERENCES region(region_id)
        )
    """


def create_organization():
    organization_table = """
        CREATE TABLE organization (
            organization_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            region INTEGER,
            headquarters INTEGER,
            FOREIGN KEY(region) REFERENCES region(region_id),
            FOREIGN KEY(headquarters) REFERENCES location(location_id)
        ) 
    """


def create_pcs():
    class_table = """
        CREATE TABLE class (
            class_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            source TEXT,
            page INTEGER
        )
    """
    pcs_table = """
        CREATE TABLE pcs (
            pc_id INTEGER PRIMARY KEY,
            player TEXT NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            alive BOOL DEFAULT TRUE,
            picture BLOB,
            class INTEGER,
            origin INTEGER,
            area INTEGER,
            FOREIGN KEY(class) REFERENCES class(class_id),
            FOREIGN KEY(origin) REFERENCES region(region_id),
            FOREIGN KEY(area) REFERENCES region(region_id)
        )
    """


def create_npcs():
    npc_table = """
        CREATE TABLE npcs (
            npc_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            residence INTEGER,
        )
    """