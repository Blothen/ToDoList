import yaml

db_file = "./storage/users.yaml"


def check_user(user):
    try:
        with open(db_file, "r+") as f:
            try:
                data = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f"YAML parsing error: {e}")

            if data is None or 'username' not in data or user not in data['username']:
                return False
            else:
                return True
    except FileNotFoundError:
        print(f"Error: File '{db_file}' not found.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
