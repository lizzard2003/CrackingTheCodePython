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

#1.4 Palindrome Permutation
# palindrome is a word or phrase that is the same forward and backwards
# we need to return true or false
def is_permutation_of_palindrome(s):
    # Convert the string to lowercase and remove non-letter characters
    s = ''.join(filter(str.isalpha, s.lower()))

    # Count the occurrences of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Count the number of characters with odd occurrences
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
    
    return True

# Example usage
input_string = "whattootsie"
result = is_permutation_of_palindrome(input_string)
if result:
    print("The string is a permutation of a palindrome.")
else:
    print("The string is not a permutation of a palindrome.")
 
 #One way 
 # ways to see of a string is edited
 # this is changing only one character
 # you are supposed to return true or false

def is_one_edit_away(str1, str2):
    # Calculate the length difference between the two strings
    len1, len2 = len(str1), len(str2)
    if abs(len1 - len2) > 1:
        return False  # If the length difference is more than 1, it's not one edit away

    # Ensure str1 is the shorter string
    if len1 > len2:
        str1, str2 = str2, str1

    i, j = 0, 0  # Pointers for the two strings
    found_difference = False  # Flag to track if a difference is found

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if found_difference:
                return False  # If a second difference is found, it's not one edit away
            found_difference = True  # Set the flag for the first difference

            if len1 == len2:
                i += 1  # If the lengths are the same, move the pointer in the shorter string
        else:
            i += 1  # If characters match, move both pointers
        j += 1

    return True

# Example usage:
str1 = "pale"
str2 = "kaale"
result = is_one_edit_away(str1, str2)
print(result)  # Output should be True

# 1.6 String Compression
# compress the string and count the amount of letters in the string as it fgoes throug 
# if the string and the counting is the sam lenght then return the original string 
# you are trying to bring back a shorter version 
def compress_string(s):
    if not s:
        return s  # Return the original string if it's empty

    compressed = []
    count = 1

    for i in range(1, len(s)): # start at 1
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))  # Add the last character and its count

    compressed_str = ''.join(compressed)

    # Return the compressed string only if it's shorter than the original
    return compressed_str if len(compressed_str) < len(s) else s

# Example usage:
input_str = "aabcccccaaa"
compressed_result = compress_string(input_str)
print(compressed_result)  # Output should be "a2b1c5a3"

#1.7 Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is represented 
# by an interger, write a method
# to rotate the image 90 degree, Can you do this in place? 
def rotate_matrix(matrix):
    if not matrix:
        return matrix  # Return the original matrix if it's empty

    n = len(matrix)

    # Perform a series of swaps to rotate the matrix 90 degrees in place
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save the top element
            top = matrix[first][i]
            # Move left element to top
            matrix[first][i] = matrix[last - offset][first]
            # Move bottom element to left
            matrix[last - offset][first] = matrix[last][last - offset]
            # Move right element to bottom
            matrix[last][last - offset] = matrix[i][last]
            # Move top element to right
            matrix[i][last] = top

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)

# The matrix will be rotated 90 degrees in place
for row in matrix:
    print(row)

#1.8 Zero Matrix
#Write an algorithm such that if an element in a MxN matrix is 0, 
# its entire row and column are set to 0.

def set_zeros(matrix):
    if not matrix:
        return matrix  # Return the original matrix if it's empty

    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    # Identify rows and columns containing zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set rows to zero
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0

    # Set columns to zero
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

set_zeros(matrix)

# The matrix will have rows and columns with zeros set to zero
for row in matrix:
    print("----------")
    print(row)
