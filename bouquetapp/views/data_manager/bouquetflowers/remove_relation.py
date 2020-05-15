import sqlite3
from bouquetapp.views.connection import Connection

def remove_relation(bouquet_flower_id):
    """

    """
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM bouquetapp_bouquetflower  
        WHERE id = ?
        """, (bouquet_flower_id, ))
