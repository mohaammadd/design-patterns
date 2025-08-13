"""
Factory Method Design Pattern Example

This script demonstrates the Factory Method, a creational design pattern.
The pattern provides an interface for creating objects in a superclass, but
allows subclasses to alter the type of objects that will be created. This is
useful when the exact type of an object isn't known until runtime.

-----------------------------------------------------------------------
Visual Diagram of the Factory Method Pattern
-----------------------------------------------------------------------

  +-----------------+          creates          +----------------+
  |     Creator     |------------------------->|    Product     |
  |-----------------|                           |----------------|
  | - factory_method()|                           | - do_stuff()   |
  | - operation()   |                           +----------------+
  +--------^--------+                                    ^
           |                                             |
           | (implements)                                | (implements)
           |                                             |
  +-----------------+                           +----------------+
  | ConcreteCreator |                           | ConcreteProduct|
  |-----------------|                           |----------------|
  | - factory_method()|                           | - do_stuff()   |
  +-----------------+                           +----------------+

- The Client uses a `ConcreteCreator` to perform an `operation()`.
- The `operation()` in the base `Creator` calls the `factory_method()`.
- The `ConcreteCreator`'s `factory_method()` creates a `ConcreteProduct`.
- The `operation()` then uses this `ConcreteProduct`.

-----------------------------------------------------------------------

Pattern Components in this Code:
1.  Product: DataFormat (The interface for products)
2.  Concrete Products: JsonFormat, XmlFormat
3.  Creator: FileProcessor (Declares the factory method)
4.  Concrete Creators: JsonFileProcessor, XmlFileProcessor
5.  Client: The `client_code` function.
"""

from abc import ABC, abstractmethod

# --- 1. Product Interface ---
class DataFormat(ABC):
    """
    The Product interface declares the operations that all concrete products must
    implement. The client code will work with objects of this type.
    """
    @abstractmethod
    def process(self, file_name: str) -> str:
        """Processes the file and returns a status string."""
        pass

# --- 2. Concrete Products ---
class JsonFormat(DataFormat):
    """Concrete Product for handling JSON data."""
    def process(self, file_name: str) -> str:
        return f"Processing '{file_name}' using the JSON handler."

class XmlFormat(DataFormat):
    """Concrete Product for handling XML data."""
    def process(self, file_name: str) -> str:
        return f"Processing '{file_name}' using the XML handler."


# --- 3. Creator Class ---
class FileProcessor(ABC):
    """
    The Creator class declares the factory method `create_handler` that is
    meant to return an object of a Product class.
    """
    def __init__(self, file_name: str):
        self.file_name = file_name

    @abstractmethod
    def create_handler(self) -> DataFormat:
        """
        This is the factory method. Note that it returns a type of the abstract
        Product. Subclasses will override this to return a concrete product.
        """
        pass

    def run_processing(self) -> str:
        """
        The Creator's primary responsibility is not always creating objects.
        It usually contains some core business logic that relies on Product
        objects, returned by the factory method.
        """
        # Call the factory method to create a Product object.
        handler = self.create_handler()

        # Now, use the product.
        result = handler.process(self.file_name)
        return f"FileProcessor: Executed business logic. Result: ({result})"


# --- 4. Concrete Creators ---
class JsonFileProcessor(FileProcessor):
    """
    Concrete Creator for JSON files. Overrides the factory method to return
    a JsonFormat instance.
    """
    def create_handler(self) -> DataFormat:
        return JsonFormat()

class XmlFileProcessor(FileProcessor):
    """
    Concrete Creator for XML files. Overrides the factory method to return
    an XmlFormat instance.
    """
    def create_handler(self) -> DataFormat:
        return XmlFormat()


# --- 5. Client Code ---
def client_code(processor: FileProcessor):
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """
    print("Client: I'm not aware of the processor's concrete class, but it works.")
    print(processor.run_processing(), end="\n\n")


if __name__ == "__main__":
    print("App: Launched with the JsonFileProcessor.")
    client_code(JsonFileProcessor("document.json"))

    print("App: Launched with the XmlFileProcessor.")
    client_code(XmlFileProcessor("spreadsheet.xml"))
