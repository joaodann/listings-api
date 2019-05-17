global global_variable
global_variable = None

def create_cache(default_value=None):
    global global_variable
    global_variable = default_value

def use_cache():
    return global_variable