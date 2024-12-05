# aoc-py-template
A template for working on adventofcode.com (AOC) puzzles.

If you are attempting to compete on public or private leaderboards, it's important to minimize time wasted on boilerplate code. This project aims to make it easier to focus on solving the problem.

## Usage
To prepare for a new puzzle, run the setup script to create a per-day copy of the template.py file and create empty sample files. You can either specify the day as an input parameter, or leave it empty to generate all days 1..25.
```
$> ./setup.sh 2
- generates day02.py and day02_sample.txt
$> ./setup.sh
- generate dayNN.py and dayNN_sample.txt files for all values 01..25
```

When running dayNN.py, it looks for an input.txt file in the current directory. If one exists, it'll be renamed to dayNN_input.txt (unless one already exists in the directory). Then it will read all txt files in the current directory that start with dayNN, as well as input.txt. It'll then execute part1 and part2 functions for the contents of each.

The intended workflow for a new day is as follows:
1. ./setup.sh NN
2. Download the input.txt file from AOC
3. Copy any samples from AOC into the dayNN_sample.txt file
4. Implement the part1 function in dayNN.py
5. Once part1 is done, implement part2

## Files

### template.py

This file contains a reasonable starting point for working on a new puzzle. It contains commonly needed imports, and scaffolding for running your code against input files.

### setup.sh

Running setup.sh {day number} creates a new copy of the template.py file for that day, and creates a blank sample file.

### position.py

This file contains some classes for working with positional data. Often the puzzles in AOC involve for example grid data, and it's often necessary to track the position and neighbors of various cells.
