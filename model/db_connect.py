import sqlite3

def database_connection():
    conn = sqlite3.connect('../web_insights.db', check_same_thread=False)
    c = conn.cursor()
    return conn, c