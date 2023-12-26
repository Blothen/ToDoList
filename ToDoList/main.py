import json
import yaml
import hashlib

db_file = "../storage/users.yaml"  # Replace with the actual file name and extension


def check_user(user):
    with open(db_file, "r") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError:
            data = {'username': [], 'passwords': {}}

    return user in data.get('username', [])


def check_password(password):
    password_hash = hashlib.md5(password.encode()).hexdigest()
    with open(db_file, "r") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError:
            data = {'username': [], 'passwords': {}}

    return password_hash in data.get('passwords', {}).values()


def get_user(user, passwd):
    password_hash = hashlib.md5(passwd.encode()).hexdigest()
    return check_user(user) and check_password(password_hash)


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
            print("Added user:", user)
            print(yaml.dump(data, default_flow_style=False))


if __name__ == '__main__':
    add_user("new_user", "new_password")
