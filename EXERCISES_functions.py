

#Write a Python function to sum all the numbers in a list (and return that sum)
def sum_numbers(numbers):
    """
    Sums all the numbers in a list.
    
    Parameters -  numbers: list of numbers
    Returns -  sum of the numbers
    """
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage:
numbers_list = [1, 2, 3, 4, 5]
result = sum_numbers(numbers_list)
print("Sum:", result)  # Output: Sum: 15


#Write a Python function to multiply all the numbers in a list. Return that product
def multiply_numbers(numbers):
    """
    Multiply all the numbers in a list.
    
    Parameters -  numbers: list of numbers
    Returns -  sum of the numbers
    """
    total = 1
    for number in numbers:
        total *= number
    return total

# Example usage:
numbers_list = [1, 2, 3, 4, 5]
result = multiply_numbers(numbers_list)
print("Multiply:", result)  # Output: 120

#Write a Python function to reverse a string using for loops
def reverse_string(s):
    """
    Reverses a string using a for loop.
    
    Parameters - s: string to reverse
    Returns - reversed string
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage:
original_string = "hello"
reversed_result = reverse_string(original_string)
print("Reversed string:", reversed_result)  # Output: Reversed string: olleh

#Write a Python function to check whether a number is in a given range
def is_in_range(number, start, end):
    """
    Checks if a number is within a given range [start, end].
    
    Parameters  - number: the number to check
                - start: the start of the range
                - end: the end of the range
    Return -  True if the number is within the range, False otherwise
    """
    return start <= number <= end

# Example usage:
num = 5
range_start = 1
range_end = 10

if is_in_range(num, range_start, range_end):
    print(str(num) + " is in the range " + str(range_start) + " to " + str(range_end))
else:
    print(str(num) + " is NOT in the range " + str(range_start) + " to " + str(range_end))



#Write a Python function to print the even numbers from a given list
def print_even_numbers(numbers):
    """
    Prints the even numbers from a given list.
    
    Parameter -  numbers: list of integers
    Return - none. It prints within the function.
    """
    for number in numbers:
        if number % 2 == 0:
            print(number)

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
print_even_numbers(numbers_list)


#Write a Python function that checks whether a passed string is palindrome or not (same forward as backward)
def is_palindrome(s):
    """
    Checks whether a given string is a palindrome.
    
    Parameter -  s: string to check
    Return -  True if the string is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for consistent comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage:
test_string = "Racecar"
if is_palindrome(test_string):
    print(str(test_string) + " is a palindrome.")
else:
    print(str(test_string) + " is NOT a palindrome.")


#Write a Python program to access a function inside a function
def outer_function():
    """
    Outer function containing an inner function.
    """
    print("Outer function is called.")
    
    def inner_function():
        """
        Inner function defined inside the outer function.
        """
        print("Inner function is called.")
    
    # Accessing the inner function from within the outer function
    return inner_function

# Call the outer function and get the inner function
inner_func = outer_function()

# Call the inner function
inner_func()


#Write a python function that will take, as arguments, a dictionary and a string. It will then print out the value of the dictionary at the key as defined by the string
def get_value_from_dict(dictionary, key):
    """
    Prints the value of a dictionary at the specified key.
    
    :param dictionary: the dictionary to look up
    :param key: the key whose value needs to be printed
    """
    if key in dictionary:
        print(f"The value for the key '{key}' is: {dictionary[key]}")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

# Example usage:
example_dict = {"name": "Alice", "age": 30, "city": "New York"}
key_to_lookup = "age"

get_value_from_dict(example_dict, key_to_lookup)

