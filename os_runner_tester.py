import pytest
from os_runner.os_runner import OsRunner

class TestOsRunner:

    def setup_method(self):
        """
        Setup method to run before each test
        :return:
        """

        self.runner = OsRunner()

    def test_path_not_exist(self):
        """
        Test path not exist
        :return:
        """

        result = self.runner.list_entries_in_path("fake_path")
        assert "Error"  in result

    def test_path_exist(self):
        """
        Test path exist
        :return:
        """

        result = self.runner.list_entries_in_path(".")
        assert "Error" not in result

    def test_list_entry_current_dir(self, entry = "setup.py"):
        """
        Test list entries current directory
        :return:
        """

        result = self.runner.list_entries_in_path()

        # check to see if the result is a list
        assert isinstance(result, list)

        # check if the list is no empty
        assert len(result) > 0

        # check for a specific element
        assert entry in result

    def test_create_file(self, name = "hello_world.txt"):

        result = self.runner.create_text_file(name = name)

        assert "Success" in result

    def test_create_file_rights_missing(self, name = "hello_world.txt", path = "/"):

        result = self.runner.create_text_file(name = name, path = path)
        assert "Error" in result

    def test_create_folder(self, name = "hello_world"):

        result = self.runner.create_folder(name = name)
        assert "Success" in result

    def test_create_folder_rights_missing(self, name = "hello_world", path = "/"):
        result = self.runner.create_folder(name = name, path = path)
        assert "Error" in result