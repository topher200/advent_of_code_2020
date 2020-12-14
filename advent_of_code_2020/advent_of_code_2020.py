import click
from day_1 import solution


@click.command()
@click.option(
    "--input-file",
    default="day_1/input.txt",
    help="Filename to read in for puzzle input",
)
def day1(input_filename: str):
    with open(input_filename) as input_file:
        input = [int(line) for line in input_file.readlines()]

    solution.solve(input)
