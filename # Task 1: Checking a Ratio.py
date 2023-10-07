# Task 1: Checking a Ratio

def check_ratio(number):
    # Extract individual digits from the number
    first_digit = number // 1000
    second_digit = (number // 100) % 10
    third_digit = (number // 10) % 10
    fourth_digit = number % 10
    
    # Check if the ratio holds
    if (first_digit + fourth_digit) == (second_digit - third_digit):
        return "yes"  # If yes, return "yes"
    else:
        return "no"   # If no, return "no"


# Task 2: Internet Access

def internet_access(age):
    if age >= 18:
        return "Access allowed"  # If age is 18 or higher, access is allowed
    else:
        return "Access denied"   # Otherwise, access is denied


# Task 3: Arithmetic Progression

def is_arithmetic_progression(a, b, c):
    return (b - a) == (c - b)  # Check if the numbers form an arithmetic progression


# Task 4: Rook Move

def rook_move(x1, y1, x2, y2):
    return (x1 == x2) or (y1 == y2)  # Check if a rook can move from one square to another


# Task 5: King's Move

def kings_move(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1  # Check if a king can move from one square to another


# Task 6: Average of the Largest Numbers

def average_of_largest(a, b, c):
    # Find the largest number by sorting the list
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]  # Return the second largest number (average of the largest)


# Task 7: Number of Days in a Month

def days_in_month(month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]  # Get the number of days for the given month


# Task 8: Determine Weight Category

def weight_category(weight):
    if weight <= 60:
        return "Light weight"
    elif weight <= 64:
        return "First welterweight"
    elif weight <= 69:
        return "Welterweight"


# Task 9: Compare Passwords

def compare_passwords(password, confirmation):
    if password == confirmation:
        return "Password accepted"  # If passwords match, they are accepted
    else:
        return "Password not accepted"  # If not, they are not accepted


# Task 10: Even or Odd?

def even_or_odd(number):
    if number % 2 == 0:
        return "Even value"  # If the number is even, it's an even value
    else:
        return "Odd number"  # If not, it's an odd number


# Task 11: Find the Smallest of Two Numbers

def smallest_of_two(a, b):
    return min(a, b)  # Return the smallest of two numbers


# Task 12: Determine Age Group

def age_group(age):
    if age <= 13:
        return "childhood"
    elif age <= 24:
        return "youth"
    elif age <= 59:
        return "maturity"
    else:
        return "old age"


# Task 13: Identify Triangle Type

def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Versatile"