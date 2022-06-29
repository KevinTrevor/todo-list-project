from flask import Flask, request, jsonify
from datetime import datetime
from database import tasks, setup


app = Flask(__name__)
setup.create_tables()

@app.route('/tasks', methods = ['POST'])
def add_task():
    """
        Método para añadir una nueva tarea a la base de datos 
    """
    title = request.json['title']
    create_date = datetime.now().strftime("%x") # Fecha en formato 06/29/2022
    data = (title, create_date)

    task_id = tasks.insert_task(data)

    if task_id:
        task = tasks.select_task_by_id(task_id)
        return jsonify({'task' : task})
    return jsonify({'message' : 'Internal error'})

if __name__ == "__main__":
    app.run(debug=True)