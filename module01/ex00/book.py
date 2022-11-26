'''
This module defines a class Book
'''

from datetime import datetime
from datetime import date
from time import sleep
import sys
from recipe import Recipe


class Book:
    '''
    A book containg recipes
    '''

    def __init__(self, name: str):
        # Check and set name
        if isinstance(name, str) and name:
            self.name = name
        else:
            sys.exit("Book name should be a non-empty string")

        self.last_update = str(date.today()) + \
            " at " + str(datetime.now().strftime("%H:%M:%S"))
        self.creation_date = str(date.today())
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }

    def __str__(self) -> str:
        return f'Book name: {self.name}\n\
    Created on: {self.creation_date}\n\
    Last update: {self.last_update}\n'

    def get_recipe_by_name(self, name):
        """Prints a recipe with the given name and returns the instance"""
        if not isinstance(name, str) or not name:
            print("Parameter name should be a non-empty string", file=sys.stderr)
            return None
        search_list = self.recipes_list['starter'] + \
            self.recipes_list['lunch'] + \
            self.recipes_list['dessert']
        for recipe in search_list:
            if recipe.name == name:
                print(recipe)
                return recipe
        print(f"No recipe found with the name {name}")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if not isinstance(recipe_type, str) or \
                recipe_type not in ['starter', 'lunch', 'dessert']:
            print('Recipe type should be "starter", "lunch", or "dessert"',
                  file=sys.stderr)
            return None

        return [recipe.name for recipe in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        print("Adding recipe...")
        sleep(1)
        if not isinstance(recipe, Recipe):
            print('Parameter recipe should be an instance of Recipe')
            return
        if any([item for item in self.recipes_list[recipe.recipe_type]
                    if item.name == recipe.name]):
            print(
                f"A recipe with the name {recipe.name} already exists in the book!")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = str(date.today()) + \
            " at " + str(datetime.now().strftime("%H:%M:%S"))
        print(
            f"Recipe {recipe.name} successfully added to the book!")
