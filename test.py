from os_runner.os_runner import OsRunner


if __name__ == '__main__':
    my_os_runner = OsRunner()
    my_os_runner.list_entries_in_path()
    my_os_runner.change_current_directory('/')
    my_os_runner.list_entries_in_path()
