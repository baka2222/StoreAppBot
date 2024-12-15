import sqlite3


def fetch_category():
    conn = sqlite3.connect('StoreApp/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM clothes_category')
    rows = cursor.fetchall()
    conn.close()

    return rows