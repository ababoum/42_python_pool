'''
Test examples for generator.py
'''

from generator import generator

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)

print("****************SHUFFLE*****************")

for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print("***************ORDERED******************")

for word in generator(text, sep=" ", option="ordered"):
    print(word)

print("***************UNIQUE******************")

text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)

print("*********************************")

text = 1.0
for word in generator(text, sep=" "):
    print(word)
    
print("*********************************")

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="prout"):
    print(word)
    
print("*********************************")

for word in generator(None, sep=" ", option="prout"):
    print(word)
    
print("******************SCALE******************")

for word in generator("This is a simple string for a basic test. Very simple.", sep=" "):
    print(word)
print("-----------")
for word in generator("This is a simple string for a basic test. Very simple.", sep="."):
    print(word)
print("-----------")
for word in generator("This is a simple string for a basic test. Very simple.", sep="i"):
    print(word)
print("-----------")
for word in generator("This is a simple string for a basic test. Very simple.", sep="si"):
    print(word)
print("-----------")