"""Command2 module for {{cookiecutter.program_name}}."""
import typer
from {{cookiecutter.program_name}}.logger import logger

app = typer.Typer()
COMMAND_NAME = "command2"
HELP = "Command2 help"


@app.callback(invoke_without_command=True, no_args_is_help=True)
def main(
    ctx: typer.Context,
    param: str = typer.Option(..., '--param', help='Param name')):
    
   logger.info("Command2")
