from typing import Any, Optional, Callable, Union


# You can define your own types!
# ------------------------------
Vector = list[float]
def foo(v: Vector) -> Vector:
    return v


# Optional (Parameter) = You do NOT have to pass the "Optional" parameter,
#                        as long as there the default value is defined.
# Optional (return type) = Function will either return 'str' or 'None'
# ------------------------------------------------------------------------
def funct_1(my_str: str, button: Optional[bool]=True) -> Optional[str]:
    if button:
        return my_str
    else:
        return None

print(funct_1("hello world", False))


# Any = It's pretty self-explanatory.
# -----------------------------------
def funct_2(output: Optional[Any]=None) -> Optional[Any]:
    return output

def funct_3(output: Any) -> Any:
    return output

