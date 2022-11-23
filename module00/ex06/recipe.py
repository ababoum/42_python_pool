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
    for recipe in cookbook:
        print(recipe)


def print_recipe_details(recipe_name):
    try:
        print(repr(cookbook[recipe_name]))
    except:
        print(
            f"\033[93m{recipe_name} does not exist in the cookbook!\033[0m", file=sys.stderr)


def delete_recipe(recipe_name):
    try:
        cookbook.pop(recipe_name)
    except:
        print(
            f"\033[93m{recipe_name} does not exist in the cookbook!\033[0m", file=sys.stderr)


def add_recipe():
    name = ""
    while not name:
        print("Enter a name:")
        name = input()
        if not name:
            print(
                "\033[93mRecipe name cannot be empty!\033[0m", file=sys.stderr)

    ingredients = []
    item = ""
    while not ingredients:
        print("Enter ingredients:")
        while not item:
            item = input()
            if item:
                ingredients += item
                item = ""
            else:
                break
        if not ingredients:
            print(
                "\033[93mIngredients list cannot be empty!\033[0m", file=sys.stderr)
    meal_type = ""
    while not meal_type:
        print("Enter a meal type:")
        meal_type = input()
        if not meal_type:
            print(
                "\033[93mMeal type cannot be empty!\033[0m", file=sys.stderr)
    prep_time = 0
    while prep_time <= 0:
        print("Enter a preparation time:")
        try:
            prep_time = int(input())
            if prep_time < 0:
                raise Exception()
        except:
            print(
                "\033[93mPreparation time should be a positive integer!\033[0m", file=sys.stderr)
            prep_time = 0

    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal_type,
        'prep_time': prep_time
    }


print_recipes()
print("***************************")
print_recipe_details('sandwich')
print_recipe_details('prout')
print("***************************")
delete_recipe('sandwich')
print_recipes()
print("***************************")
add_recipe()
print_recipes()
