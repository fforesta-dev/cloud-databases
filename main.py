# main.py
# Cloud To-Do app using Firestore (NoSQL key/value cloud database).
#
# This script provides a command-line interface for managing users and tasks
# in a Firestore database. It demonstrates CRUD operations on two related
# collections: users and tasks.

from crud import (
    create_user,  # Create a new user
    list_users,  # List all users
    delete_user,  # Delete a user by ID
    create_task,  # Create a new task for a user
    list_tasks,  # List all tasks or tasks for a user
    update_task,  # Update a task's title or completion status
    delete_task,  # Delete a task by ID
)


def print_users():
    """
    Fetch and print all users from the database.
    """
    users = list_users()
    if not users:
        print("\n(no users found)")
        return
    print("\nUSERS:")
    for u in users:
        print(f"- {u['id']} | {u['name']} | {u['email']}")


def print_tasks(user_id=None):
    """
    Fetch and print tasks. If user_id is provided, filter by user.
    """
    tasks = list_tasks(user_id=user_id)
    if not tasks:
        print("\n(no tasks found)")
        return
    print("\nTASKS:")
    for t in tasks:
        status = "✅" if t.get("completed") else "❌"
        print(f"- {t['id']} | {status} | {t['title']} | user_id={t['user_id']}")


def prompt_bool(message: str) -> bool:
    """
    Prompt the user for a yes/no answer. Returns True for yes, False for no.
    """
    while True:
        value = input(message).strip().lower()
        if value in ("y", "yes"):
            return True
        if value in ("n", "no"):
            return False
        print("Please type y/yes or n/no.")


def menu():
    """
    Main CLI menu loop for interacting with the Firestore Cloud To-Do app.
    Handles user input and calls CRUD operations.
    """
    while True:
        print(
            "\n=== CLOUD TODO (Firestore) ===\n"
            "1) List users\n"
            "2) Create user\n"
            "3) Delete user\n"
            "4) List tasks (all)\n"
            "5) List tasks for a user\n"
            "6) Create task\n"
            "7) Update task\n"
            "8) Delete task\n"
            "9) Exit\n"
        )
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print_users()
        elif choice == "2":
            user_id = input("User ID (optional, e.g. u001): ").strip() or None
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            new_id = create_user(name, email, user_id=user_id)
            print(f"✅ User created with ID: {new_id}")
        elif choice == "3":
            print_users()
            user_id = input("Enter user ID to delete: ").strip()
            delete_user(user_id)
            print("✅ User deleted.")
        elif choice == "4":
            print_tasks()
        elif choice == "5":
            print_users()
            user_id = input("Enter user ID to filter tasks: ").strip()
            print_tasks(user_id=user_id)
        elif choice == "6":
            print_users()
            user_id = input("Enter user ID for this task: ").strip()
            task_id = input("Task ID (optional, e.g. t001): ").strip() or None
            title = input("Task title: ").strip()
            new_id = create_task(user_id, title, task_id=task_id)
            print(f"✅ Task created with ID: {new_id}")
        elif choice == "7":
            print_tasks()
            task_id = input("Enter task ID to update: ").strip()
            change_title = prompt_bool("Change title? (y/n): ")
            new_title = input("New title: ").strip() if change_title else None
            change_status = prompt_bool("Change completed status? (y/n): ")
            completed = (
                prompt_bool("Mark completed? (y/n): ") if change_status else None
            )
            update_task(task_id, new_title=new_title, completed=completed)
            print("✅ Task updated.")
        elif choice == "8":
            print_tasks()
            task_id = input("Enter task ID to delete: ").strip()
            delete_task(task_id)
            print("✅ Task deleted.")
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-9.")


# Entry point for the CLI application
if __name__ == "__main__":
    menu()
