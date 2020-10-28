# Fast list, dictionary or set creation through a short loop syntax

my_list = [char for char in 'hello']
my_list2 = [n for n in range(0, 5)]
# map integration
my_list3 = [n * 2 for n in range(0, 5)]
# filter integration, applied first
my_list4 = [n * 2 for n in range(0, 5) if n % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# set
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list({i for i in some_list if some_list.count(i) > 1})

print(duplicates)

# dict

simple_dict = {
  'a': 1,
  'b': 2
}

new_dict = {k:v*2 for k,v in simple_dict.items() if v % 2 == 0}
print(new_dict)