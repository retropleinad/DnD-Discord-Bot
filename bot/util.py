

def trim_args(args):
    output = {}
    for arg in args:
        condition = arg.strip().split("=")
        output[condition[0]] = condition[1]
    return output


def split_tuple(args, wedge):
    first_half = []
    second_half = []
    chop = False
    for arg in args:
        if arg == wedge:
            chop = True
        elif chop:
            second_half.append(arg)
        else:
            first_half.append(arg)
    return first_half, second_half