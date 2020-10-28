# Functional programming insists on separation of concerns between data and the behavior of your program. Instead of object we have pure functions.
# Given the same input, we always expect the same output
# A function should not produce any side effect

from functools import reduce

def isEven(n): return n % 2 == 0
def multiplyBy2(item): return item * 2
def add(accum, item): return accum + item

input = [1, 6, 2, 9, 3, 7, 8]

# filter and map return iterables in Python 3. You must use list if you want to reuse the result, you cannot reuse a looped iterable.
f = list(filter(isEven, input))
print(f'Filter: {f}')
m = list(map(multiplyBy2, f))
print(f'Map: {m}')
# def reduce(function, iterable, initializer=None)
r = reduce(add, m, 0)
print(f'Reduce: {r}')

# Same thing as above but with lambda

f = filter(lambda n: n % 2 == 0, input)
m = map(lambda n: n * 2, f)
r = reduce(lambda acc, item: acc + item, m)
print(f'Reduce with lambda: {r}')

# Similar to https://www.php.net/manual/en/function.array-combine.php
target_list = ["c", "b", "a"]
zippped = list(zip(input, target_list))
zippped.sort(key=lambda x: x[1])
print(zippped)
