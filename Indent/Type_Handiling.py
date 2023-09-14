var: str = "Hello"
match var:
    case str():
        print(f"{var=} is a string")
    case int():
        print(f"{var=} is an integer")
    case float():
        print(f"{var=} is a float")
    case bool():
        print(f"{var=} is a bool")
    case None:
        print(f"{var=} is a none")
    case _:
        print(f"{var=} is an unknown type")
