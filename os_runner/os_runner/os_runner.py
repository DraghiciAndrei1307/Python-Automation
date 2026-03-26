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


    def change_mode(self, path='.', mode='0o644'):

        if not os.path.exists(path):
            return f"Error: Path {path} does not exist!"

        try:
            os.chmod(path, int(mode))
            return f"The {path} mode was changed to {mode}"
        except PermissionError:
            return f"Error: You need root/admin rights"
        except Exception as e:
            return f"Error: {e}"


    def create_text_file(self, name='hello.txt', mode = '0o644', path='.'):

        # Check if the path exists
        if not os.path.exists(path):
            return f"Error: Path {path} does not exist!"

        # Create a new file at the designated path

        try:
            file_path = os.path.join(path, name)

            with open(file_path, 'w') as f:
                pass

            # Change mode of the
            self.change_mode(file_path, mode)

            return f"Successfully created file: {file_path}"

        except PermissionError:
            return f"Error: You need root/admin rights"

        except Exception as e:
            print(f"Error: {e}")


    def create_folder(self, path='.', name="hello_folder", mode='0o644'):

        # Check if the path exists
        if not os.path.exists(path):
            return f"Error: Path {path} does not exist!"

        try:
            folder_path = os.path.join(path, name)

            os.mkdir(folder_path)

            # Change mode of the
            self.change_mode(folder_path, mode)

            return f"Successfully created file: {folder_path}"

        except PermissionError:
            return f"Error: You need root/admin rights"
        except Exception as e:
            return f"Error: {e}"


    def move(self):
        pass


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
