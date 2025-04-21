# Task Management API

A Django REST API for task management with JWT authentication, caching, filtering, and pagination capabilities.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [Authentication Endpoints](#authentication-endpoints)
  - [User Endpoints](#user-endpoints)
  - [Task Endpoints](#task-endpoints)
  - [Profile Endpoints](#profile-endpoints)
- [Request Examples](#request-examples)
- [Response Examples](#response-examples)
- [Error Handling](#error-handling)
- [Security Considerations](#security-considerations)

## Overview

This Task Management API allows users to create and manage tasks through a RESTful interface. The API implements JWT authentication to secure endpoints, server-side caching using redis for improved performance, and robust filtering and pagination to handle large datasets efficiently.

## Features

- **JWT Authentication**: Secure endpoints with JSON Web Tokens
- **Role-based Access Control**: Different permissions for regular users and admin users
- **Redis Caching**: Improved performance with cached responses
- **Search & Filtering**: Find tasks and profiles using search parameters
- **Pagination**: Handle large datasets efficiently
- **Task Management**: Create, read, update, and delete tasks
- **User Profiles**: Manage user profiles and associated tasks

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mohamedkamelx/todo-api.git
cd todo-api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Install docker and run redis container at port 6379:


6. Start the development server:
```bash
python manage.py runserver
```

## Authentication

The API uses JWT (JSON Web Token) authentication. To access protected endpoints, you need to:

1. Register a new user or use existing credentials to obtain a token
2. Include the access token in the Authorization header for subsequent requests
3. Refresh the token when it expires

## API Endpoints

### Authentication Endpoints

| Endpoint | Method | Description | Authentication Required |
|----------|--------|-------------|------------------------|
| `/mainpage/api/register/` | POST | Register a new user | No |
| `/mainpage/api/token/` | POST | Obtain JWT token | No |
| `/mainpage/api/token/refresh/` | POST | Refresh JWT token | No |

### User Endpoints

| Endpoint | Method | Description | Authentication Required |
|----------|--------|-------------|------------------------|
| `/mainpage/myprofile/` | GET | Get current user's profile | Yes |

### Task Endpoints

| Endpoint | Method | Description | Authentication Required |
|----------|--------|-------------|------------------------|
| `/mainpage/task/` | GET | List all tasks for the authenticated user | Yes |
| `/mainpage/task/` | POST | Create a new task | Yes |
| `/mainpage/task/{id}/` | GET | Retrieve a specific task | Yes |
| `/mainpage/task/{id}/` | PUT | Update a specific task | Yes |
| `/mainpage/task/{id}/` | DELETE | Delete a specific task | Yes |

### Profile Endpoints

| Endpoint | Method | Description | Authentication Required |
|----------|--------|-------------|------------------------|
| `/mainpage/profile/` | GET | List all profiles (admin only) | Yes (Admin) |
| `/mainpage/profile/{id}/` | GET | Retrieve a specific profile (admin only) | Yes (Admin) |

## Request Examples

### Register a new user

```bash
curl -X POST http://localhost:8000/mainpage/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "newuser", "password": "securepassword123"}'
```

### Obtain JWT token

```bash
curl -X POST http://localhost:8000/mainpage/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "myusername", "password": "mypassword"}'
```

### Refresh JWT token

```bash
curl -X POST http://localhost:8000/mainpage/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token_here"}'
```

### Get current user's profile

```bash
curl -X GET http://localhost:8000/mainpage/myprofile/ \
  -H "Authorization: Bearer your_access_token_here"
```

### List all tasks for the authenticated user

```bash
curl -X GET http://localhost:8000/mainpage/task/ \
  -H "Authorization: Bearer your_access_token_here"
```

### Create a new task

```bash
curl -X POST http://localhost:8000/mainpage/task/ \
  -H "Authorization: Bearer your_access_token_here" \
  -H "Content-Type: application/json" \
  -d '{"title": "New Task", "description": "Task description"}'
```

## Response Examples

### Successful login (token creation)

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Get user profile

```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "username"
  },
  "tasks": [
    {
      "id": 1,
      "title": "Task 1",
      "description": "Description for task 1",
      "created_at": "2025-04-20T14:30:00Z"
    },
    {
      "id": 2,
      "title": "Task 2",
      "description": "Description for task 2",
      "created_at": "2025-04-21T10:15:00Z"
    }
  ]
}
```

### List tasks (with pagination)

```json
{
  "count": 10,
  "next": "http://localhost:8000/mainpage/task/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Task 1",
      "description": "Task description",
      "created_at": "2025-04-20T14:30:00Z",
      "user": 1
    },
    {
      "id": 2,
      "title": "Task 2",
      "description": "Another description",
      "created_at": "2025-04-21T10:15:00Z",
      "user": 1
    }
    // ...more tasks (up to page_size)
  ]
}
```
