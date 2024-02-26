import pytest, requests

#CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []

#create
def test_create_task():
    new_task_data = {
        "title": "nova tarefa",
        "description": "descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200

    #recuperando resposta
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

#read
    #all
def test_read_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200

    response_json = response.json()
    assert 'tasks' in response_json
    assert 'total_tasks' in response_json 

    #only one
def test_read_only_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200

        response_json = response.json()
        assert task_id == response_json['id']

#update
def test_update_tasks():
    if tasks:
        task_id = tasks[0]
        payload = {
            'completed': False,
            'description':'Nova descrição',
            'title':'Titulo atualizado'
        }

        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200

        response_json = response.json()
        assert "message" in response_json

        #new task request
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200

        response_json = response.json()
        assert response_json['title'] == payload['title']
        assert response_json['description'] == payload['description']
        assert response_json['completed'] == payload['completed']

#delete
def delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f'{BASE_URL}/tasks/{task_id}')

        assert response.status_code == 200

        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 404