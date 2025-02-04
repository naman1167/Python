# 1. Remove an item from a set if it is present
nums_set = set(map(int, input("Input numbers for the set (space-separated): ").split()))
val_to_remove = int(input("Enter a number to remove from the set: "))
nums_set.discard(val_to_remove)
print("Updated set after removal:", nums_set)

# 2. Check if two sets have no elements in common
first_set = set(map(int, input("Input numbers for the first set (space-separated): ").split()))
second_set = set(map(int, input("Input numbers for the second set (space-separated): ").split()))
if first_set.isdisjoint(second_set):
    print("The sets have no common elements.")
else:
    print("The sets have common elements.")

# 3. Get only unique items from two sets
unique_items = first_set.symmetric_difference(second_set)
print("Unique elements from both sets:", unique_items)

# 4. Convert Set to a single String
char_set = set(input("Input characters for the set (space-separated): ").split())
result_str = ''.join(char_set)
print("Converted set to string:", result_str)

# 5. Count number of vowels in a given string using sets
vowel_set = {'a', 'e', 'i', 'o', 'u'}
input_string = input("Enter a string to check for vowels: ").lower()
vowel_count = sum(1 for letter in input_string if letter in vowel_set)
print("Total vowels found:", vowel_count)