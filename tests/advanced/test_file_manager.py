import pytest
import os
from projects.advanced.file_manager import FileManager

@pytest.fixture
def temp_file():
    filename = "test_file.txt"
    fm = FileManager(filename)

    yield fm
    if os.path.exists(filename):
        os.remove(filename)

def test_write_file(temp_file):
    assert temp_file.write_file("Hello, Pytest!") is True
    assert os.path.exists(temp_file.filename)

def test_read_file(temp_file):
    temp_file.write_file("Testing file read")
    content = temp_file.read_file()
    assert content == "Testing file read"

def test_read_nonexistent_file(temp_file):
    assert temp_file.read_file() is None

def test_delete_file(temp_file):
    temp_file.write_file("To be deleted")
    assert temp_file.delete_file() is True
    assert not os.path.exists(temp_file.filename)