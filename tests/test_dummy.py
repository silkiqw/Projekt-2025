

def test_dummy():
    assert True  # Dieser Test wird immer erfolgreich sein


# Füge d

# Jetzt sollte der Import funktionieren
from ..wetter.meineApp.views import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    assert add(-1, 1) == 0

def test_add_zero():
    assert add(0, 5) == 5
    assert add(0, 0) == 0
