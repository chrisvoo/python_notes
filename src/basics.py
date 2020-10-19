print("Numbers\n" + "-" * 50)

# https://docs.python.org/3.8/library/stdtypes.html#numeric-types-int-float-complex
print(type(2 + 4))   # int
print(type(6 * .3))  # float
print(type(6 ** 6))  # power of a number
print(type(6 // 5))  # int, rounds down to nearest whole number

# math functions
# https://docs.python.org/3.8/library/math.html#module-math
print(round(5.3))    # to the nearest int
print(abs(-5.6))     # absolute value

print("\nVariables\n" + "-" * 50)

a, b = 3, 5.4        # multiple assignments shortcut
print(b)

# ; is used to separate commands on a single line.
a = 5; b = 6; c = a; a = 9   
print(c)             # still 5, passed by value, not reference (immutable objects)

print("\nStrings\n" + "-" * 50)

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
print(slicing[::-1])      # reverse, a new list
print(' '.join(["A", "string", "concatenation"]))

print("\nLists\n" + "-" * 50)

# They're ordered sequences of objects (a form of array). Lists aren't immutable
collection = ['apples', 'bananas', 'oranges', 5, 3.4]
print(collection[1:]) # list slicing, ['bananas', 'oranges', 5, 3.4]
new_collection = collection
print(new_collection[0] == collection[0])  # Passed by reference
# to copy a list, you need to slice it, like collection[:]

# Nested lists
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
print(basket[1][1][0])
basket.append("Grape")
basket.extend(["Oranges", "Banana"]) # duplicated item
print(basket.index("Banana") == 0)
print(("Banana" in basket) is True)

print("\nUpacking - " + str(basket) + " -\n")
a, b, *others, d = basket
print(a)
print(others)
print(d) # duplicated item


# An unordered key-value pairs, whose keys must be unique and immutable (strings, booleans and numbers are valid key types)
print("\nDictionary\n" + "-" * 50)

aDict = {
  "a": 1,
  "b": "hello",
  "c": [1, 2],
  123: 'By number'
}

print(aDict[123])
print(aDict.get("age", 39)) # Default value if age does not exist
print("a" in aDict) # check keys
print("hello" in aDict.values())
aDict.update({
  "newItem": "hey",
  "a": 2
})
print(aDict.items())

# It's like an immutable list. Items can be accessed by index
print("\Tuples\n" + "-" * 50)
my_tuple = (1, 5, "a")

# An order collection of unique objects. It doesn't support indexing, more similar to dictionaries than lists. Conversions to/from lists it's pretty seamless with their respective constructor.
# Set has many math set methods. Union and intersection can be also applied with | and & 
print("\Sets\n" + "-" * 50)
my_set = { 1, "z", 5, 3, "a", 3, 2 }
my_set.add(4)
print(my_set) # duplicates silently discarded


school = {'Bobby','Tammy','Jammy','Sally','Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
# no need to convert here
print(school.difference(attendance_list))
