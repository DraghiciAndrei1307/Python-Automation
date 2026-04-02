import click

from os_runner import OsRunner

def setup_os_runner():
    return OsRunner()

@click.group()
@click.pass_context
def cli(ctx):
    """
    This is a group command. We create a group for the future commands
    that we will implement in the future. In this command, we can load
     configuration files.
    :param ctx:
    :return:
    """
    ctx.ensure_object(dict)

@cli.command()
@click.option('--count',
              default=1,
              help='Number of greetings.'
              )
@click.option('--name',
              prompt='Your name',
              help='The person to greet.'
              )
@click.pass_context
def hello(ctx, count, name):
    """
    Simple program that greets NAME for a total of COUNT times.
    """
    for x in range(count):
        click.echo(f"Hello {name}!")

@cli.command()
@click.option('--name',
              prompt='Your name',
              help='The person to say goodbye to.'
              )
@click.pass_context
def goodbye(ctx, name):
    """Simple command that says goodbye NAME."""
    click.echo(f"Goodbye {name}!")

@cli.command()
@click.option(
    '--path',
    prompt='Enter a path',
    help='The path you want to list the entries for.'
)
@click.pass_context
def list_entries(ctx, path):
    os_runner = setup_os_runner()
    print(os_runner.list_entries_in_path(path))

@cli.command()
@click.option(
    '--path',
    prompt='Enter a path',
    help='The path you want to go to.'
)
@click.pass_context
def change_current_directory(ctx, path):
    os_runner = setup_os_runner()
    print(os_runner.change_current_directory(path))

@cli.command()
@click.option(
    '--name',
    prompt='How should the file be named?',
    help='The name of the file you want to create.'
)
@click.option(
    '--path',
    prompt='Enter a path',
    help='The path where you want to create the new file.'
)
@click.option(
    '--mode',
    prompt='Configure the mode of the file.',
    help='The mode of the file. Use digits to configure the mode (e.g. 0644).'
)
@click.pass_context
def create_text_file(ctx, name, path, mode):
    os_runner = setup_os_runner()
    print(os_runner.create_text_file(name, path, mode))

@cli.command()
@click.option(
    '--path',
    prompt='Enter a path',
    help='The path you want to change the mode for.'
)
@click.option(
    '--mode',
    prompt='Mode',
    help='The mode you want to change to.'
)
@click.pass_context
def change_mode(ctx, path, mode):
    os_runner = setup_os_runner()
    print(os_runner.change_mode(path, mode))

@cli.command()
@click.option(
    '--path',
    prompt='Enter a path',
    help='The path you want to create the new folder.'
)
@click.option(
    '--name',
    prompt='How should the folder be named?',
    help='The name of the folder you want to create.'
)
@click.option(
    '--mode',
    prompt='Mode',
    help='The mode you want to change to. '
         'Use digits to configure the mode (e.g. 0644).'
)
@click.pass_context
def create_folder(ctx, path, name, mode):
    os_runner = setup_os_runner()
    print(os_runner.create_folder(path, name, mode))

@cli.command()
@click.option(
    '--src',
    prompt='Enter a source path',
    help='The source path you want to copy from.'
)
@click.option(
    '--dest',
    prompt='Enter a destination path',
    help='The destination path you want to copy to.'
)
@click.pass_context
def move(ctx, src, dest):
    os_runner = setup_os_runner()
    print(os_runner.move(src, dest))

@cli.command()
@click.option(
    '--command',
    prompt='Enter a command',
    help='The command you want to execute.'
)
@click.pass_context
def run_cmd(ctx, command):
    os_runner = setup_os_runner()
    print(os_runner.run_cmd(command))
