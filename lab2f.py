#!/usr/bin/env python3
# Author: Denzel Gallardo
# Author ID: dgallardo3 - 104167234
# Date Created: 2025-02-04

import sys  # Import sys to handle command-line arguments

# Assign the first command-line argument as the timer value
timer = int(sys.argv[1])

# While loop to count down
while timer != 0:
    print(timer)
    timer -= 1

# Print final message
print("blast off!")
