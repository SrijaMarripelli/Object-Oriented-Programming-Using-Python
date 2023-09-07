# Python Object Oriented Programming 
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)    # TODO : "The "frozen" parameter makes the class immutable"
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1)

# TODO : Attempting to change the value of an immutable class throws an exception
# obj.value1 = "Another Value"
# print(obj.value1)

# TODO : Even functions within the class can't change anything
obj.somefunc(20)
