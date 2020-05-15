import sqlite3
from bouquetapp.views.connection import Connection
from bouquetapp.models import model_factory, Bouquet

def get_all_bouquets():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Bouquet)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            *
        FROM bouquetapp_bouquet
        ORDER BY name ASC
        """)

    return db_cursor.fetchall()