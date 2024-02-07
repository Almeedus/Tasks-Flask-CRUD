from flask import Flask, request, jsonify
from models.task import Task
app =  Flask(__name__)

tasks = []
tasks_id_control = 1
@app.route('/tasks', methods=['POST'])
def create_task():
    global tasks_id_control
    data = request.get_json()
    new_task = Task(id=tasks_id_control, title=data['title'], description= data.get('description', ''))
    tasks_id_control += 1
    tasks.append(new_task)
    return jsonify({'message': 'Nova tarefa criada com sucesso.'})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks_list = []
    tasks_total = 0
    
    for task in tasks:
        tasks_list.append(task.to_dict())
        tasks_total += 1

    output = {
        "tasks": tasks_list,
        "total_tasks": tasks_total
    }

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)