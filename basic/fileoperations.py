from pathlib import Path

file_path = Path(__file__).resolve().parent / "example.txt"
# with file_path.open("r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# with file_path.open('a') as file:
#     file.write("\nThis is an appended line.")

# new_file_path = Path(__file__).resolve().parent / "newfile.txt"
# with new_file_path.open("w", encoding="utf-8") as file:
#     lines = ["This is the first line.", "This is the second line.", "This is the third line."]
#     file.writelines(lines)

with file_path.open("r", encoding="utf-8") as file:
    content = file.read()
    number_of_lines = content.count('.') + 1 if content else 0
    number_of_words = len(content.split())
    number_of_characters = len(content)
    print(f"Number of lines: {number_of_lines}")
    print(f"Number of words: {number_of_words}")
    print(f"Number of characters: {number_of_characters}")
