import sqlite3
from bouquetapp.views.connection import Connection
from bouquetapp.models import model_factory, BouquetFlower

def get_relations(bouquet_id):
    """

    """
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(BouquetFlower)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            *
        FROM bouquetapp_bouquetflower bf
        WHERE bf.bouquet_id = ?
        """, (bouquet_id, ))

        return db_cursor.fetchall()