# ABC: Abstract Base Class. @abstractmethod introduces formal, compile-time-like safety. It guarantees that any concrete subclass must implement that specific method, allowing you to reliably treat different objects
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

car = Car()
car.start_engine()  # Output: Car engine started.