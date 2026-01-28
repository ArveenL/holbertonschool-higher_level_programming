classes

Python - Classes & Objects 
a class creates a new type, and objects are instances of that type.

class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name   until def _init_(self, new_name=None)  my understanding: we have a custom type(class) called user it has 2 public class variables called id and name and 1 private class variable called _password   we're also defining and initialising(def _init_) a linker to class objects called self, and we're associating the following parameter : new_name = None   as such new_name can be used by class objects later on


Python Classes & Objects Cheat Sheet
Class
* A custom data type or blueprint for objects.
* Defined with class ClassName:.
* Example: class User: ...
Object / Instance
* A concrete thing created from a class.
* instance = ClassName()
* Instance and object are the same thing.
* Example: u = User()
self
* Keyword in all class methods referring to the specific object being used or created.
* First parameter in every method (by convention called self).
* Not special — could technically be another name, but self is standard.
init method
* Special method run automatically when an object is created.
* Used to initialize instance variables.
* Example: def __init__(self, name): self.name = name
Regular Method
* Functions defined inside a class that can be called on objects.
* Example:

def drive(self): print("Driving")
Class Variables
* Shared by all objects of the class.
* Defined directly under the class, outside __init__.
* Example:

id = 89   # accessible via User.id or u.id
Instance (Object) Variables / Attributes
* Unique to each object.
* Defined inside __init__ using self.
* Example:

self.is_new = True
self.name = new_name
Public vs Private Variables
* Public: Name has no leading underscore → accessible outside class.
* Private: Name starts with __ → name-mangled to prevent direct access.
* Example:

__password = None  # private class variable
How arguments work in init
* First parameter → self (object being created).
* Subsequent parameters → values you pass during object creation.
* Example:

u = User("John")   # Internally: User.__init__(u, "John")
Accessing Variables
* Class variable: accessible by any object → u.id or User.id.
* Instance variable: accessible only by that object → u.is_new.
Example: Putting it together

class User:
    id = 89                 # class variable
    __password = None       # private class variable

    def __init__(self, new_name=None):
        self.is_new = True  # instance variable
        if new_name:
            self.name = new_name  # instance variable

u = User("John")
print(u.name)    # "John" → instance variable overrides class variable
print(u.id)      # 89 → class variable shared by all
print(u.is_new)  # True → instance variable unique to u
Key Notes
* self links methods and instance variables to the specific object.
* __init__ initializes the object; regular methods do stuff anytime.
* Class variables → shared; instance variables → unique per object.
* Instance variables exist only after the object is created.

