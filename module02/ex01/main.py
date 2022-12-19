def what_are_the_vars(*args, **kwargs):
    """
    ...
    """
    ret = ObjectC()
    for key, value in kwargs.items():
        setattr(ret, key, value)
    for count, item in enumerate(args):
        if hasattr(ret, f"var_{count}"):
            return None
        setattr(ret, f"var_{count}", item)
    return ret


class ObjectC(object):

    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    print("*" * 25)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    print("*" * 25)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    print("*" * 25)
    obj = what_are_the_vars()
    doom_printer(obj)
    print("*" * 25)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    print("*" * 25)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    print("*" * 25)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)

    print("=" * 42)

    obj = what_are_the_vars(None)
    doom_printer(obj)

    print("*" * 25)

    obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
    doom_printer(obj)
    
    print("*" * 25)

    obj = what_are_the_vars(3, var_0=2)
    doom_printer(obj)

    
