import sqlite3 
#sqlite uses ISO8601 format for text, remember that

DB_NAME = "logs.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_time TEXT,
        mode INTEGER,
        duration INTEGER 
    """)
    conn.commit()
    return conn, cursor


# this should log values
def log_value(mode: int, duration: int, start_time):
    """Insert a work/rest interval into the logs table.

    mode        -> 0 = work, 1 = rest
    duration    -> in seconds
    start_time  -> [start_time of work/rest session]
    """
    conn, cursor = get_connection()
    
    cursor.execute(
        "INSERT INTO logs (start_time, mode, duration) VALUES (?, ?, ?)",
        (start_time.isoformat(sep=" "), mode, duration)
    )
    conn.commit()
    conn.close()


def get_logs(mode=None):
    # Retrieve logs (all or filtered by mode)
    conn, cursor = get_connection()
    if mode:
        cursor.execute("SELECT * FROM logs WHERE mode=?", (mode,))
    else:
        cursor.execute("SELECT * FROM logs")
    rows = cursor.fetchall()
    conn.close()
    return rows