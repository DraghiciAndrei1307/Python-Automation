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
@click.option('--path',
              prompt='Enter a path',
              help='The path you want to list the entries for.'
              )
@click.pass_context
def list_entries(ctx, path):
    os_runner = setup_os_runner()
    os_runner.list_entries_in_path(path)

