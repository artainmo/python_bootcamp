cookbook = {
    'sandwich' : {
    'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
    'meal' : "lunch",
    'prep_time' : 10,
    } ,
    'cake' : {
    'ingredients' : ["flour", "sugar", "eggs"],
    'meal' : "dessert",
    'prep_time' : 60,
    } ,
    'salad' : {
    'ingredients' : ["avocado", "arugula", "tomatoes", "spinach"],
    'meal' : "lunch",
    'prep_time' : 15,
    } ,
}

def add_recipe(recipe, ingredients, meal, prep_time):
    new_rec = {
    recipe :{
    "ingredients" : ingredients,
    'meal' : meal,
    'prep_time' : 15,
    }
    }
    cookbook.update(new_rec)

def del_recipe(recipe):
    cookbook.pop(recipe)

def print_recipe(recipe):
    print("Recipe for " + recipe + ":")
    print("Ingredients list: " + str(cookbook[recipe]["ingredients"]))
    print("To be eaten for " + cookbook[recipe]["meal"])
    print("Takes %d minutes of cooking" % (cookbook[recipe]["prep_time"]))

def base_prompt():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    get = int(input(">> "))
    return get

get = base_prompt()
while True:
    print(get)
    if get == 1:
        recipe = input("Please enter the recipe's name to add:\n>> ")
        ingredients = input("Please list the ingredients:\n>> ")
        meal = input("Please tell us what meal:\n>> ")
        prep_time = input("Please tell us the preparation time:\n>> ")
        add_recipe(recipe, ingredients, meal, prep_time)
        get = base_prompt()
    elif get == 2:
        recipe = input("Please enter the recipe's name to delete:\n>> ")
        del_recipe(recipe)
        get = base_prompt()
    elif get == 3:
        recipe = input("Please enter the recipe's name to get its details:\n>> ")
        print_recipe(recipe)
        get = base_prompt()
    elif get == 4:
        for recipe in cookbook:
            print(recipe)
        get = base_prompt()
    elif get == 5:
        print("cookbook closed")
        exit()
    else:
        get = int(input("Tis option does not exist, please type the corresponding number.\nTo exit, enter 5.\n>> "))
