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
   git clone [https://github.com/yourusername/django-blog-project.git](https://github.com/akshayambulgekar/Blog_Project.git)
   cd django-blog-project

2. **Create a virtual environment:**
   ```bash
      python -m venv venv


3. **Activate the virtual environment:**
  
   ```bash
   venv\Scripts\activate


4. **Install the dependencies:**
   
   ```bash
      pip install -r requirements.txt


5. **Apply the migrations:**

   ```bash
      python manage.py migrate
6. **createsuperuser**
   ```bash
      python manage.py createsuperuser

7. ***Run the development server***:
   ```bash
      python manage.py runserver

8. **API Endpoints**
   Here are the available API endpoints:
   - Register User: POST /api/register/
   -Login User: POST /api/token/ (obtain JWT)
   -Refresh Token: POST /api/token/refresh/
   -List Posts: GET /api/posts/
   -Create Post: POST /api/posts/ (Authenticated users)
   -Retrieve Post: GET /api/posts/<id>/
   -Update Post: PUT /api/posts/<id>/ (Authenticated and authorized users)
   -Delete Post: DELETE /api/posts/<id>/ (Authenticated and authorized users)



