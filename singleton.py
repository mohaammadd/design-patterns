"""
Singleton pattern implementation in Python.

This module provides a simple implementation of the Singleton design pattern.
It ensures that a class has only one instance and provides a global point of access to it.

* Insure that the class can only be instantiated once.

* Provide easy access to the single instance.

*Control their instantiation and access.( for example hiding the constructor of a class)

###############################################################################

Usage:

Working in a shared class like a database connection, configuration settings, or logging service.

import collections as c1
import collections as c2

id(c1)  # Output: <class 'collections.abc'>
id(c2)  # Output: <class 'collections.abc'>

assert c1 is c2  # True, both refer to the same instance

###############################################################################

Implementation:

Singleton pattern ensure that only one instance of a class ever exist, and provide a global access to that instance.

Typically, this is done by:

1: Declaring all constructors of the class to be protected, which prevents instantiation from outside the class.
2: Providing a static method that returns the single instance of the class.
3: Using a class variable to hold the single instance.

"""
# Singleton pattern implementation in Python
# A simple implementation of the Singleton pattern using a class variable
# This implementation ensures that only one instance of the class can be created.
# It provides a global point of access to that instance.
# This is a common design pattern used in various applications, such as logging, configuration management, etc.
class A:
    _instance = None

    def __init__(self):
        raise RuntimeError("This class cannot be instantiated directly. Use the get_instance method.")
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)

        return cls._instance
    

one = A.get_instance()
two = A.get_instance()

print("ID of one:", id(one))
print("ID of two:", id(two))


# Using metaclass for Singleton patternb is another common approach.
# This allows for more control over class creation and can be cleaner in some cases.
# Example of Singleton using a metaclass
class Singleton(type):
    _instaance = None

    def __call__(self, *args, **kwargs):
        if not self._instaance:
            self._instaance = super().__call__(*args, **kwargs)
        return self._instaance
    


class B(metaclass=Singleton):
    pass

three = B()
four = B()

print("ID of three:", id(three))
print("ID of four:", id(four))