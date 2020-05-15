import sqlite3
from bouquetapp.views.connection import Connection

def update_bouquet(form_data, bouquet_id):
    """
    Runs UPDATE sql query on passed in bouquet_id using the passed in form_data information as values

    needs form_data["occasion"]

    => NONE
    """
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE bouquetapp_bouquet
        SET occasion = ?
        WHERE id = ?
        """, (form_data["occasion"], bouquet_id))
