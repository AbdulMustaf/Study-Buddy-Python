# example.py

def greet(name):
    """Greets the user by name."""
    return f"Hello, {name}!"

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides the first number by the second.
    
    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of division.

    Raises:
        ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def factorial(n):
    """Calculates the factorial of a number.
    
    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_palindrome(word):
    """Checks if a word is a palindrome.
    
    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]

def fibonacci(n):
    """Generates the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def calculate_area(shape, *dimensions):
    """Calculates the area of a given shape.
    
    Args:
        shape (str): The shape type ('circle', 'rectangle', 'triangle').
        dimensions (tuple): The dimensions required for the shape.

    Returns:
        float: The area of the shape.

    Raises:
        ValueError: If the shape is not recognized.
    """
    if shape == "circle":
        radius = dimensions[0]
        return 3.14159 * radius ** 2
    elif shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "triangle":
        base, height = dimensions
        return 0.5 * base * height
    else:
        raise ValueError("Unknown shape.")

def read_file(file_path):
    """Reads and returns the content of a file.
    
    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    with open(file_path, "r") as file:
        return file.read()

def write_to_file(file_path, content):
    """Writes content to a file.
    
    Args:
        file_path (str): The path to the file.
        content (str): The content to write.
    """
    with open(file_path, "w") as file:
        file.write(content)

def count_words(sentence):
    """Counts the number of words in a sentence.
    
    Args:
        sentence (str): The sentence to count words in.

    Returns:
        int: The number of words in the sentence.
    """
    return len(sentence.split())

def reverse_list(lst):
    """Reverses a list.
    
    Args:
        lst (list): The list to reverse.

    Returns:
        list: The reversed list.
    """
    return lst[::-1]

def find_max(numbers):
    """Finds the maximum number in a list.
    
    Args:
        numbers (list): The list of numbers.

    Returns:
        int or float: The maximum number.
    """
    return max(numbers)

def sort_list(lst):
    """Sorts a list in ascending order.
    
    Args:
        lst (list): The list to sort.

    Returns:
        list: The sorted list.
    """
    return sorted(lst)

def validate_email(email):
    """Validates if the given email is in a proper format.
    
    Args:
        email (str): The email to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    import re
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def convert_to_uppercase(text):
    """Converts a string to uppercase.
    
    Args:
        text (str): The string to convert.

    Returns:
        str: The uppercase version of the string.
    """
    return text.upper()
