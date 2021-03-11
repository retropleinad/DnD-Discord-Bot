

def trim_args(*args):
    output = {}
    for arg in args:
        condition = arg.strip().split("=")
        output[condition[0]] = condition[1]
    return output