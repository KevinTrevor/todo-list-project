import sqlite3
from sqlite3 import Error
from .connection import create_connection

def read_file(path):
    """
        Función que lee un archivo en un pathing especifico
    y retorna lo leído.
    """
    with open(path, "r") as sql_file:
        return sql_file.read()

def create_tables():
    """
        Función que crea las tablas de una base de datos a 
        través de código DDL 
    """

    conn = create_connection()

    path = "database/sql/tables.sql"

    sql = read_file(path)

    try:
        cur = conn.cursor() 
        cur.execute(sql)

        conn.commit()
        return True
    except Error as e:
        print(f"Error at create_tables(): {e}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

