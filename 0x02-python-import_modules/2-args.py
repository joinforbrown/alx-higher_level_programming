#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_args, "s" if num_args > 1 else ""))
        for i in range(num_args):
            print("{}: {}".format(i + 1, argv[i]))


