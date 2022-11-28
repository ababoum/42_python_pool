'''
Test examples for game.py classes
'''

from game import Stark, GotCharacter

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()

print(arya.is_alive)
arya.die()
print(arya.is_alive)

print(arya.__doc__)


print("*********************************************")

anonymous = GotCharacter()
print(anonymous.first_name)
print(anonymous.is_alive)

luigi = GotCharacter("Name", True)
print(luigi.first_name)
print(luigi.is_alive)

print(luigi.__doc__)

print("*********************************************")

robert = Stark("Robert")
print(robert.__dict__)
robert.die()
print(robert.__dict__)