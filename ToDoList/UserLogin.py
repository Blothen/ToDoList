import yaml
import hashlib


db_file = "./storage/users.yaml"


def check_credentials(username, password):
    password_hash = hashlib.md5(password.encode()).hexdigest()

    try:
        with open(db_file, "r") as f:
            try:
                data = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f"YAML parsing error: {e}")
                data = {'username': [], 'passwords': {}}

        usernames = data.get('username', [])
        passwords = data.get('passwords', {})

        if username in usernames and passwords.get(username) == password_hash:
            return True
        else:
            return False

    except FileNotFoundError:
        print(f"Error: File '{db_file}' not found.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
