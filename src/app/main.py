from collections import Counter


string = input("Insert text tattoo: ")

characters = len(string)
string_without_spaces = len(string.replace(' ', ''))

char_count = Counter(string.upper())
print(f"Number of unique characters: {len(char_count)}")
print(f"Number of characters with spaces: {characters}")
print("Each symbol occurs:")
for char, count in char_count.items():
    print(f"'{char}': {count} once(s)")
