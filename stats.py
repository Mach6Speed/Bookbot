# This module contains functions for calculating statistics about text.

# counts the number of words in the text
def count_words(text):
    return len(text.split())

# counts the occurrences of each character in the text
def count_each_character(text):
    character_counts = {}
    for char in text:
        if char.lower() in character_counts:
            character_counts[char.lower()] += 1
        else:
            character_counts[char.lower()] = 1
    return character_counts


# sorts the character counts in descending order and returns a list of dictionaries with 'char' and 'num' keys
def sort_on(item):
    return item["num"]

def sort_character_counts(character_counts):
    list_to_sort = []
    for char in character_counts:
        list_to_sort.append({"char" : char, "num" : character_counts[char]})
    list_to_sort.sort(reverse=True, key=sort_on)
    return list_to_sort

# calculates the total number of characters by summing the counts in the dictionary argument
def total_characters(character_counts):
    return sum(character_counts.values())


