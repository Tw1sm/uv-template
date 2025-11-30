import typer
from {{cookiecutter.program_name}}.logger import init_logger, logger, console
from {{cookiecutter.program_name}} import __version__
from {{cookiecutter.program_name}}.commands import __all__

app = typer.Typer(
    add_completion=False,
    rich_markup_mode='rich',
    context_settings={'help_option_names': ['-h', '--help']},
    pretty_exceptions_show_locals=False,
    no_args_is_help=True
)

# Add subcommands
for command in __all__:
     app.add_typer(
        command.app,
        name=command.COMMAND_NAME,
        help=command.HELP
    )


@app.callback()
def main(
    debug: bool = typer.Option(False, '--debug', help='Enable [green]DEBUG[/] output'),
    version: bool = typer.Option(False, '--version', '-v', help='Show version and exit')
):
    """{{cookiecutter.program_name}} - A modular CLI application."""
    if version:
        console.print(f'{{cookiecutter.program_name}} version {__version__}')
        raise typer.Exit()

    init_logger(debug)


if __name__ == '__main__':
    app(prog_name='{{cookiecutter.program_name}}')
