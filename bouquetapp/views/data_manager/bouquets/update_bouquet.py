import sqlite3
from bouquetapp.views.connection import Connection

def update_bouquet(form_data, bouquet_id):
    """

    """
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE bouquetapp_bouquet
        SET occasion = ?
        WHERE id = ?
        """, (form_data["occasion"], bouquet_id))
