# Django Blog Project

A simple blog application built with Django, featuring user authentication, CRUD operations for blog posts, and both API and HTML views.

## Features

- User Registration and Login
- JWT Authentication for API endpoints
- CRUD operations for blog posts
- Role-based access to create, update, and delete posts
- Responsive design for user interfaces
- API Endpoints to manage posts

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default for Django, can be switched to PostgreSQL, MySQL, etc.)
- **Authentication**: Django Authentication System, JWT (JSON Web Tokens)

## Prerequisites

- Python 3.6 or higher
- Django 3.2 or higher
- Django REST Framework
- Django Simple JWT

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/django-blog-project.git
   cd django-blog-project

2. **Install Dependencies**
   ```bash
      npm install

3. **Set Up Environment Variables**
   Create a .env file in the root directory of the project and add the following environment variable:
   ```bash
   MONGODB_URI=mongodb://localhost:27017/todo-list-app
   PORT=3000

4. **Ensure MongoDB is Running**
   For a local MongoDB installation, ensure the MongoDB service is running. Open a terminal and start the MongoDB server:
   ```bash
      mongod

5. **Running the Application**
   To start the application, run:
   ```bash
      npm start

   Or, if you prefer using nodemon for development (auto-restarts the server on changes):
   ```bash
   npm run dev

6. **API Endpoints**
   Here are the available API endpoints:
   - GET /api/tasks: Retrieve a list of all tasks.
   - GET /api/tasks/: Retrieve a single task by its ID.
   - POST /api/tasks: Create a new task.
   - PUT /api/tasks/: Update an existing task.
   - DELETE /api/tasks/: Delete a task.



