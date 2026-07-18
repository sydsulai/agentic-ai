from pathlib import Path

my_list = [1,2,3,4,5,6]
iterator = iter(my_list)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

### Generators

def my_generator(n):
    for i in range(n):
        yield i**2

gen = my_generator(5)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break

### Practical : Reading Large Files with Generators

file_path = Path(__file__).resolve().parent / "example.txt"
def read_large_file(file_path):
    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()

gen = read_large_file(file_path)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break