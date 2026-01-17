# TaskMaster API

A RESTful API for managing tasks with user authentication, built with Flask and PostgreSQL.

## Features

- User registration and authentication
- JWT-based authorization
- Full CRUD operations for tasks
- User-specific task management
- Secure password hashing
- PostgreSQL database

## Technologies Used

- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** Flask-JWT-Extended
- **Security:** Werkzeug (password hashing)

## API Endpoints

### Authentication
- `POST /api/register` - Register a new user
- `POST /api/login` - Login and get JWT token

### Tasks (Protected - Requires JWT)
- `GET /api/tasks` - Get all tasks for logged-in user
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/<id>` - Get a specific task
- `PUT /api/tasks/<id>` - Update a task
- `DELETE /api/tasks/<id>` - Delete a task

## Future Improvements

This project is actively being developed, and I plan to implement the following enhancements:

- **CI/CD Pipeline**: Implement automated testing and deployment using GitHub Actions
- **Web Dashboard**: Build a responsive web interface 
- **Email Verification**: Add email verification for new user registrations
- **Password Reset**: Implement secure password reset functionality
- **Task Categories**: Allow users to organize tasks into categories/projects
- **Task Priority & Due Dates**: Add priority levels and deadline tracking
- **Task Sharing**: Enable task collaboration between users
- **Search & Filtering**: Advanced search and filtering capabilities for tasks


