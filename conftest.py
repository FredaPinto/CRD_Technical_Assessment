import pytest


@pytest.fixture(scope="session")
def userLogin():
    print("I have logged in as user abc")