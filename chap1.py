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


# permutation
# check the char count of both strings if they are not equal then they are not permutations
# we can then sort them  and compare them
# Solution 2 if they are equal
# we map each character to its frequency 
# bhasically making a hashtable
# for the fist string we increment throught the first string and for the second we decrament
from itertools import permutations

def generate_permutations(input_list):
    perm_list = list(permutations(input_list))
    return perm_list

my_list = [1, 2, 3]
permutations_result = generate_permutations(my_list)

for perm in permutations_result:
    print(perm)
 # this code returns every permutation between 1 and 3 


def are_permutations(str1, str2):
    # Remove spaces and convert strings to lowercase for accurate comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings match
    return sorted(str1) == sorted(str2)

# Test cases
string1 = "Listen"
string2 = "Silent"
print(are_permutations(string1, string2))  # Should print True

string3 = "Hello"
string4 = "World"
print(are_permutations(string3, string4))  # Should print False

#1.3 URLify: Write a method to replace all space in a string with a '%20'
# we are working backwards and inserting 0 first then 2
# there is enough space at the end to put all the needed chars in the string
def replace_spaces_with_percent20(input_str, true_length):
    # Convert the string to a list of characters to modify in-place
    char_list = list(input_str)

    # Calculate the number of spaces in the true_length part of the string
    space_count = char_list[:true_length].count(' ')

    # Calculate the index to start adding characters from the end
    new_index = true_length + space_count * 2

    # Iterate through the string in reverse order and replace spaces with '%20'
    for i in range(true_length - 1, -1, -1):
        if char_list[i] == ' ':
            char_list[new_index - 1] = '0'
            char_list[new_index - 2] = '2'
            char_list[new_index - 3] = '%'
            new_index -= 3
        else:
            char_list[new_index - 1] = char_list[i]
            new_index -= 1

    return ''.join(char_list)

# Test
input_str = "Mr John Smith    "
true_length = 13
result = replace_spaces_with_percent20(input_str, true_length)
print(result)  # Should print "Mr%20John%20Smith"
