# Basic

## Functions

**lambda:** lambda(arguments, expression)
**map:** map(function, iterable1, iterable2) = Lazy Loading Technique(Stores in memory)
**filter:** filter(function, iterable)

## File

Modes:

- r = Read
- w = Write
- a = Append
- rb = ReadByte
- wb = WriteByte
- w+ = WriteAndRead

## OOPS

***PolyMorphism with ABC:***

- ABC: Abstract Base Class. @abstractmethod introduces formal, compile-time-like safety. It guarantees that any concrete subclass must implement that specific method, allowing you to reliably treat different objects

***Encapsulation:***

- Wrapping Data and methods in a single unit. Restricts access to some of the objects components, preventing accidental interference and missing of data.
- 3 Access Modifiers

  - Public
  - Private (__)
  - Protected (_)

***Abstraction:***

- Hiding the complex features of a class.
- ABC - AbstractBaseClass
- @abstractmethod - Gives a feature to child class to implement their own definition.

## Magic Methods - Double Underscore Functions - Dunder Functions

- Builtin functions
- Define the behaviour of an object
- You can override this builtin functions by defining your own definition.

## Iterators

- Uses LazyLoading technique. [Stores in Memory only accessible when we call using next(iterator)]
- Advanced Python Concept
- Efficing Looping and Memory Management
- Access elements of a collection sequentially without exposing the underlying structure.

## Generators

- Generates the next element of a sequence using lazy loading technique.
- Using yield keyword - They create it as iterator and can be retrieved using next
- Saves it in the local variable.

## function copy

## Clousres

- Functions inside a function
- Main functions messages are accessbile within the sub_functions as well.

## Decorators

- Modify the behavior or Add functionality of the function/class method without changing the code.