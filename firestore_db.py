# firestore_db.py
# Firestore database connection utility for the Cloud To-Do app.

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def get_db():
    """
    Initialize and return a Firestore client.
    Ensures the Firebase app is initialized only once per process.
    Returns:
        firestore.Client: The Firestore client instance.
    """
    if not firebase_admin._apps:
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
    return firestore.client()
