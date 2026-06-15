# Repository Pattern — Python

Demonstration project for the article "Repository Pattern: The Pattern That Keeps Your Code Clean and Testable" published on Medium.  
Implements the Repository Pattern applied to a user management system.

## Requirements

- Python 3.11 or higher

## Install

```bash
pip install -r requirements.txt
```

## Test

```bash
pytest tests/ -v
```

## Project Structure
├── src/

│   ├── models.py         # User entity

│   ├── repository.py     # Interface + SQLite + InMemory

│   └── service.py        # Business logic

├── tests/

│   └── test_user_service.py

└── .github/workflows/    # CI/CD pipeline

## Article

[Repository Pattern: The Pattern That Keeps Your Code Clean and Testable](https://medium.com/p/c1d7fea6bd9e)

## Student

Junior Mamani Estaña