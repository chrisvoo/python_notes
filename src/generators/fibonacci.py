# When you call a function that contains a yield statement anywhere, you get a generator object, but no code runs. Then each time you extract an object from the generator, Python executes code in the function until it comes to a yield statement, then pauses and delivers the object. When you extract another object, Python resumes just after the yield and continues until it reaches another yield (often the same one, but one iteration later). This continues until the function runs off the end, at which point the generator is deemed exhausted.

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
      yield x
      x, y = y, x+y


print(list(fibonacci_numbers(25)))

'''
x = 0
y = 1
0
x = 1
y = 1
1
x = 1
y = 2
1
x = 2
y = 3
2
x = 3
y = 5
3
'''