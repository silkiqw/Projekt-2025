
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from wetter.meineApp.views import add  # Jetzt sollte es klappen
except ImportError:
    print("Module wetter.meineApp.views not found. Please check the module path.")
    sys.exit(1)

print("Import erfolgreich!")





def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    assert add(-1, 1) == 0

def test_add_zero():
    assert add(0, 5) == 5
    assert add(0, 0) == 0
