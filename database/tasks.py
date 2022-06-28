import sqlite3
from sqlite3 import Error
from venv import create
from .connection import create_connection

def insert_task(data):
    """
        Función que crea una nueva tarea en la tabla tasks
        de la base de datos
    """

    conn = create_connection()

    sql = "INSERT INTO task (title, create_date) VALUES (?, ?)"

    try:

        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

        return cur.lastrowid
    except Error as e:
        print(f"Error at insert_task(): {e}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def select_task_by_id(id):

    """
        Función que selecciona una fila que coincida con el id
    en la base de datos y la retorna.
    """

    conn = create_connection()

    sql = f"SELECT * FROM tasks WHERE id = '{id}'"

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        task = dict(cur.fetchone())

        return task
    except Error as e:
        print(f"Error at select_task_by_id(): {e}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
    