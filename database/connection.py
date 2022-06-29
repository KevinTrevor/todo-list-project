import sqlite3
from sqlite3 import Error

def create_connection():

    """
        Función que permite conectarnos con una base de datos 
        determinada
    """

    conn = None

    try:
        conn = sqlite3.connect(database="database/tasks.db")
    except Error as e:
        print(f"Error at connection to database: {e}")
    
    return conn