from pytest import fixture
from src.bhaskara import Bhaskara

@fixture
def bhaskara():
    return Bhaskara()