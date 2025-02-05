#!/usr/bin/env python3
# Author: Denzel Gallardo
# Author ID: <Your Seneca ID>
# Date Created: yyyy/mm/dd

import sys  # Import sys to handle command-line arguments

# Check if an argument is provided, otherwise set timer to 3
if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

# While loop to count down
while timer != 0:
    print(timer)
    timer -= 1

# Print final message
print("blast off!")
