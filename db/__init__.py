import sqlite3

CONN = sqlite3.connect("db/restaurant_company.db")
CURSOR = CONN.cursor()

def create_conn():
    return sqlite3.connect("db/restaurant_company.db")
    
