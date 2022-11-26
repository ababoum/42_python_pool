'''
This module defines a class Recipe
'''

import sys


class Recipe:
    '''
    A recipe object with approriate attributes
    '''

    def __init__(
            self, name: str, cooking_lvl: int, cooking_time: int,
            ingredients: list, description: str, recipe_type: str):
        # Check and set name
        if isinstance(name, str) and name:
            self.name = name
        else:
            print("Recipe name should be a non-empty string", file=sys.stderr)
            self = None
            return
        # Check and set cooking level
        if isinstance(cooking_lvl, int) and cooking_lvl in range(1, 6):
            self.cooking_lvl = cooking_lvl
        else:
            print("Cooking level should be an integer between 1 and 5",
                  file=sys.stderr)
            self = None
            return
        # Check and set cooking time
        if isinstance(cooking_time, int) and cooking_time > 0:
            self.cooking_time = cooking_time
        else:
            print("Cooking time should be a positive integer", file=sys.stderr)
            self = None
            return
        # Check and set ingredients list
        if isinstance(ingredients, list) and \
                ingredients and all(isinstance(item, str) for item in ingredients):
            self.ingredients = ingredients
        else:
            print(
                "Ingredients should be a non-empty list containing only strings",
                file=sys.stderr)
            self = None
            return
        # Check and set description
        if isinstance(description, str):
            self.description = description
        else:
            print('Description should be a string', file=sys.stderr)
            self = None
            return
        # Check and set recipe type
        if isinstance(recipe_type, str) and \
                recipe_type in ['starter', 'lunch', 'dessert']:
            self.recipe_type = recipe_type
        else:
            print('Recipe type should be "starter", "lunch", or "dessert"',
                  file=sys.stderr)
            self = None
            return
        # Check and set description
        if isinstance(description, str):
            self.description = description
        else:
            print("Description should be a string", file=sys.stderr)
            self = None
            return

    def __str__(self):
        return f'Recipe name: {self.name}\n\
    Difficulty: {self.cooking_lvl}\n\
    Cooking time: {self.cooking_time} minutes\n\
    Ingredients: {self.ingredients}\n\
    Description: {self.description}\n\
    Type: {self.recipe_type}\n'
