import sqlite3

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE animal_type (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type VARCHAR(50) NOT NULL 
        );
    """

    query_1 = """
        CREATE TABLE colors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type VARCHAR(50) NOT NULL
        );
    """

    query_2 = """
        CREATE TABLE breed (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type VARCHAR(50) NOT NULL
        );
    """

    query_3 = """
        CREATE TABLE animal_outcome (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            outcome_type VARCHAR(50) NOT NULL,
            outcome_month INTEGER NOT NULL,
            outcome_year INTEGER NOT NULL,
            age_upon_outcome INTEGER NOT NULL
        );
    """
        
    query_4 = """
        CREATE TABLE animals_2 (
            id integer primary key autoincrement,
            animal_id VARCHAR(50),
            type_id INTEGER,
            name VARCHAR(50),
            breed_id INTEGER,
            color1_id INTEGER,
            color2_id INTEGER,
            date_of_birth INTEGER,
            outcome_id INTEGER,
            FOREIGN KEY (type_id) REFERENCES animal_type(id),
            FOREIGN KEY (breed_id) REFERENCES breed(id),
            FOREIGN KEY (color1_id) REFERENCES colors(id),
            FOREIGN KEY (color2_id) REFERENCES colors(id),
            FOREIGN KEY (outcome_id) REFERENCES animal_outcome(id)
        );
    """

    query_5 = """ 
    INSERT INTO animal_type
    SELECT DISTINCT animal_type FROM animals
    """

cursor.execute(query)
cursor.execute(query_1)
cursor.execute(query_2)
cursor.execute(query_3)
cursor.execute(query_4)
cursor.execute(query_5)
