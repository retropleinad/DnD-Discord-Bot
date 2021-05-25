import sqlite3

from . import util

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

PATH = util.PATH

tables = (
    """
        CREATE TABLE player (
            player_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """,
    """
        CREATE TABLE region (
            region_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
    """,
    """
        CREATE TABLE location (
            location_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            region_id INTEGER,
            FOREIGN KEY(region_id) REFERENCES region(region_id)
        )
    """,
    """
        CREATE TABLE organization (
            organization_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            region_id INTEGER,
            FOREIGN KEY(region_id) REFERENCES region(region_id)
        ) 
    """,
    """
        CREATE TABLE source (
            source_id INTEGER PRIMARY KEY,
            title TEXT UNIQUE NOT NULL
        )
    """,
    """
        CREATE TABLE class (
            class_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            source_id INTEGER,
            FOREIGN KEY(source_id) REFERENCES source(source_id)
        )
    """,
    """
        CREATE TABLE pcs (
            pc_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            alive BOOL DEFAULT TRUE,
            player_id INTEGER,
            class_id INTEGER,
            origin INTEGER,
            region_id INTEGER,
            organization_id INTEGER,
            FOREIGN KEY(player_id) REFERENCES player(player_id),
            FOREIGN KEY(class_id) REFERENCES class(class_id),
            FOREIGN KEY(origin) REFERENCES region(region_id),
            FOREIGN KEY(region_id) REFERENCES region(region_id),
            FOREIGN KEY(organization_id) REFERENCES organization(organization_id)
        )
    """,
    """
        CREATE TABLE npcs (
            npc_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            alive BOOL DEFAULT TRUE,
            region INTEGER,
            organization_id INTEGER,
            FOREIGN KEY(region) REFERENCES region(region_id),
            FOREIGN KEY(organization_id) REFERENCES organization(organization_id)
        )
    """,
    """
        CREATE TABLE items (
            item_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            pc_id INT,
            FOREIGN KEY(pc_id) REFERENCES pcs(pc_id)
        )
    """
)

connection = sqlite3.connect(PATH)

for table in tables:
    connection.execute(table)

connection.close()