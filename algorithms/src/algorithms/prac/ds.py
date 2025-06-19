"""Review Python data structure operations:
Lists: append() , pop() , insert() , remove() , slicing [:] , extend()
Strings: split() , join() , strip() , find() , replace() , startswith() , endswith()
Sets: add() , remove() , discard() , union() , intersection() , difference()
Dicts: get() , setdefault() , pop() , keys() , values() , items()
Practice VSCode shortcuts: Ctrl+D (select word), Ctrl+/ (comment), Ctrl+Shift+P (command
palette)"""


# Python Data Structures Practice Exercises
# Fill in the blanks and run each section to check your work

print("=== LISTS PRACTICE ===")
# 1. Create a list and practice basic operations
fruits = ["apple", "banana"]
# Add "orange" to the end
# TODO: fruits.___("orange")
fruits.append("orange")
# Add "grape" at position 1
# TODO: fruits.___(1, "grape")
fruits.insert(1, "grape")
# Remove "banana"
# TODO: fruits.___("banana")
fruits.remove("banana")
# Get the last 2 items using slicing
# TODO: last_two = fruits[___]
last_two = fruits[-2:]
print("Fruits:", fruits)
print("Last two:", last_two)
print()

print("=== STRINGS PRACTICE ===")
text = "  Hello, World! How are you?  "
# Remove whitespace from both ends
# TODO: clean_text = text.___()
clean_text =text.strip()
# Split into words
# TODO: words = clean_text.___(", ")
words = clean_text.split(" ")
# Join words with " | "
# TODO: joined = " | ".___(___)
joined = " | ".join(words)
# Check if it starts with "Hello"
# TODO: starts_hello = clean_text.___(_____)
starts_hello = clean_text.startswith('hello')
print("Clean text:", clean_text)
print("Words:", words)
print("Joined:", joined)
print("Starts with Hello:", starts_hello)
print()

print("=== SETS PRACTICE ===")
set1 = {1,2,3,4}
set2 = {4,5,6,7}

# Add 7 to set1
# TODO: set1.___(7)
set1.add(7)
# Find common elements
# TODO: common = set1.___(set2)
common = set1.intersection(set2)
# Find elements only in set1
# TODO: only_set1 = set1.___(set2)
only_set1 = set1.difference(set2)
# Remove 2 from set1 (use the safe method)
# TODO: set1.___(2)
set1.remove(2)
print("Set1:", set1)
print("Common:", common)
print("Only in set1:", only_set1)
print()

print("=== DICTIONARIES PRACTICE ===")
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Get Alice's score with default 0 if not found
# TODO: alice_score = scores.___(_____, _____)
alice_score = scores.get("Alice", 0)
# Add or update David's score to 88
# TODO: scores[_____] = _____
scores["David"] = 88
# Get all names (keys)
# TODO: names = list(scores.___())
names = list(scores.keys())
# Get all score values
# TODO: all_scores = list(scores.___())
all_scores = list(scores.values())
# Get key-value pairs
# TODO: pairs = list(scores.___())
pairs = list(scores.items())

print("Alice's score:", alice_score)
print("Names:", names)
print("All scores:", all_scores)
print("Pairs:", pairs)
print()

print("=== COLLECTIONS.COUNTER PRACTICE ===")
from collections import Counter

text = "hello world"
# Count character frequency
# TODO: char_count = Counter(____)
char_count=Counter(text)

# Get the 2 most common characters
# TODO: most_common_2 = char_count.___(2)
most_common_2 = char_count.most_common(2)

# Count of 'l'
# TODO: l_count = char_count[____]
l_count = char_count.get('l')

print("Character counts:", char_count)
print("Most common 2:", most_common_2)
print("Count of 'l':", l_count)
print()

print("=== INPUT PARSING PRACTICE ===")
# Simulate reading input (normally you'd use input())
sample_input = "5 10 15 20"
print("Sample input:", sample_input)

# Parse into list of integers
# TODO: numbers = list(map(int, sample_input.___()))
numbers = list(map(int, sample_input.split()))

# Find the sum
# TODO: total = sum(____)
total = sum(numbers)

print("Parsed numbers:", numbers)
print("Sum:", total)

l=[1,2,3,4,5]
l.append(6)
l.remove(5)
l.insert(1, 2)