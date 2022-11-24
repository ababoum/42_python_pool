'''
This module defines a program that manages a cookbook in the form of a dictionary
'''

import sys

cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def print_recipes():
    '''
    Displays all the recipe names
    '''
    if not cookbook:
        print("The cookbook is empty!")
    else:
        for recipe in cookbook:
            print(recipe)


def print_recipe_details(recipe_name):
    '''
    Displays the details of a recipe with a given name from the cookbook
    '''
    try:
        if recipe_name not in cookbook:
            raise KeyError
        print(f'Recipe for {recipe_name}')
        print(f'  Ingredients list: {cookbook[recipe_name]["ingredients"]}')
        print(f'  To be eaten for {cookbook[recipe_name]["meal"]}.')
        print(
            f'  Takes {cookbook[recipe_name]["prep_time"]} minute(s) of cooking.')
    except KeyError:
        print(
            f"\033[93m{recipe_name} does not exist in the cookbook!\033[0m", file=sys.stderr)


def delete_recipe(recipe_name):
    '''
    Deletes a recipe from the cookbook'''
    try:
        if not recipe_name:
            raise KeyError
        cookbook.pop(recipe_name)
        print(
            f'\033[32mRecipe {repr(recipe_name)} successfully deleted from the notebook\033[0m')
    except KeyError:
        print(
            f"\033[93m{repr(recipe_name)} does not exist in the cookbook!\033[0m", file=sys.stderr)


def input_recipe_name():
    '''
    Prompts user for recipe name until it's not empty, then returns it
    '''
    name = ""
    while not name:
        print("Enter a name:")
        name = sanitize_input()
        if not name:
            print(
                "\033[93mRecipe name cannot be empty!\033[0m", file=sys.stderr)
    return name

def add_recipe():
    '''
    Add a recipe to the cookbook with the information input by the user
    '''
    name = input_recipe_name()
    if name in cookbook:
        print(
            f"\033[93m{repr(name)} already exists!\033[0m", file=sys.stderr)
        return

    ingredients = []
    item = ""
    while not ingredients:
        print("Enter ingredients:")
        while not item:
            item = sanitize_input()
            if item:
                ingredients.append(item)
                item = ""
            else:
                break
        if not ingredients:
            print(
                "\033[93mIngredients list cannot be empty!\033[0m", file=sys.stderr)
    meal_type = ""
    while not meal_type:
        print("Enter a meal type:")
        meal_type = sanitize_input()
        if not meal_type:
            print(
                "\033[93mMeal type cannot be empty!\033[0m", file=sys.stderr)
    prep_time = 0
    while prep_time <= 0:
        print("Enter a preparation time:")
        try:
            prep_time = int(input())
            if prep_time <= 0:
                raise ValueError
        except (ValueError, EOFError):
            print(
                "\033[93mPreparation time should be a positive integer!\033[0m", file=sys.stderr)
            prep_time = 0

    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal_type,
        'prep_time': prep_time
    }
    print(f'\033[32mRecipe "{name}" successfully added to the notebook\033[0m')


def sanitize_input():
    '''
    Checks if the user input is not empty and sent with an EOF
    '''
    try:
        ret = input()
    except EOFError:
        ret = ""
    return ret


OPTIONS_LIST = "List of available option:\n\
	1: Add a recipe\n\
	2: Delete a recipe\n\
	3: Print a recipe\n\
	4: Print the cookbook\n\
	5: Quit"

print('Welcome to the Python Cookbook !')
print(f'{OPTIONS_LIST}')
while True:
    print("\nPlease select an option:")
    try:
        option = int(input())
        print()
        if option not in range(1, 6):
            raise ValueError
    except (ValueError, EOFError):
        print("\033[93mSorry, this option does not exist.\033[0m")
        print(OPTIONS_LIST)
        continue
    if option == 1:
        add_recipe()
    elif option == 2:
        print("Enter the name of the recipe you wish to delete:")
        recipe_name_input = sanitize_input()
        delete_recipe(recipe_name_input)
    elif option == 3:
        print("Enter the name of the recipe you wish to display:")
        recipe_name_input = sanitize_input()
        print_recipe_details(recipe_name_input)
    elif option == 4:
        print_recipes()
    elif option == 5:
        print("Cookbook closed. Goodbye !")
        break
