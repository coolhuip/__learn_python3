from __future__ import annotations
        # The above import allows older Python versions to use updated features.
from typing import Any, Optional, Callable, Union

print("===================================")
print()


# You can define your own types!
# ------------------------------
Vector = list[float]
def foo(v: Vector) -> Vector:
    return v


# Optional (Parameter) = You do NOT have to pass the "Optional" parameter,
#                        as long as there the default value is defined.
# Optional (return type) = Function will either return 'str' or 'None'
# ------------------------------------------------------------------------
def bar(my_str: str, button: Optional[bool]=True) -> Optional[str]:
    if button:
        return my_str
    else:
        return None
    
print("DEMO: Optional type")
print(bar("hello world", False))
print(bar("hello world"))
print()


# Any = It's pretty self-explanatory.
# -----------------------------------
def funct_1(output: Optional[Any]=None) -> Optional[Any]:
    return output

def funct_2(output: Any) -> Any:
    return output


# Union = Define the possible types that can be passed.
# -----------------------------------------------------
def foo_2(x: Union[bool, int]) -> Union[list[str], str]:
    if isinstance(x, bool):
        return ["foo_2()", "has returned", "a", "list[str]", "type", "!"]
    elif isinstance(x, int):
        return "foo_2() has returned a 'str' type!"
    else:
        raise TypeError

print("DEMO: Union type")
print(foo_2(int()))
print(foo_2(bool()))
print()


# Callable = Use this type if your parameter is a callable function.
# ------------------------------------------------------------------
def add(x: int, y: list[int, str]) -> int:
    return x + y[0] + int(y[1])

def add_sum(a: int, b: Callable[[int, list[int, str]], int]):
    return a + b

print("DEMO: Callable type")
print("Result of add_sum(3, add(7, [10, '209'])) = "
            , add_sum(3, add(7, [10, "209"])))






print()
print("===================================")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
