# 1. Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly. 
# 2. an iterable implements the dunder method __iter__
# 3. A generator can be consumed with next(generator) until the items expire

# The example below occupies memory with all the items
#def make_list(num):
#  result = []
#  for i in range(num):
#    result.append(i*2)

#  return result

# here we occupy the memory an element at a time
def make_list(num):
  for i in range(num):
    yield i*2

# print(list(make_list(5)))

for i in make_list(5):
  print(i)
