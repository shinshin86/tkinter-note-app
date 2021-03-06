import sqlite3
import os
import sys
from os import path
from datetime import datetime


DB_NAME = "note.db"


def connect_db():
    return sqlite3.connect(find_db_file(DB_NAME))


def find_db_file(filename):
    if getattr(sys, "frozen", False):
        datadir = path.dirname(sys.executable)
    else:
        datadir = os.path.dirname(__file__)

    return path.join(datadir, filename)


def init_db_table():
    # set converter
    detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    sqlite3.dbapi2.converters['DATETIME'] = sqlite3.dbapi2.converters['TIMESTAMP']

    conn = connect_db()
    cur = conn.cursor()
    sql_statement = "CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, text TEXT, created_at datetime, updated_at datetime)"
    cur.execute(sql_statement)
    conn.commit()
    conn.close()


def get_all_note():
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM note ORDER BY id DESC")
    result = [dict(row) for row in cur.fetchall()]
    conn.close()
    return result


def get_note(id):
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sql_statement = "SELECT * FROM note WHERE id=?"
    cur.execute(sql_statement, (str(id)))
    result = cur.fetchone()
    conn.close()
    return dict(result)


def create_note(title, text):
    conn = connect_db()
    cur = conn.cursor()
    sql_statement = "INSERT INTO note VALUES(NULL, ?, ?, ?, ?)"
    cur.execute(sql_statement, (title, text, datetime.now(), datetime.now()))
    conn.commit()
    conn.close()


def update_note(id, title, text):
    conn = connect_db()
    cur = conn.cursor()
    sql_statement = "UPDATE note SET title=?, text=?, updated_at=? WHERE id=?"
    cur.execute(sql_statement, (title, text, datetime.now(), str(id)))
    conn.commit()
    conn.close()


def remove_note(id):
    conn = connect_db()
    cur = conn.cursor()
    sql_statement = "DELETE FROM note WHERE id = ?"
    cur.execute(sql_statement, (str(id)))
    conn.commit()
    conn.close()
