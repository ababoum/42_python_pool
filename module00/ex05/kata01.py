'''
Kata number 01
'''

KATA = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for element in KATA.items():
    print(f'{element[0]} was created by {element[1]}')

print("*****************************")

KATA = {
    'Python': 'Guido van Rossum'
}

for element in KATA.items():
    print(f'{element[0]} was created by {element[1]}')

print("*****************************")

KATA = {}

for element in KATA.items():
    print(f'{element[0]} was created by {element[1]}')
