import random
import utility
import my_package.utils as utils
from my_package.stuff import stuff, more_stuff

# The pycache is created everytime we use modules. It contains compiled files.
# The file that we run has __name__ set to __main__.
# A package is simply a folder containing multiple modules inside. At the
# root of the package there's always a file named __init__.py, used by the
# interpreter to recognize a Python package.

# the reason for you may see something similar is that you want a code to
# be executed only if you run this file
if __name__ == '__main__':
  print(utility.multiply(5, 6))
  utils.mypack([1,2,3])
  stuff()
  more_stuff()

  print(random.random())