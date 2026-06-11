import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    nickname TEXT NOT NULL,
    classroom TEXT NOT NULL,
    level TEXT NOT NULL,
    gender TEXT,
    sport TEXT NOT NULL,
    register_time TEXT
)
""")

conn.commit()
conn.close()

print("สร้างฐานข้อมูลสำเร็จ")