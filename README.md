# Overview

This project is a Cloud To-Do List application built to strengthen my skills as a software engineer working with cloud data storage. The program uses Python to connect to a Google Firebase Firestore database (NoSQL) through an API, allowing the application to store and manage data in the cloud.


The application provides a simple command-line menu that lets a user create accounts and manage tasks. It demonstrates full CRUD functionality (create, read/query, update, delete) on data stored in Firestore. Tasks are related to users through a `user_id` field to demonstrate working with related collections.


My purpose for writing this software was to practice building a real program that integrates with a cloud database, including secure credential handling, queries, and clean modular code organization.


[Software Demo Video](https://youtu.be/h_fRlOW_Ld4)

# Cloud Database

I used Google Firebase Firestore as the cloud database for this project. Firestore is a NoSQL document (key/value) database that stores data in collections and documents and supports queries and updates through its API.

Database structure:
- `users` collection: stores user documents (name, email)
- `tasks` collection: stores task documents (title, completed, user_id)
The relationship is implemented by storing the Firestore user document id in each task as `user_id`.

# Development Environment

Tools used:
- Visual Studio Code
- Firebase Console (Firestore Database)
- Git and GitHub

Language and libraries:
- Python 3
- firebase-admin (Firebase Admin SDK for Firestore access)

# Useful Websites

- [Firebase Documentation](https://firebase.google.com/docs)
- [Firestore Documentation](https://firebase.google.com/docs/firestore)
- [Firebase Admin SDK for Python](https://firebase.google.com/docs/admin/setup)

# Future Work

- Add input validation (ex: prevent empty names/tasks and validate email format)
- Add a feature to automatically delete all tasks when a user is deleted
- Add authentication so each user can only manage their own tasks