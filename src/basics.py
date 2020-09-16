# Numbers
# https://docs.python.org/3.8/library/stdtypes.html#numeric-types-int-float-complex
print(type(2 + 4))   # int
print(type(6 * .3))  # float
print(type(6 ** 6))  # power of a number
print(type(6 // 5))  # int, rounds down to nearest whole number

# math functions
# https://docs.python.org/3.8/library/math.html#module-math
print(round(5.3))    # to the nearest int
print(abs(-5.6))     # absolute value

# Variables
a, b = 3, 5.4        # multiple assignments shortcut
print(b)

# ; is used to separate commands on a single line.
a = 5; b = 6; c = a; a = 9   
print(c)             # still 5, passed by value, not reference (immutable objects)

# Strings
longString = '''
This is 
a long 
String
'''
print(longString)
print('Concatenation ' + str(5))  # needs type conversion

name = 'Chris'
age = 39
print(f'Hi {name}, you\'re {age} years old') # formatted string (Python 3)
print('Hi {}, you\'re {} years old'.format(name, age)) # Python 2

# print("Hello {}, your balance is {}.".format("Cindy", 50))
# print("Hello {0}, your balance is {1}.".format("Cindy", 50))
# print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
# print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

slicing = "I'm a string"
print(slicing[6:])        # : means till the end, last char excluded
print(slicing[0:3:2])     # stepover, take a char every two chars in this case
print(slicing[::-1])      # reverse