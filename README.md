# Minimal In-Memory CLI To-Do List

A simple, in-memory command-line interface (CLI) to-do list application written in Python.

## Running the App

The application uses an interactive prompt to maintain the in-memory state of your tasks during the session.

Start the app:
```bash
./todo.py
# or
python3 todo.py
```

Inside the interactive prompt, you can use the following commands:
- `add <task>`: Adds a new task and assigns it an ID.
- `list`: Lists all tasks along with their completion status.
- `done <id>`: Marks the task with the given ID as complete.
- `delete <id>`: Deletes the task with the given ID.
- `exit`: Exits the application.

Example session:
```text
$ ./todo.py
In-Memory To-Do List
Commands: add <task>, list, done <id>, delete <id>, exit
> add Buy milk
Added task 1
> add Read book
Added task 2
> list
1: [ ] Buy milk
2: [ ] Read book
> done 1
Task 1 marked as complete
> list
1: [x] Buy milk
2: [ ] Read book
> delete 2
Task 2 deleted
> list
1: [x] Buy milk
> exit
```

## Running Tests

Automated tests are included to verify the core functions (add, done, delete). Since there are zero external dependencies, they can be run using Python's built-in `unittest` framework:

```bash
python3 -m unittest test_todo.py
```
