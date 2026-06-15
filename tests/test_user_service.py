import pytest
from src.models import User
from src.repository import InMemoryUserRepository
from src.service import UserService


@pytest.fixture
def service():
    return UserService(InMemoryUserRepository())


def test_register_user(service):
    user = service.register_user("Ana Torres", "ana@example.com")
    assert user.id is not None
    assert user.name == "Ana Torres"
    assert user.email == "ana@example.com"


def test_register_invalid_email(service):
    with pytest.raises(ValueError):
        service.register_user("Carlos", "no-es-email")


def test_register_missing_fields(service):
    with pytest.raises(ValueError):
        service.register_user("", "algo@example.com")


def test_get_user(service):
    user = service.register_user("Ana Torres", "ana@example.com")
    found = service.get_user(user.id)
    assert found.name == "Ana Torres"


def test_get_user_not_found(service):
    with pytest.raises(ValueError):
        service.get_user(999)


def test_remove_user(service):
    user = service.register_user("Luis", "luis@example.com")
    assert service.remove_user(user.id) is True


def test_remove_user_not_found(service):
    assert service.remove_user(999) is False


def test_list_users(service):
    service.register_user("Maria", "maria@example.com")
    service.register_user("Pedro", "pedro@example.com")
    assert len(service.list_users()) == 2