from os_runner.os_runner import OsRunner


if __name__ == '__main__':
    my_os_runner = OsRunner()
    print(f"Contents: {my_os_runner.list_entries_in_path()}")
    my_os_runner.change_current_directory('/')
    print(f"Contents: {my_os_runner.list_entries_in_path()}")
    my_os_runner.change_current_directory(my_os_runner.home)
    print(f"Contents: {my_os_runner.list_entries_in_path()}")
    print(f"Run command: {my_os_runner.run_cmd(['ls', '-ltr'])}")
    print(my_os_runner.create_text_file())
