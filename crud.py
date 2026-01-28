from firestore_db import get_db

"""
crud.py
CRUD operations for users and tasks in the Firestore Cloud To-Do app.
Each function interacts with the Firestore database via get_db().
"""


def create_user(name: str, email: str, user_id: str | None = None) -> str:
    """
    Create a new user document in the 'users' collection.
    Args:
        name (str): The user's name.
        email (str): The user's email address.
    Returns:
        str: The Firestore document ID of the new user.
    """
    db = get_db()
    doc_ref = (
        db.collection("users").document(user_id)
        if user_id
        else db.collection("users").document()
    )
    doc_ref.set({"name": name, "email": email})
    return doc_ref.id


def list_users() -> list[dict]:
    """
    Retrieve all users from the 'users' collection.
    Returns:
        list[dict]: List of user documents with their IDs.
    """
    db = get_db()
    results = []
    for doc in db.collection("users").stream():
        data = doc.to_dict()
        data["id"] = doc.id
        results.append(data)
    return results


def delete_user(user_id: str) -> None:
    """
    Delete a user document by ID from the 'users' collection.
    Args:
        user_id (str): The Firestore document ID of the user to delete.
    """
    db = get_db()
    db.collection("users").document(user_id).delete()


def create_task(user_id: str, title: str, task_id: str | None = None) -> str:
    """
    Create a new task document in the 'tasks' collection for a user.
    Args:
        user_id (str): The ID of the user who owns the task.
        title (str): The title of the task.
    Returns:
        str: The Firestore document ID of the new task.
    """
    db = get_db()
    doc_ref = (
        db.collection("tasks").document(task_id)
        if task_id
        else db.collection("tasks").document()
    )
    doc_ref.set({"user_id": user_id, "title": title, "completed": False})
    return doc_ref.id


def list_tasks(user_id: str | None = None) -> list[dict]:
    """
    Retrieve tasks from the 'tasks' collection. Optionally filter by user_id.
    Args:
        user_id (str, optional): The user ID to filter tasks. Defaults to None.
    Returns:
        list[dict]: List of task documents with their IDs.
    """
    db = get_db()
    if user_id:
        query = db.collection("tasks").where("user_id", "==", user_id)
        stream = query.stream()
    else:
        stream = db.collection("tasks").stream()
    results = []
    for doc in stream:
        data = doc.to_dict()
        data["id"] = doc.id
        results.append(data)
    return results


def update_task(
    task_id: str, new_title: str | None = None, completed: bool | None = None
) -> None:
    """
    Update a task's title and/or completion status in the 'tasks' collection.
    Args:
        task_id (str): The Firestore document ID of the task to update.
        new_title (str, optional): The new title for the task.
        completed (bool, optional): The new completion status.
    """
    db = get_db()
    updates = {}
    if new_title is not None:
        updates["title"] = new_title
    if completed is not None:
        updates["completed"] = completed
    if updates:
        db.collection("tasks").document(task_id).update(updates)


def delete_task(task_id: str) -> None:
    """
    Delete a task document by ID from the 'tasks' collection.
    Args:
        task_id (str): The Firestore document ID of the task to delete.
    """
    db = get_db()
    db.collection("tasks").document(task_id).delete()
