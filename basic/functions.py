# Sample: lambda arguments: expression It wont work for any iterables, but works for number of arguments.

# Squaring
square = lambda x: x**2
square_result = square(3) # Calling the lambda function with argument 3
# print(square_result)

# Sample: map(function, iterable) It applies the function to each item in the iterable and returns a map object. Can work for multiple iterables.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x: x**2, numbers)))
people = [
    {
        "name": "John",
        "age": 30
    },
    {
        "name": "Jane",
        "age": 25
    },
    {
        "name": "Doe",
        "age": 35
    }
]
# print(list(map(lambda person: person["name"], people)))

# filter(function, iterable) It filters the items in the iterable based on the function and returns a filter object. Can work with multiple conditions.
# print(list(filter(lambda x: x % 2 == 0, numbers)))
# print(list(filter(lambda x: x>5 and x%2==0, numbers)))
print(list(filter(lambda person: person["age"] > 25, people)))