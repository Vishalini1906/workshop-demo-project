#!/usr/bin/env python3
import sys

# In-memory storage
tasks = {}
next_id = 1

def add(task_name):
    global next_id
    task_id = next_id
    tasks[task_id] = {'name': task_name, 'done': False}
    next_id += 1
    return task_id

def list_tasks():
    return tasks

def done(task_id):
    if task_id in tasks:
        tasks[task_id]['done'] = True
        return True
    return False

def delete(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False

def process_command(args):
    if not args:
        print("Commands: add <task>, list, done <id>, delete <id>")
        return

    command = args[0]
    if command == "add":
        if len(args) < 2:
            print("Usage: add <task>")
        else:
            task_name = " ".join(args[1:])
            tid = add(task_name)
            print(f"Added task {tid}")
    elif command == "list":
        if not tasks:
            print("No tasks.")
        else:
            for tid, task in tasks.items():
                status = "[x]" if task['done'] else "[ ]"
                print(f"{tid}: {status} {task['name']}")
    elif command == "done":
        if len(args) < 2 or not args[1].isdigit():
            print("Usage: done <id>")
        else:
            tid = int(args[1])
            if done(tid):
                print(f"Task {tid} marked as complete")
            else:
                print(f"Task {tid} not found")
    elif command == "delete":
        if len(args) < 2 or not args[1].isdigit():
            print("Usage: delete <id>")
        else:
            tid = int(args[1])
            if delete(tid):
                print(f"Task {tid} deleted")
            else:
                print(f"Task {tid} not found")
    else:
        print("Unknown command")

if __name__ == "__main__":
    # If arguments are passed, process them (single-shot)
    if len(sys.argv) > 1:
        process_command(sys.argv[1:])
    else:
        # Interactive mode to maintain in-memory state
        print("In-Memory To-Do List")
        print("Commands: add <task>, list, done <id>, delete <id>, exit")
        while True:
            try:
                line = input("> ").strip()
                if not line:
                    continue
                if line == "exit":
                    break
                process_command(line.split())
            except EOFError:
                print()
                break
            except KeyboardInterrupt:
                print()
                break
