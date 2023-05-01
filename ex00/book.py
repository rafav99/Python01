from recipe import Recipe
from datetime import date, datetime

class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : [] }
        if not isinstance(self.name, str) or len(self.name) == 0:
            print("Error: name must be a non-empty string")
            exit(1)
        if not isinstance(self.last_update, date):
            print("Error: last_update must be a date")
            exit(1)
        if not isinstance(self.creation_date, date):
            print("Error: creation_date must be a date")
            exit(1)
        if not isinstance(self.recipes_list, dict):
            print("Error: recipes_list is a dictionary")
            exit(1)
    def get_recipe_by_name(self, name):
        found = 0
        for i in self.recipes_list["starter"]:
            if i.name == name:
                print(i)
                found = 1
        for i in self.recipes_list["lunch"]:
            if i.name == name:
                print(i)
                found = 1
        for i in self.recipes_list["dessert"]:
            if i.name == name:
                print(i)
                found = 1
        if found == 0:
            print("Error: recipe not found")
            exit(1)
    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("Error: argument must be a Recipe")
            exit(1)
        if recipe.recipe_type == "starter":
            self.recipes_list["starter"].append(recipe)
        if recipe.recipe_type == "lunch":
            self.recipes_list["lunch"].append(recipe)
        if recipe.recipe_type == "dessert":
            self.recipes_list["dessert"].append(recipe)
        self.last_update= datetime.now()
    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipes_list:
            print("Error: insert a valid recipe type")
            exit(1)
        namelist = []
        for i in self.recipes_list[recipe_type]:
            namelist.append(i.name)
        print("{} recipes:".format(recipe_type),', '.join(namelist))
    