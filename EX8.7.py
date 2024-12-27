def count_characters(s):
    char_count = {}  # Initialize an empty dictionary
    for char in s:
        if char in char_count:  # If character is already in dictionary, increment its count
            char_count[char] += 1
        else:
            char_count[char] = 1  # If character is not in dictionary, add it with count 1
    return char_count

# Input string
input_string = "Letter"

# Call the function and print the result
result = count_characters(input_string)
print(result)
