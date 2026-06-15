# Repository Pattern — Python

Ejemplo del patrón Repository del catálogo de Fowler implementado en Python.

## Estructura

src/
├── models.py       # Entidad User
├── repository.py   # Interfaz + SQLite + InMemory
└── service.py      # Lógica de negocio

tests/
└── test_user_service.py

## Correr tests

pip install -r requirements.txt
pytest tests/ -v

## CI/CD

GitHub Actions corre los tests automáticamente en cada push a `main`.