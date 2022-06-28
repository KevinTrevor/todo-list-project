import sqlite3
from sqlite3 import Error

def create_connection():

    """
        Función que permite conectarnos con una base de datos 
        determinada

        return None
    """

    conn = None

    try:
        conn = sqlite3.connect(database="database/task.db")
    except Error as e:
        print(f"Error at connection to database: {e}")
    
    return conn