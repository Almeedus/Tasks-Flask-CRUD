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
        "total_tasks": len(tasks_list)
    }

    return jsonify(output)

#permite que receba na rota um parametro
@app.route('/tasks/<int:id>', methods=['GET']) #parametro de rota
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

#nessa rota recebemos tanto o parametro na rota quanto um corpo de requisição
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = None
    for t in tasks:
        if t.id == task_id:
            task = t
            break

    if task == None:
        return jsonify({'message': "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    return jsonify({'message': 'Tarefa atualizada com sucesso'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = None
    for t in tasks:
        if t.id == task_id:
            task = t
            break
    
    if task == None:
        return jsonify({'message': "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({'message': 'Tarefa deletada com sucesso.'})
            

if __name__ == "__main__":
    app.run(debug=True)