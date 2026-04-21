import sqlite3

DB_NAME = "passwords.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT,
            password TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_password(service, username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
        (service, username, password)
    )
    conn.commit()
    conn.close()

def list_passwords():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, service, username, created_at FROM passwords")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_password_by_id(password_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, service, username, password, created_at FROM passwords WHERE id = ?",
        (password_id,)
    )
    row = cur.fetchone()
    conn.close()
    return row

def delete_password(password_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM passwords WHERE id = ?", (password_id,))
    conn.commit()
    conn.close()
