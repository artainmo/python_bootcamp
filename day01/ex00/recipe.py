class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if int(cooking_lvl) < 0 or int(cooking_lvl) > 5:
            print("ERROR cooking level value out of range")
            exit()
        if int(cooking_time) < 0:
            print("ERROR cooking time value out of range")
            exit()
        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
            print("ERROR incorrect recipe type")
            exit()
        self.name = str(name)
        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        self.ingredients = ingredients
        self.description = str(description)
        self.recipe_type = recipe_type

# Because no value is atributed to self, use this function with this notation __str__(class) instead of class.__str__
    def __str__(self):
        txt = ""
        txt = self.name + "\n" + str(self.cooking_lvl) + "\n" +  str(self.cooking_time) + "\n"
        for ingredients in self.ingredients:
            txt += ingredients + " "
        txt += "\n" + str(self.description) + "\n" + str(self.recipe_type)
        return txt
