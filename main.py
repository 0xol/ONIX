def run_init_from_module(module_name):
    # open the module file
    try:
        with open(module_name + ".py") as f:
            module_code = f.read()
    except OSError:
        print("Could not open module file: {0}.py".format(module_name))
        return

    # execute the module code
    try:
        exec(module_code, globals(), locals())
    except:
        print("Could not execute module code for module: {0}".format(module_name))
        return

    # check if the module has an init() function
    if "init" in locals() and callable(locals()["init"]):
        # call the init() function
        locals()["init"]()
    else:
        print("Module {0} does not have an init() function.".format(module_name))

def main():
    run_init_from_module(input())