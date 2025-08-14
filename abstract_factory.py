"""
Abstract Factory Pattern Implementation

The Abstract Factory pattern provides an interface for creating families of related 
or dependent objects without specifying their concrete classes. It's useful when:
- You need to create multiple related products that should work together
- You want to ensure consistency among products from the same family
- You need to support multiple product lines or platforms

Pattern Structure Components:

1. **Abstract Factory (GUIFactory)**: 
   - Declares abstract methods for creating each type of product
   - Defines the interface that all concrete factories must implement
   - Ensures all factories can create the same set of product types

2. **Concrete Factories (WindowsFactory, MacOSFactory)**: 
   - Implement the abstract factory interface
   - Each factory creates a complete family of related products
   - Guarantee that products from the same family are compatible
   - Encapsulate the knowledge of which concrete products to instantiate

3. **Abstract Products (Button, Checkbox)**: 
   - Define interfaces for different types of products
   - Declare common methods that all variants must implement
   - Allow client code to work with products without knowing concrete types

4. **Concrete Products (WindowsButton, MacOSButton, etc.)**: 
   - Implement the abstract product interfaces
   - Provide platform-specific or variant-specific behavior
   - Products from the same family (e.g., all Windows products) work together

5. **Client (Application)**: 
   - Uses only abstract factory and product interfaces
   - Remains decoupled from concrete implementations
   - Can work with any product family through the same interface

UML Class Diagram:
┌──────────────────────┐                                  ┌─────────────┐
│    AbstractFactory   │◄─────────────────────────────────┤   Client    │
│  (GUIFactory)        │                                  │(Application)│
│ +create_button()     │                                  └─────────────┘
│ +create_checkbox()   │                                         │
└──────────┬───────────┘                                         │
           △                                                     │
           │                                                     │
     ┌─────┴─────┐                                               │
     │           │                                               │
┌────▼────┐ ┌────▼────┐                                          │
│Concrete │ │Concrete │                                          │
│Factory1 │ │Factory2 │                                          │
│(Windows │ │(MacOS   │                                          │
│Factory) │ │Factory) │                                          │
│+create_ │ │+create_ │                                          │
│button() │ │button() │                                          │
│+create_ │ │+create_ │                                          │
│checkbox()│ │checkbox()│                                         │
└────┬────┘ └────┬────┘                                          │
     │           │                                               │
     │           │     ┌─────────────────────┐                   │
     │           │     │  AbstractProductA   │◄──────────────────┘
     │           │     │    (Button)         │
     │           │     │ +render()           │
     │           │     └──────────┬──────────┘
     │           │                △
     │           │                │
     │           │          ┌─────┴─────┐
     │           │          │           │
     │           │     ┌────▼────┐ ┌────▼────┐
     │           └────►│ProductA1│ │ProductA2│
     │                 │(Windows │ │(MacOS   │
     │                 │Button)  │ │Button)  │
     │                 │+render()│ │+render()│
     │                 └─────────┘ └─────────┘
     │
     │                 ┌─────────────────────┐
     │                 │  AbstractProductB   │◄──────────────────┐
     │                 │   (Checkbox)        │                   │
     │                 │ +render()           │                   │
     │                 └──────────┬──────────┘                   │
     │                            △                              │
     │                            │                              │
     │                      ┌─────┴─────┐                        │
     │                      │           │                        │
     │                 ┌────▼────┐ ┌────▼────┐                   │
     └────────────────►│ProductB1│ │ProductB2│◄──────────────────┘
                       │(Windows │ │(MacOS   │
                       │Checkbox)│ │Checkbox)│
                       │+render()│ │+render()│
                       └─────────┘ └─────────┘

Relationships Explained:
◄── USES: Client uses AbstractFactory interface to create products
△   IMPLEMENTS: Concrete classes implement abstract interfaces  
──► CREATES: Factories instantiate and return concrete products

Pattern Flow:
1. Client receives an AbstractFactory instance (dependency injection)
2. Client calls factory methods (create_button(), create_checkbox())
3. Factory returns concrete products that belong to the same family
4. Client uses products through their abstract interfaces
5. All products from same factory work together consistently

Key Benefits in This Implementation:
- Consistency: All Windows components look/behave like Windows UI
- Flexibility: Easy to add new platforms (Linux, Web, Mobile)
- Testability: Can inject mock factories for unit testing
- Maintainability: Changes to one platform don't affect others

Example Use Case:
This implementation demonstrates creating UI components (buttons, checkboxes) for
different operating systems (Windows, MacOS). Each factory ensures that all 
components follow the same visual style and behavior for their platform.

Benefits:
- Consistency: Products from the same family work well together
- Flexibility: Easy to add new product families
- Isolation: Client code is decoupled from concrete classes
- Single Responsibility: Each factory handles one product family

Trade-offs:
- Can be complex for simple use cases
- Adding new product types requires changing all factory interfaces
- More classes and interfaces to maintain


"""
from abc import ABC, abstractmethod

# Abstract products
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Concrete products - Windoes Style
class WindosButton(Button):
    def render(self) ->str:
        return "Rendering Windows-style button"
    
class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering Windows-style checkbox"
# Concrete products - MacOS Style
class MacOSButton(Button):
    def render(self) -> str:
        return "Rendering MacOS-style button"
    
class MackOSCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering MacOS-style checkbox"
    
# Abstract factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindosButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MackOSCheckbox()
    
# Client code
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory


    def create_ui(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()

        print(button.render())
        print(checkbox.render())
        return button, checkbox
    
# Factory selection function

def get_factory(platform: str) -> GUIFactory:
    """ Factory selection based on platform."""
    factories = {
        "windows": WindowsFactory(),
        "macos": MacOSFactory()
    }
    factory = factories.get(platform.lower())
    if not factory:
        raise ValueError(f"Unsupported platform: {platform}")
    return factory

# Example usage
if __name__ == "__main__":
    print("=== Abstract Factory Pattern Demo ===\n")
    
    # Demonstrate Windows UI
    print("Creating Windows Application:")
    windows_factory = get_factory("windows")
    windows_app = Application(windows_factory)
    windows_app.create_ui()
    
    print("\n" + "-" * 40 + "\n")
    
    # Demonstrate MacOS UI
    print("Creating MacOS Application:")
    macos_factory = get_factory("macos")
    macos_app = Application(macos_factory)
    macos_app.create_ui()
    
    print("\n" + "-" * 40 + "\n")
    
    # Example with error handling
    try:
        print("Attempting to create Linux Application:")
        linux_factory = get_factory("linux")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== Dynamic Factory Selection ===")
    
    # Simulate runtime platform detection
    import platform as sys_platform
    
    # For demo purposes, we'll map actual system to our supported platforms
    system_name = sys_platform.system().lower()
    platform_map = {
        'windows': 'windows',
        'darwin': 'macos',  # macOS returns 'Darwin'
        'linux': 'windows'  # Default to windows for unsupported platforms
    }
    
    detected_platform = platform_map.get(system_name, 'windows')
    print(f"Detected platform: {sys_platform.system()} -> Using {detected_platform} factory")
    
    auto_factory = get_factory(detected_platform)
    auto_app = Application(auto_factory)
    auto_app.create_ui()