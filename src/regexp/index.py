import re

s = 'search this inside this string!'

# raw string, you can avoid escaping chars
pattern = re.compile(r'this')

print(pattern.search(s).span()) # (7, 11) tuple index start/end
print(pattern.findall(s)) # ['this', 'this']