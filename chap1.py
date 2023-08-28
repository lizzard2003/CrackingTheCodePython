#1.1 Is Unique 
# this is how you would find a set of unique characters in a string 

def has_unique_characters(string):
    char_set = set() # making a new set to add the unique characters 
    for char in string:
        if char in char_set:
            return False # if there is 2 that are the same it will return false 
        char_set.add(char)
    return True

input_string = "icecube"
result = has_unique_characters(input_string)
print(result)  # Output: True

# this returns the unique chars 
# in to particular order 
def unique_characters_set(string):
    char_set = set()
    for char in string:
        char_set.add(char)
    return char_set

input_string = "abcdefg"
result_set = unique_characters_set(input_string)
print(result_set)  # Output: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

# this is without a dataset and it wil traverse  twice 

def unique_characters_set(string):
    char_set = set()
    for char in string:
        char_set.add(char)
    return char_set

input_string = "abcdefg"
result_set = unique_characters_set(input_string)
print(result_set)  # Output: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
