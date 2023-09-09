import roman


# Function to convert an integer to a Roman numeral
def integer_to_roman(num):
    try:
        roman_numeral = roman.toRoman(num)
        return roman_numeral
    except roman.InvalidRomanNumeralError:
        return "Invalid input. Please enter a positive integer."


# Input from the user
try:
    user_input = int(input("Enter an integer: "))
    if user_input <= 0:
        print("Please enter a positive integer.")
    else:
        roman_numeral = integer_to_roman(user_input)
        print(f"Roman numeral: {roman_numeral}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
