#!/bin/bash

setup_day() {
  local py_file="day$(printf "%02d" $1).py"
  local sample_file="day$(printf "%02d" $1)_sample.txt"

  if [ ! -f $py_file ]; then
    cat template.py | sed "s/CURRENT_DAY = 0/CURRENT_DAY = $1/" > $py_file
  else
    echo "File $py_file already exists"
  fi

  if [ ! -f $sample_file ]; then
    touch $sample_file
  else
    echo "File $sample_file already exists"
  fi
}

if [ $# -eq 0 ]; then
    for i in {1..25}; do
      setup_day $i
    done
else
  setup_day $1
fi
