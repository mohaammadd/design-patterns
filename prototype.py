"""
Prototype Design Pattern 

The Prototype pattern is a creational design pattern that allows you to create new objects 
by cloning existing instances rather than creating new ones from scratch. This is particularly 
useful when object creation is expensive or complex.

Pattern Structure:
┌─────────────────────┐      ┌─────────────────────────────────┐
│  Prototype interface│◄─────┤  Client (can produce copy of   │
│                     │      │         any object)            │
│  clone(): Prototype │      │                                 │
└─────────────────────┘      │  copyObj = existing.clone()    │
          ▲        ▲         └─────────────────────────────────┘
          │        │                        
          │        │                        
┌─────────────────┐   ┌─────────────────┐
│ Prototype       │   │ Prototype       │
│ Subclass1       │   │ Subclass2       │
├─────────────────┤   ├─────────────────┤
│ - element1      │   │ - element2      │
├─────────────────┤   ├─────────────────┤
│ + SubClass1()   │   │ + SubClass2()   │
│ + clone():      │   │ + clone():      │
│   Prototype     │   │   Prototype     │
└─────────────────┘   └─────────────────┘

Key Benefits:
- Reduces the cost of creating objects when instantiation is expensive
- Allows dynamic object creation at runtime
- Eliminates the need for parallel class hierarchies of factories
- Provides an alternative to inheritance for object creation

Python's Copy Module:
Python provides built-in support for the Prototype pattern through the 'copy' module:

1. Shallow Copy (copy.copy()):
   - Creates a new object but inserts references to objects found in the original
   - Changes to mutable objects within the copy affect the original

2. Deep Copy (copy.deepcopy()):
   - Creates a new object and recursively copies all nested objects
   - Completely independent copy - changes don't affect the original

Implementation Notes:
- Use shallow copy when you want to share references to nested objects
- Use deep copy when you need complete independence between objects
- Consider implementing a custom clone() method for more control over the copying process
- Be aware of circular references when using deep copy

Example Use Cases:
- Game objects with similar properties but different states
- Configuration objects that vary slightly between environments
- Complex objects with expensive initialization that need variations
"""

import copy
import numpy as np


class Prototype:
    def __init__(self):
        self._objects = {}
        
    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(attrs)
        return cloned_obj


def client_prototype(name, obj, **attrs):
    prototype = Prototype()
    prototype.register_object(name, obj)
    return prototype.clone(name, **attrs)


class DataMatrix:
    """Simple matrix class for NumPy array demonstration."""
    
    def __init__(self, name, data, metadata=None):
        self.name = name
        self.data = data
        self.metadata = metadata or {}
    
    def __repr__(self):
        return f"DataMatrix('{self.name}', shape={self.data.shape}, metadata={self.metadata})"


# Simple demonstration
if __name__ == "__main__":
    print("=== Prototype Pattern with NumPy Arrays ===\n")
    
    # Create prototype registry
    registry = Prototype()
    
    # Create and register a prototype
    original_data = np.array([[1, 2, 3], [4, 5, 6]])
    prototype_matrix = DataMatrix("BaseMatrix", original_data, {"version": "1.0"})
    registry.register_object("base_matrix", prototype_matrix)
    
    print("Original prototype:")
    print(prototype_matrix)
    print("Data:\n", prototype_matrix.data)
    print()
    
    # Clone with modifications
    clone1 = registry.clone("base_matrix")
    clone1.name = "ExperimentA"
    clone1.metadata = {"version": "1.0", "experiment": "A"}
    
    clone2 = registry.clone("base_matrix")
    clone2.name = "ExperimentB"
    
    # Modify clones independently
    clone1.data[0, 0] = 999
    clone2.data[1, 1] = 777
    
    print("After modifications:")
    print("Original:", prototype_matrix)
    print("Data:\n", prototype_matrix.data)
    print()
    print("Clone 1:", clone1)
    print("Data:\n", clone1.data)
    print()
    print("Clone 2:", clone2) 
    print("Data:\n", clone2.data)
    print()
    
    # Verify independence
    print("Arrays are independent:")
    print(f"Original != Clone1: {id(prototype_matrix.data) != id(clone1.data)}")
    print(f"Clone1 != Clone2: {id(clone1.data) != id(clone2.data)}")