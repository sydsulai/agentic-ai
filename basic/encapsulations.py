class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.gender = "Male"
    
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    
class Employee(Person):
    
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self._employee_id = employee_id


if __name__ == "__main__":
    emp = Employee("John Doe", 30, "E12345")
    
    # Accessing public attribute
    print(f"Gender: {emp.gender}")
    print(f"Employee ID: {emp._employee_id}")  # Not recommended, but possible
    print(f"Name: {emp.get_name()}")