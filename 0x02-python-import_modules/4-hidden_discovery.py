import marshal
import types

def print_hidden_names(module_file):
    with open(module_file, 'rb') as file:
        code = marshal.load(file)

    module = types.ModuleType("hidden_module")
    exec(code, module.__dict__)

    names = sorted(name for name in dir(module) if not name.startswith('__'))
    
    for name in names:
        print(name)

if __name__ == "__main__":
    module_file = "hidden_4.pyc"
    print_hidden_names(module_file)

