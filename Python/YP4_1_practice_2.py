def print_max(a: int, b: int) -> None:
    """
    Prints max value of a and b
    NOTE: prints equals if a = b.
    """
    if a > b:
        print(a, "is max")
    elif a == b:
        print(a, "equals to", b)
    else:
        print(b, "is max")
