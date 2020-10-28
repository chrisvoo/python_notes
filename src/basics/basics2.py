import getpass

username = input("username: ")
# this do not stream to stdout the password typed
password = getpass.getpass(prompt="password: ")

if username == "jayjay" and password == "secret":
  pLength = len(password)
  hiddenPass = pLength  * '*'
  print(f"Logged in as {username} with password {hiddenPass}")
else:
  print('Invalid credentials')

# ternary operator
message = "Not Chris" if username != "Chris" else "It's Chris"
print(message)

print(1 == True) # Truthy value
print(['1'] is ['1']) # checks if they have the same memory location

# multiline string used as comment, immediately garbage collected
"""
All values are considered "truthy" except for the following, which are "falsy":

None
False
0
0.0
0j
Decimal(0)
Fraction(0, 1)
[] - an empty list
{} - an empty dict
() - an empty tuple
'' - an empty str
b'' - an empty bytes
set() - an empty set
an empty range, like range(0)
objects for which obj.__bool__() returns False first, if true then checks if obj.__len__() returns 0
"""


# FOR loops
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for l in picture: # whatever iterable you want
  for b in l:
    print("*" if b == 1 else " ", end = "")
  print("")  

# range returns an iterable range object
for i in range(0, 10, 2): # step is third param
  print(i)

# enumerate returns an element and its index of an iterable
for i, char in enumerate("Hello"):
  print(f"Index: {i} -> {char}")

i = 0
while i < 2:
  i += 1
  print(i)
  # break
else:
  # this gets printed only if there are no break statements
  print("Loop terminated")