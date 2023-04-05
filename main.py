"""
This is going to be one giant Python3 file filled w/ code for review.
----------------------------------------------------------------------------
As a tech intern, ignorance is expected.
But, there is NO excuse for not knowing things that you should already know
  according to your resume.
"""
from __future__ import annotations
from typing import Any, Optional

# ------------------------------------- #
# 1) Concatenating Strings
# ------------------------------------- #
str1 = "Hi"
str2 = "my"
str3 = "name"
str4 = "is"
# BAD
print(str1 + ", " + str2 + " " + str3 + " " + str4 + " Slim Shady")
# GOOD
print(f"{str1}, {str2} {str3} {str4} Slim Shady")
print("{}, {} {} {} Slim Shady".format(str1, str2, str3, str4))

# ------------------------------------- #
# 2) Properly Handling Files
# ------------------------------------- #
filename = "my_file.txt"

# BAD --> Manually opening & closing files can cause unhandled exceptions.
f1 = open(filename, "w+")
for i in range(3):
    f1.write("Written by BAD practice\n")
f1.write("\n")
f1.close()

# good --> use the "with-as" keyword.
with open(filename, "a+") as f2:
    for i in range(3):
        f2.write("Appended by GOOD practice\n")
    f2.write("\n")


if __name__ == "__main__":
    import doctest
    doctest.testmod()   
