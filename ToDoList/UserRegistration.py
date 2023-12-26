import yaml
import hashlib
import json


db_file = "./storage/users.yaml"


def add_user(user, passwd):
    with open(db_file, "r+") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError:
            data = {'username': [], 'passwords': {}}

        if user not in data['username']:
            data['username'] = data['username'] + [user]
            password_hash = hashlib.md5(passwd.encode()).hexdigest()
            data['passwords'][user] = password_hash
            f.seek(0)
            yaml.dump(data, f, default_flow_style=False)
            f.truncate()
            f.seek(0)
            create_empty_json(user)
            print("Added user:", user)
        else:
            print("User already exists")


def create_empty_json(user):
    file_path = "./storage/" + user + ".json"
    try:
        # Define the initial structure of the JSON file
        empty_data = {
            "counter": 0,
            "data": []
        }
        with open(file_path, 'w') as file:
            json.dump(empty_data, file, indent=2)

        print(f"Empty JSON file created successfully at '{file_path}'.")
    except Exception as e:
        print(f"Error: {str(e)}")
