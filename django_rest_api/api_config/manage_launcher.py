import os
import sys
import argparse
import django

def setup_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_config.settings')
    django.setup()

def main():

    setup_django()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django is not installed") from exc

    # no args: the server will start on 0.0.0.0:9001
    args = sys.argv
    if len(args) == 1:
        args.append('runserver')
        args.append('0.0.0.0:9001')

    execute_from_command_line(args)

def create_superuser():

    setup_django()

    try:
        from django.contrib.auth import get_user_model
    except ImportError as exc:
        raise ImportError("Django is not installed") from exc

    User = get_user_model()

    parser = argparse.ArgumentParser(description='Create Django superuser')
    parser.add_argument('-u', '--username', required=True, help='Username', default=os.environ.get('DJANGO_SUPERUSER_NAME', 'admin'))
    parser.add_argument('-e', '--email', required=True, help='Email', default=os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com'))
    parser.add_argument('-p', '--password', required=True, help='Password', defualt=os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'password123'))

    args = parser.parse_args()

    if not User.objects.filter(username=args.username).exists():
        User.objects.create_superuser(args.username, args.email, args.password)
        print(f"Superuser {args.username} was created.")
    else:
        print(f"Your superuser already exists.")

def create_user():

    setup_django()

    try:
        from django.contrib.auth import get_user_model
    except ImportError as exc:
        raise ImportError("Django is not installed") from exc

    User = get_user_model()

    parser = argparse.ArgumentParser(description='Create Django superuser')
    parser.add_argument('-u', '--username', required=True, help='Username', default='neo')
    parser.add_argument('-e', '--email', required=True, help='Email', default='neo@example.com')
    parser.add_argument('-p', '--password', required=True, help='Password', defualt='password123')

    args = parser.parse_args()

    if not User.objects.filter(username=args.username).exists():
        User.objects.create_user(args.username, args.email, args.password)
        print(f"User {args.username} was created.")
    else:
        print(f"User already exists.")
