from ToDoList.JsonHandler import read_json_file, add_data_to_json, remove_and_decrement, update_status
from ToDoList.UserRegistration import add_user


db_file = "./storage/users.yaml"


def retrieve_tasks(user):
    file = "./storage/" + user + ".json"
    data = read_json_file(file)
    return data


def add_tasks(user, task):
    file = "./storage/" + user + ".json"
    add_data_to_json(file, task)


def remove_tasks(user, task):
    file = "./storage/" + user + ".json"
    remove_and_decrement(file, task)


def complete_tasks(user, task):
    file = "./storage/" + user + ".json"
    update_status(user, task, file)


if __name__ == '__main__':
    db_file = "../storage/users.yaml"
    add_user("admin", "admin", db_file)
    add_tasks("admin", "admin", True)
    retrieve_tasks("admin")
    #remove_tasks("admin", "admin")
    retrieve_tasks("admin")
