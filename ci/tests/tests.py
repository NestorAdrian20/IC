import pytest
from .sumas import Suma

# Create your tests here.

class TestSuma:
    def test_prueba(self):
        suma = Suma()
        assert suma.suma() == 35

