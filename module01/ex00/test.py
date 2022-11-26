'''
Test file for Recipe and Book classes
'''

from recipe import Recipe
from book import Book

cake = Recipe('cake', 4, 42, ['chocolate'], 'lunch')
print(cake)
pizza = Recipe('pizza', 4, 42, ['tomato', 'cheese'], 'dessert')
print(pizza)

book = Book('Choumicha')
print(book)

book.add_recipe(cake)
book.add_recipe(cake)
book.add_recipe(pizza)
book.add_recipe("prout")


book.get_recipe_by_name("hello")
book.get_recipe_by_name("cake")

print(book.get_recipes_by_types('starter'))
print(book.get_recipes_by_types('lunch'))
print(book.get_recipes_by_types('dessert'))
book.get_recipes_by_types('breakfast')

print(book)


print("********************SCALE EXAMPLES*****************************")

print("********************RECIPE*************************************")

try:
    Recipe("cooki", 0, 10, ["dough", "sugar", "love"],
           "deliciousness incarnate", "dessert")
except:
    pass

Recipe("cooki", 1.5, 10, ["dough", "sugar", "love"],
       "deliciousness incarnate", "dessert")
Recipe("cooki", 1, 10, [], "deliciousness incarnate", "dessert")
Recipe("cooki", 1, 10, ["dough", "sugar", "love"],
       "deliciousness incarnate", "dessert")
print("Congratulations you finally made sime delicous cookies")

print("********************BOOK***************************************")

b = Book("My seductive recipes")
print(b.creation_date)
# should be the current date and time
print(b.last_update)
# should be the same as the creation date or None

print("-----------------")
crumble = Recipe("Crumble", 1, 25, [
                 "apples", "flour", "sugar"], "delicious", "dessert")
b.add_recipe(crumble)
print(b.last_update)

print("-----------------")
b.get_recipe_by_name("Crumble")
# should print the recipe
# AND
# <Recipe object at x>

print("-----------------")
b.get_recipe_by_name("Liver Icecream")
# The recipe does not exist
# The error must be handled in a justifiable manner
# such as returning None, [], or printing an error message

print("-----------------")
print(b.get_recipes_by_types("dessert")[0])
# Should print the Crumble recipe
b.get_recipes_by_types("asdasd")
# The recipe type does not exist, error must be handled in a justifiable manner
# such as returning None, [], or printing an error message
