import os

class OsRunner:
    def __init__(self):
        pass


    def list_entries_in_path(self, path='.'):
        """
        This method lists all the entries in the given path.
        Omit the path, and it will list the contents of the
        current directory.
        :param path:
        :return:
        """
        if not os.path.exists(path):
            return f"Error: Path {path} does not exist!"

        return os.listdir(path)

    def change_current_directory(self, path='.'):

        """
        This method changes the current working directory.
        :param path:
        :return:
        """

        if not os.path.exists(path):
            return f"Error: Path {path} does not exist!"

        return os.chdir(path)

    def run_cmd(self, command):
        pass


