# string operations
name = "elephant"
sent = "elephant is an animal"

print(len(name))  # to get the length of the string

# slice and dice
print(name[3])

print(name[3:])

print(name[:3])

print(name[3:6])

# string functions

print(sent)
print(sent.upper())
print(sent.lower())
print(sent.capitalize())
print(sent.title())
print("nAmE".swapcase())
print(name.count('e'))
print(name.replace('p','y'))
print(sent.split())
print(sent.split('an'))
print("an".join(sent.split('an')))
print("all the best".center(84,"~"))
print("ABC".isupper())
print("ABC".islower())
print("abc123".isalpha())
print("abc123".isalnum())
print("3 ".isspace())
print(sum((1,2,3,4,5)))
print(min((1,2,3,4,5)))
print(max((1,2,3,4,5)))

