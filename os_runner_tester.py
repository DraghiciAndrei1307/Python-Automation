import os

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
        assert result["success"] == False

    def test_path_exist(self, path="."):
        """
        Test path exist
        :return:
        """
        result = self.runner.list_entries_in_path(path)

        assert result["success"] == True

    def test_list_entry_current_dir(self, entry="setup.py"):
        """
        Test list entries current directory
        :return:
        """

        result = self.runner.list_entries_in_path()

        assert result["success"] == True

        data = result["data"]

        # check to see if the result is a list
        assert isinstance(data, list)

        # check if the list is no empty
        assert len(data) > 0

        # check for a specific element
        assert entry in data

    def test_create_file(self, name="hello_world.txt"):
        result = self.runner.create_text_file(name=name)

        assert result["success"] == True
        assert result["exit_code"] == 0

    def test_create_file_rights_missing(
            self,
            name="hello_world.txt",
            path="/"
    ):
        result = self.runner.create_text_file(name=name, path=path)

        assert result["success"] == True
        assert self.test_path_exist(path=os.path.join(path, name))

    def test_create_folder(self, path=".", name="hello_world"):
        result = self.runner.create_folder(path=path, name=name)

        assert result["success"] == True
        assert self.test_path_exist(path=os.path.join(path, name))

    def test_create_folder_rights_missing(self, name="hello_world", path="/"):
        result = self.runner.create_folder(name=name, path=path)

        assert result["success"] == True
        assert self.test_path_exist(path=os.path.join(path, name))
