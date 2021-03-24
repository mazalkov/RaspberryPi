# https://www.learnpython.org/en/Sets


a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

a, b = set(a), set(b) 

print(a.difference(b))
