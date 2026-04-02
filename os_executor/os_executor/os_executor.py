import click

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
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.pass_context
def hello(ctx, count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

@cli.command()
@click.option('--name', prompt='Your name',
              help='The person to say goodbye to.')
@click.pass_context
def goodbye(ctx, name):
    """Simple command that says goodbye NAME."""
    click.echo(f"Goodbye {name}!")
