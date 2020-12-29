import os

import click

from advent_of_code_2020.day_1 import solution


@click.command()
@click.option(
    "--input-file",
    default="advent_of_code_2020/day_1/input.txt",
    help="Filename to read in for puzzle input",
)
def day1(input_file: str):
    assert os.path.isfile(input_file), f"File '{input_file}' not found."
    with open(input_file) as file:
        input = (int(line) for line in file.readlines())

    print(solution.solve(input))
