import sqlite3
from bouquetapp.views.connection import Connection
from bouquetapp.models import model_factory, Bouquet

def get_all_bouquets():
    """
    Grabs all of the bouquets in the database

    Uses the Bouquet model to represent data

    Sql query grabs all bouquets in order alphabetically
    
    => list of Bouquet classes
    """
    with sqlite3.connect(Connection.db_path) as conn:
        # Uses the Bouquet model to represent data
        conn.row_factory = model_factory(Bouquet)

        db_cursor = conn.cursor()

        # Grabs all data in alphabetical order by name
        db_cursor.execute("""
        SELECT
            *
        FROM bouquetapp_bouquet
        ORDER BY name ASC
        """)

    # list of Bouquet classes
    return db_cursor.fetchall()