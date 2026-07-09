import sqlite3
from inventory import inventory

DB_NAME = "inventory.db"


def create_database():
    """Creates the inventory database and table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()



def migrate_data():
    """Migrates inventory data into SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM inventory")

    for item in inventory:
        cursor.execute(
            """
            INSERT INTO inventory (item_name, quantity, price)
            VALUES (?, ?, ?)
            """,
            (item["item_name"], item["quantity"], item["price"])
        )

    conn.commit()
    conn.close()

def get_inventory():
    """Returns all inventory records from SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT item_name, quantity, price FROM inventory"
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "item_name": row[0],
            "quantity": row[1],
            "price": row[2]
        }
        for row in rows
    ]