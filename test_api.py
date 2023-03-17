from ApiClass import Pixegami
import requests

api = Pixegami()


def test_can_open():
    data = api.get_root()
    assert data.status_code == 200


def test_can_create_task():
    payload = Pixegami.newPayload()
    data = api.create_task(payload)
    assert data.status_code == 200
    task_id = data.json()["task"]["task_id"]
    response = api.get_task(task_id)
    assert response.status_code == 200


def test_can_get_task_list():
    n = 3
    payload = Pixegami.newPayload()
    for i in range(n):
        response = api.create_task(payload)
        assert response.status_code == 200
    data = api.get_task_list(response.json()['task']['user_id'])
    assert len(data.json()["tasks"]) == n


def test_can_update_task():
    payload = Pixegami.newPayload()
    data = api.create_task(payload)
    assert data.status_code == 200
    userid = data.json()['task']['user_id']
    taskid = data.json()['task']['task_id']
    response = api.update_task(taskid, userid)
    assert response.status_code == 200
    updated_data = api.get_task(taskid)
    assert updated_data.status_code == 200
    assert data.json()['task']['content'] != updated_data.json()['content']
    assert data.json()['task']['user_id'] == updated_data.json()['user_id']


def test_can_delete_task():
    payload = Pixegami.newPayload()
    task = api.create_task(payload)
    assert task.status_code == 200
    taskId = task.json()['task']['task_id']
    del_response = api.delete_task(taskId)
    assert del_response.status_code == 200
    get_response = api.get_task(taskId)
    assert get_response.status_code == 404
