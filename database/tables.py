import sqlite3

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

temp_path = "campaign.db"

tables = (
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
            region INTEGER,
            FOREIGN KEY(region) REFERENCES region(region_id)
        )
    """,
    """
        CREATE TABLE organization (
            organization_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            region INTEGER,
            headquarters INTEGER,
            FOREIGN KEY(region) REFERENCES region(region_id),
            FOREIGN KEY(headquarters) REFERENCES location(location_id)
        ) 
    """,
    """
        CREATE TABLE class (
            class_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            source TEXT,
            page INTEGER
        )
    """,
    """
        CREATE TABLE pcs (
            pc_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            player TEXT NOT NULL,
            description TEXT,
            alive BOOL DEFAULT TRUE,
            class_id INTEGER,
            origin INTEGER,
            region_id INTEGER,
            organization_id INTEGER,
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
            pc_id INT,
            description TEXT,
            FOREIGN KEY(pc_id) REFERENCES pcs(pc_id)
        )
    """
)

connection = sqlite3.connect(temp_path)

for table in tables:
    connection.execute(table)

connection.close()