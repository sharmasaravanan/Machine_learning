import re

string = "Python is a scripting language.Python is easy to learn"

match_obj = re.match(r'Python', string)

print(match_obj.group(0))

search_obj = re.search(r'Python', string)

print(search_obj.group(0))

print(re.findall(r'Python', string))

print(re.sub(r'Python', r'AI', string))

print(re.findall(r'\w', string))

print(re.findall(r'\w*', string))

print(re.findall(r'\w+', string))

print(re.findall(r'^\w+', string))

print(re.findall(r'\w+$', string))

print(re.findall(r'@\w+', "test@gmail.com"))

print(re.findall(r'@\w+.\w+', "test@gmail.com"))

print(re.findall(r'@\w+.(\w+)', "test@gmail.com"))

print(re.findall(r'\d{2}-\d{2}-\d{4}', "john's date of birth is 11-11-2001"))

print(re.findall(r'\d{2}-\d{2}-(\d{4})', "john's date of birth is 11-11-2001"))

print(re.findall(r'[aeiouAEIOU]\w+', string))

print(re.findall(r'\b[aeiouAEIOU]\w+', string))

print(re.findall(r'\b[^aeiouAEIOU ]\w+', string))

val = '99999999999'

if (re.match(r'[8-9]{1}[0-9]{9}', val)):
    print('yes')

text = "abc,def;ghi jkl"
print(re.split(r'[;,\s]', text))

print(re.sub(r'[;,\s]', ' ', text))

html = '<tr align="center"><td>5</td> <td>William</td> <td>Ava</td></tr>'

print(re.findall(r'<td>\w+</td>\s<td>(\w+)</td', html))

# remove the parenthesis area in a string
# github (.com) -> github


# remove words from a string of length between 1 and a given number.

# find all adverbs and their positions
# "Clearly, he has no excuse for such behavior."

# abbreviate 'Road' as 'Rd.'


# r" ?\([^)]+\)"
# '\W*\b\w{1,3}\b'
