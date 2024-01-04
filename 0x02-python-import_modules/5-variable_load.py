#!/usr/bin/python3
import importlib

if __name__ == "__main__":
    variable_module = importlib.import_module("variable_load_5")
    print(variable_module.a)

