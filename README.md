---

```markdown
# Task Management API

A Django REST Framework-based API for managing users, tasks, and user profiles with secure JWT authentication and role-based access control.

## Features

- JWT Authentication using `djangorestframework-simplejwt`
- User registration and login system
- Authenticated users can manage their own tasks
- Admins can view all user profiles and their tasks
- Role-based permissions using DRF's permission system
- Optional request profiling using `django-silk`

## Technology Stack

- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (can be switched to PostgreSQL or another database)
- Optional: `django-silk` for request profiling

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-project-directory>
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

## API Overview

### Authentication

- Obtain Token: `POST /mainpage/api/token/`
- Refresh Token: `POST /mainpage/api/token/refresh/`

All protected endpoints require an access token in the header:

```
Authorization: Bearer <your_access_token>
```

### User Registration

- `POST /mainpage/api/register/`

Payload:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Task Endpoints (Authenticated Users Only)

- `GET /mainpage/task/`: List the tasks created by the current user
- `POST /mainpage/task/`: Create a new task

### Profile Endpoints (Admin Only)

- `GET /mainpage/profile/`: View all user profiles and their tasks


## Example Requests

### Register a New User

```bash
curl -X POST http://localhost:8000/mainpage/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass"}'
```

### Obtain JWT Token

```bash
curl -X POST http://localhost:8000/mainpage/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass"}'
```
