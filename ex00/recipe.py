class Recipe:
    def __init__(self, name, cooking_level, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_level = cooking_level
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        if not isinstance(self.name, str) or len(self.name) == 0:
            print("Error: name must be a non-empty string")
            exit(1)
        if not isinstance(self.cooking_level, int) or self.cooking_level < 1 or self.cooking_level > 5:
            print("Error: cooking level must be an int between  1 and 5")
            exit(1)
        if not isinstance(self.cooking_time, int) or self.cooking_time < 0:
            print("Error: cooking time must be a positive int")
            exit(1)
        if not isinstance(self.ingredients, list) or len(self.ingredients) == 0 or\
        not all(isinstance(ingredient, str) for ingredient in self.ingredients):
            print("Error: ingredients must be a non-empty list")
            exit(1)
        if not isinstance(self.description, str):
            print("Error: description must be a string")
            exit(1)
        if not isinstance(self.recipe_type, str) or self.recipe_type not in ["starter", "lunch", "dessert"]:
            print("Error: Recipe type must be 'starter', 'lunch' or 'dessert'.")
            exit(1)

    def __str__(self):
        strlist = []
        strlist.append("Recipe for {}".format(self.name))
        if len(self.description) > 0:
            strlist.append(self.description)
        strlist.append("Recipe type: {}".format(self.recipe_type))
        strlist.append("Cooking level: {}".format(self.cooking_level))
        strlist.append("Cooking time: {}".format(self.cooking_time))
        strlist.append("Ingredients: {}".format(', '.join(i for i in self.ingredients)))
        txt = '\n'.join(strlist)
        return txt

