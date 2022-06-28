from flask import Flask, request, jsonify
from datetime import datetime
from database import tasks, setup


app = Flask(__name__)
setup.create_tables()

@app.route('/tasks', methods = ["POST"])
def add_task():
    """
        Método para añadir una nueva tarea a la base de datos

        return json
    """
    title = request.json['title']
    create_date = datetime.now().strftime("Xx") # Fecha en formato 28/06/2022
    data = (title, create_date)

    task_id = tasks.insert_task(data)

    if task_id:
        return jsonify({'message' : 'Task Created'})
    return jsonify({'message' : 'Internal error'})

if __name__ == "__main__":
    app.run(debug=True)