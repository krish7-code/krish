import json
import os

FILE = 'todo.json'

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
def show_menu():
    print("\nTo-Do App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Task name: ")
            task_id = len(tasks) + 1
            tasks.append({"id": task_id, "task": name, "status": "pending"})
            save_tasks(tasks)
            print("Task added!")

        elif choice == '2':
            for t in tasks:
                print(f"{t['id']}: {t['task']} [{t['status']}]")

        elif choice == '3':
            tid = int(input("Enter task ID to update: "))
            for t in tasks:
                if t['id'] == tid:
                    t['status'] = input("New status (pending/done): ")
                    break
            save_tasks(tasks)

        elif choice == '4':
            tid = int(input("Enter task ID to delete: "))
            tasks = [t for t in tasks if t['id'] != tid]
            save_tasks(tasks)

        elif choice == '5':
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
