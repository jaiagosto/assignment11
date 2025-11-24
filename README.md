# Module 11 - IS601 Calculator Assignment

## Overview
This project implements a FastAPI calculator application with SQLAlchemy polymorphic models and Pydantic schemas for validation.

## Features
- ✅ Polymorphic SQLAlchemy models (Addition, Subtraction, Multiplication, Division)
- ✅ Pydantic schemas with validation
- ✅ Factory pattern for calculation types
- ✅ Comprehensive unit and integration tests
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Docker containerization

## Project Structure
```
assignment11/
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── calculation.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── calculation.py
│   ├── __init__.py
│   ├── database.py
│   └── operations.py
├── tests/
│   ├── unit/
│   │   └── test_calculator.py
│   ├── integration/
│   │   ├── test_calculation.py
│   │   ├── test_calculation_schema.py
│   │   └── test_fastapi_calculator.py
│   └── e2e/
│       ├── conftest.py
│       └── test_e2e.py
├── templates/
│   └── index.html
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── main.py
├── requirements.txt
├── pytest.ini
├── Dockerfile
├── docker-compose.yml
├── .env
└── .gitignore
```

## Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd assignment11
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run unit tests only
```bash
pytest tests/unit/ -v
```

### Run integration tests only
```bash
pytest tests/integration/ -v
```

### Run with coverage
```bash
pytest --cov=app --cov-report=html
```

## Running the Application

### Locally
```bash
python main.py
```
Then visit: http://127.0.0.1:8000

### With Docker Compose
```bash
docker-compose up --build
```

## Key Concepts

### Polymorphic Inheritance
The Calculation model uses SQLAlchemy's polymorphic inheritance:
- Single table stores all calculation types
- `type` column discriminates between subclasses
- Factory pattern creates appropriate subclass

### Pydantic Validation
Schemas validate data at the API boundary:
- Field validators for type normalization
- Model validators for cross-field validation
- Division by zero prevention

## Docker Hub
Docker image: `<your-dockerhub-username>/assignment11:latest`

## CI/CD Pipeline
- ✅ Automated testing on push
- ✅ Security scanning with Trivy
- ✅ Docker image deployment to Docker Hub

## Author
Jailene Agosto

## License
MIT# Module 11 - IS601 Calculator Assignment
