# ToDoList Flask Application

This is a simple Flask application for managing a to-do list. The application includes user authentication (login and registration) and allows users to add, remove, and mark tasks as complete.

## Dependencies

The application uses the following dependencies:
- `Flask`: Web framework for building the application.
- `flask_cors`: Enables Cross-Origin Resource Sharing (CORS) for the application.

## File Structure

The application consists of the following files and directories:

- `app.py`: The main file containing the Flask application.
- `ToDoList/main.py`: Module for handling tasks (retrieve, add, remove, complete).
- `ToDoList/UserCheck.py`: Module for checking user existence.
- `ToDoList/UserRegistration.py`: Module for adding new users.
- `ToDoList/UserLogin.py`: Module for checking user credentials.
- `ToDoList/json_operations.py`: Module containing functions for working with JSON files.

## JSON Operations

### `json_operations.py`

#### `create_empty_json(file_path)`

This function creates an empty JSON file at the specified `file_path`. The JSON file has a predefined structure containing a counter and an empty data array. The counter keeps track of the total number of tasks in the to-do list, and the data array stores individual tasks with their completion status.

#### `read_json_file(file_path)`

This function reads and returns the content of the JSON file at the specified `file_path`. It handles FileNotFoundError gracefully by printing an error message, and in case of a JSONDecodeError, it returns None. This ensures that the application can recover from missing or corrupted JSON files.

#### `add_data_to_json(file_path, new_string)`

This function reads an existing JSON file, increments the counter, and appends new data to the data array. It expects a JSON string (`new_string`) as input, representing the new task to be added. The updated JSON is then written back to the file. This function ensures that each task is uniquely identified by incrementing the counter.

#### `remove_and_decrement(file_path, task_to_remove)`

This function reads an existing JSON file, searches for a task with the specified name, removes it, and decrements the counter. It handles cases where the task is not found or the JSON structure is invalid, providing informative error messages. This ensures robustness in task removal operations.

#### `update_status(user, task_str, file_path)`

This function reads an existing JSON file, updates the status of a task to completed, and writes the changes back to the file. It expects the user, task string, and file path as input. The completion status is updated within the JSON structure, ensuring accurate tracking of completed tasks.

#### `find_task_index(tasks, task_str)`

This is a helper function that searches for the index of a task in a list based on the task string. It is utilized in the `update_status` function to locate the position of the task within the data array.

## Routes

### `/`

- **Method**: GET
- If the user is logged in, redirects to the `/todo` page; otherwise, renders the `index.html` template and sets a cookie indicating that the user is not logged in.

### `/login`

- **Method**: POST
- Authenticates the user based on the provided username and password.
- If authentication is successful, redirects to the `/todo` page and sets cookies for the username and logged-in status.
- If authentication fails, returns "incorrect password."

### `/register`

- **Method**: POST
- Registers a new user with the provided username and password.
- If successful, redirects to the `/todo` page and sets cookies for the username and logged-in status.
- If the username already exists, returns a message indicating that the username is taken.

### `/todo`

- **Methods**: GET, POST
- Retrieves tasks for the logged-in user and renders the `todo.html` template with user information and tasks.

### `/todo/add/<task>`

- **Method**: POST
- Adds a new task for the logged-in user.
- Expects JSON data with the new task.
- Returns a JSON response indicating success or an error message.

### `/todo/remove/<task>`

- **Method**: POST
- Removes a task for the logged-in user.
- Expects the task to be removed as part of the URL.
- Returns a JSON response indicating success or an error message.

### `/todo/complete/<task>`

- **Method**: POST
- Marks a task as complete for the logged-in user.
- Expects the task to be marked as complete as part of the URL.
- Returns a JSON response indicating success or an error message.

### `/logout`

- **Method**: GET
- Logs out the user by deleting cookies for the username and logged-in status.
- Redirects to the home page.

## Running the Application

The application can be run by executing the `app.py` file.
```bash
python app.py
