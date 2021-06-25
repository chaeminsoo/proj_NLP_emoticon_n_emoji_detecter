import re

p = re.compile('[a-z]+')

result = p.findall('I am sorry youare not feeling well. :(')
print(result)