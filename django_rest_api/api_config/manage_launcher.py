import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django is not installed") from exc

    # no args: the server will start on 0.0.0.0:8000
    args = sys.argv
    if len(args) == 1:
        args.append('runserver')
        args.append('0.0.0.0:8000')

    execute_from_command_line(args)