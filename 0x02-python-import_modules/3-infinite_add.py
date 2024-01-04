#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the command line arguments excluding the script name
    arguments = sys.argv[1:]

    # Convert each argument to an integer and sum them up
    result = sum(int(arg) for arg in arguments)

    # Print the result followed by a new line
    print(result)

