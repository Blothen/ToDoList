import json


def create_empty_json(file_path):
    try:
        empty_data = {
            "counter": 0,
            "data": []
        }
        with open(file_path, 'w') as file:
            json.dump(empty_data, file, indent=2)

        print(f"Empty JSON file created successfully at '{file_path}'.")
    except Exception as e:
        print(f"Error: {str(e)}")


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON from file '{file_path}'.")
        return None


def add_data_to_json(file_path, new_string):
    new_boolean = False
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
        if 'counter' not in existing_data:
            existing_data['counter'] = 1
        else:
            existing_data['counter'] += 1
        new_data = {
            'task': new_string,
            'completed': new_boolean
        }
        existing_data['data'].append(new_data)
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=2)
        print("Data appended and counter incremented successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON from file '{file_path}'.")
    except Exception as e:
        print(f"Error: {str(e)}")


def remove_and_decrement(file_path, task_to_remove):
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
        if 'counter' not in existing_data:
            existing_data['counter'] = 0
        if 'data' not in existing_data:
            print("Error: 'data' key not found in the JSON file.")
            return
        task_found = False
        for item in existing_data['data']:
            if 'task' in item and item['task'] == task_to_remove:
                task_found = True
                existing_data['counter'] = max(0, existing_data['counter'] - 1)
                existing_data['data'].remove(item)
                break
        if task_found:
            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=2)
            print(f"Task '{task_to_remove}' removed successfully. Counter decremented.")
        else:
            print(f"Error: Task '{task_to_remove}' not found in the 'data' array.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON from file '{file_path}'.")
    except Exception as e:
        print(f"Error: {str(e)}")


def update_status(user, task_str, file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if 'data' in data:
            tasks = data['data']
            task_index = find_task_index(tasks, task_str)

            if task_index is not None:
                tasks[task_index]['completed'] = True
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=2)
                print(f"Status updated for task '{task_str}' for user '{user}'.")
            else:
                print(f"Task '{task_str}' not found.")
        else:
            print("Invalid JSON structure. 'data' key not found.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON from file '{file_path}'.")
    except Exception as e:
        print(f"Error: {str(e)}")


def find_task_index(tasks, task_str):
    # Helper function to find the index of a task in the list
    for i, task in enumerate(tasks):
        if task['task'] == task_str:
            return i
    return None