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
try:
    book.add_recipe("prout")
except:
    print()

book.get_recipe_by_name("hello")
book.get_recipe_by_name("cake")

print(book.get_recipes_by_types('starter'))
print(book.get_recipes_by_types('lunch'))
print(book.get_recipes_by_types('dessert'))
try:
    book.get_recipes_by_types('breakfast')
except:
    print()
    
print(book)
