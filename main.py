"""
This is going to be one giant Python3 file filled w/ code for review.
----------------------------------------------------------------------------
As a tech intern, ignorance is expected.
But, there is NO excuse for not knowing things that you should already know
  according to your resume.
"""
from __future__ import annotations
from typing import Any, Optional

# -------------------------- #
# 1) Concatenating Strings
# -------------------------- #

str1 = "Hi"
str2 = "my"
str3 = "name"
str4 = "is"
# BAD
print(str1 + ", " + str2 + " " + str3 + " " + str4 + " Slim Shady")
# GOOD
print(f"{str1}, {str2} {str3} {str4} Slim Shady")
print("{}, {} {} {} Slim Shady".format(str1, str2, str3, str4))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
