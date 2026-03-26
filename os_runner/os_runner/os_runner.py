import os
import subprocess
from pathlib import Path

class OsRunner:

    def __init__(self):

        self.home = Path.home()



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


    def change_file_mode(self, path='.', name='hello.txt' , mode='0o644'):

        if not os.path.exists(path):
            return f"Error: Path {path} does not exist!"

        file_path = os.path.join(path, name)

        try:
            os.chmod(file_path, int(mode))
            return f"The {file_path} mode was changed to {mode}"
        except PermissionError:
            return f"Error: You need root/admin rights"
        except Exception as e:
            return f"Error: {e}"



    def create_text_file(self, name='hello.txt', mode = '0644', path='.'):

        # Check if the path exists
        if not os.path.exists(path):
            return f"Error: Path {path} does not exist!"

        # Before creating, list the current entries
        dir_list = self.list_entries_in_path(path)
        print("List of directories and files before creation:")
        print(dir_list)
        print()

        # Create a new file at the designated path
        file_path = os.path.join(path, name)
        with open(file_path, 'w') as f:
            pass

        # Change mode of the
        self.change_file_mode(path, name, mode)

        # After creating
        dir_list = self.list_entries_in_path(path)
        print("List of directories and files before creation:")
        print(dir_list)

        return None


    def run_cmd(self, command):
        """
        This method runs a command and returns the output.
        :param command:
        :return:
        """

        try:
            cmd = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            return cmd.returncode, cmd.stdout.decode()
        except Exception as e:
            print(f"Error: {e}")

        return None
