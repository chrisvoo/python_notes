def say_hello(name, emoji = ":-D"):
  """
  This is called docstring.
  You cannot invoke a function before its definitions (like js)
  parameters, emoji has a default value
  """
  print(f"Hello {name}, {emoji}")

# positional arguments
say_hello("Chris")

# keyword arguments
say_hello(emoji = ":-O", name = "Chris")

print(say_hello.__doc__)


# *args and **kwargs are standards, but you could call them
# whatever you want (not recommended though)
# *args is a tuple of arguments, **kwards a dictionary of arguments
def sum_numbers(*args, **kwargs):
  result = 0
  for item in kwargs.values():
    result += item

  return sum(args) + result

print(sum_numbers(1,2,3, num1=5, num2=6))

# Arguments' ordering rule:
# params, *args, default arguments, **kwargs


# Scope
# The rule:
# 1 - Start with local
# 2 - Parent local
# 3 - Global
# 4 - Built-in python
a = 1

def parent():
  a = 10
  def confusion():
    return a
  return confusion()

# at first a = 10. Then confusion is defined. When it executes it, a is not defined, so it searches
# for it in the parent scope and finds 10.
print(parent())
print(a) # in the global scope and not redefined anywhere.