import sqlite3
from bouquetapp.views.connection import Connection

def add_bouquet(form_data):
    """
    Takes in form data
    Runs INSERT sql query to add new boquet to database,
    needs form_data["name"], form_data["occasion"]
    => id of created bouquet
    """
    with sqlite3.connect(Connection.db_path) as conn:

        db_cursor = conn.cursor()
        return db_cursor.execute("""
        INSERT INTO bouquetapp_bouquet(name, occasion)
        VALUES(?, ?)
        """, (form_data["name"], form_data["occasion"])).lastrowid

        