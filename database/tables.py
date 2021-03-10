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

temp_path = "../bot/campaign.db"

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
            player TEXT NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            alive BOOL DEFAULT TRUE,
            class INTEGER,
            origin INTEGER,
            area INTEGER,
            FOREIGN KEY(class) REFERENCES class(class_id),
            FOREIGN KEY(origin) REFERENCES region(region_id),
            FOREIGN KEY(area) REFERENCES region(region_id)
        )
    """,
    """
        CREATE TABLE npcs (
            npc_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            region INTEGER,
            headquarters INTEGER,
            FOREIGN KEY(region) REFERENCES region(region_id),
            FOREIGN KEY(headquarters) REFERENCES location(location_id)
        )
    """,
    """
        CREATE TABLE items (
            item_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
    """,
    """
        CREATE TABLE item_owner (
            owner_id INTEGER PRIMARY KEY,
            item INTEGER NOT NULL,
            pc INTEGER,
            npc INTEGER,
            organization INTEGER,
            FOREIGN KEY(item) references items(item_id),
            FOREIGN KEY(pc) references pcs(pc_id),
            FOREIGN KEY(npc) references npcs(npc_id),
            FOREIGN KEY(organization) references organization(organization_id)
        )
    """
)

connection = sqlite3.connect(temp_path)

for table in tables:
    connection.execute(table)

connection.close()