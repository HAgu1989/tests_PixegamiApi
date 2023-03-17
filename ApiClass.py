import uuid
import requests

# Class definition of api endpoints.
# If somthing change in API structure its one point change wihout need to refactor whole code
class Pixegami:
    def __init__(self) -> None:
        self.root = "https://todo.pixegami.io/"
        self.createTask = 'https://todo.pixegami.io/create-task'
        self.getTask = 'https://todo.pixegami.io/get-task/'  # + task_id
        self.getTaskList = 'https://todo.pixegami.io/list-tasks/'  # + user_id
        self.updateTask = "https://todo.pixegami.io/update-task"
        self.deleteTask = "https://todo.pixegami.io/delete-task/"  # + task_id
        
# Method used to generate uniqe test data

    @staticmethod
    def newPayload():
        user_id = f"test_user_{uuid.uuid4().hex}"
        content = f"content_{uuid.uuid4().hex}"
        return {
            "content": content,
            "user_id": user_id,
            "is_done": False,
        }

    def get_root(self):
        response = requests.get(self.root)
        return response

    def create_task(self, payload):
        response = requests.put(
            self.createTask, json=payload)
        return response

    def get_task(self, task_id):
        response = requests.get(self.getTask+task_id)
        return response

    def get_task_list(self, user_id):
        response = requests.get(self.getTaskList+user_id)
        return response

    def update_task(self, task_id, user_id):
        new_payload = Pixegami.newPayload()
        response = requests.put(self.updateTask, json={
            "content": new_payload["content"],
            "user_id": user_id,
            "task_id": task_id,
            "is_done": False
        })
        return response

    def delete_task(self, task_id):
        response = requests.delete(self.deleteTask+task_id)
        return response
