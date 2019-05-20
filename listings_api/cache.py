global global_variable
global_variable = None

global fileDone
fileDone = False


def create_cache(default_value=None):
    global global_variable
    global_variable = default_value
    global fileDone
    fileDone = True


def is_file_complete():
    return fileDone

def use_cache():
    return global_variable
