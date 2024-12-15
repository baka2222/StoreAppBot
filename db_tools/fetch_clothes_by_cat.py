import sqlite3

def fetch_all_clothes(cat):
    conn = sqlite3.connect('StoreApp/db.sqlite3')  
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT id, img, category_id
        FROM clothes_clothes
        WHERE category_id == {cat}
    ''')

    rows = cursor.fetchall()
    conn.close()
    return rows 