# FastAPI Social Media API

A RESTful API built with FastAPI as part of my backend engineering learning journey.

This project covers the core concepts of building a modern backend application including authentication, database management, testing, Docker, and CI/CD.

---

## Features

- User Registration
- User Authentication (JWT)
- Create, Read, Update and Delete Posts
- Voting System
- Authorization (Users can only modify their own posts)
- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Database Migrations
- Automated Testing with Pytest
- Docker & Docker Compose
- GitHub Actions CI

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT Authentication
- Passlib (bcrypt)
- Pytest
- Docker
- GitHub Actions

---

## Project Structure

```
app/
│
├── routers/
├── models.py
├── schemas.py
├── database.py
├── oauth2.py
├── utils.py
├── config.py
├── main.py
│
tests/
│
alembic/
│
.github/workflows/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Abdullah-Shomer/fastapi-project.git
```

Go into the project

```bash
cd fastapi-project
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

Example:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=your_password

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

Interactive API documentation:

```
http://localhost:8000/docs
```

---

## Database Migration

Create migration

```bash
alembic revision --autogenerate -m "message"
```

Run migrations

```bash
alembic upgrade head
```

---

## Running Tests

```bash
pytest
```

or

```bash
pytest -v
```

---

## Docker

Build

```bash
docker compose up --build
```

Run

```bash
docker compose up
```

---

## Continuous Integration

This project uses **GitHub Actions** to automatically:

- Install dependencies
- Run automated tests
- Validate every push and pull request

---

## What I Learned

During this project I learned:

- Building REST APIs with FastAPI
- Database Design with PostgreSQL
- SQLAlchemy ORM
- Alembic Migrations
- JWT Authentication & Authorization
- Dependency Injection
- API Testing with Pytest
- Docker & Docker Compose
- GitHub Actions CI
- Backend Project Structure
- Basic Deployment Workflow

---

## Future Improvements

- Pagination
- Search & Filtering
- User Profiles
- Comments
- Image Uploads
- Refresh Tokens
- Email Verification
- Password Reset
- Rate Limiting
- Caching with Redis

---

## License

This project was built for educational purposes while learning FastAPI and Backend Development.
