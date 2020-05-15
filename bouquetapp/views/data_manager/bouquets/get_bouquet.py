import sqlite3
from bouquetapp.views.connection import Connection
from bouquetapp.models import model_factory, Bouquet

def get_bouquet(bouquet_id):
    """
    Grabs the bouquet in the database that matches the passes bouquet id

    Uses the Bouquet model to represent data
    
    => Single Bouquet classes
    """
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Bouquet)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            *
        FROM bouquetapp_bouquet b
        Where b.id = ?
        """, (bouquet_id,))

        return db_cursor.fetchone()