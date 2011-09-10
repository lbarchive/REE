#!/bin/bash

# Ensure we put back what we have changed
trap 'echo -e "\e[?25h" ; stty echo ; exit 0' INT QUIT TERM EXIT

# Setting eyes
REE=">v<^"

## Initializing variables
# x position
x=1
# rolling direction
d=1

# Initializing terminal
echo -ne "\e[?25l"
stty -echo

# Main loop
while sleep 0.25; do
  r="${REE::1}"
  # Clear line and show REE
  echo -ne "\e[2K\e[${x}G${r}_${r}"
  # Sort of re-queuing
  REE="${REE:1}${r}"
  # Change x
  let x+=d
  # If on edge, change direction
  let cols_2="$(tput cols) - 2"
  if (( x <= 1 )) || (( x >= cols_2 )); then
    let d*=-1
    (( x > 1 )) && x="$cols_2"
  fi
done
