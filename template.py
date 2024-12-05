from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Set, Tuple
from position import Position, Direction
import re
import glob
import os

CURRENT_DAY = 0


def part1(content: str) -> str:
    return 'Not implemented'


def part2(content: str) -> str:
    return 'Not implemented'


def process_input_file(day: int, input_file: str):
    with open(input_file) as f:
        content = f.read()
        print(f'Day {day}, file {input_file}')
        print('Part 1: ' + part1(content))
        print('Part 2: ' + part2(content))


def maybe_move_input_txt(day: int):
    directory = os.path.dirname(__file__)
    generic_input_txt = os.path.join(directory, 'input.txt')
    specific_input_txt = os.path.join(directory, f'day{day:02d}_input.txt')
    if os.path.exists(generic_input_txt) and not os.path.exists(specific_input_txt):
        os.rename(generic_input_txt, specific_input_txt)


def get_candidate_files() -> List[str]:
    base = __file__[:-3]
    pattern = base + '*.txt'
    directory = os.path.dirname(__file__)
    return glob.glob(pattern) + glob.glob(os.path.join(directory, 'input.txt'))


def main():
    maybe_move_input_txt(CURRENT_DAY)
    candidate_files = get_candidate_files()
    if not candidate_files:
        print(f'No input files found for day {CURRENT_DAY}')

    for candidate_file in candidate_files:
        process_input_file(CURRENT_DAY, candidate_file)


if __name__ == '__main__':
    if __file__.endswith('template.py'):
        print('The template.py file is not intended to be executed directly.'
              ' Please run setup.sh to create per-day copies')
        exit(1)
    main()
