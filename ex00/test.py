from book import Book
from recipe import Recipe
# Crear nuevas recetas
r1 = Recipe("Pasta with tomato sauce", 2, 30, ["pasta", "tomatoes", "onions", "garlic"], "A classic Italian dish", "lunch")
r2 = Recipe("Chocolate cake", 3, 60, ["flour", "sugar", "butter", "cocoa powder", "eggs", "milk"], "A delicious dessert for chocolate lovers", "dessert")
mushroom_soup = Recipe("Cream of Mushroom Soup", 2, 45, ["mushrooms", "heavy cream", "onion", "garlic", "vegetable stock", "salt", "pepper", "thyme", "olive oil"], "A classic and delicious soup, perfect for cold days.", "starter")
spaghetti_carbonara = Recipe("Spaghetti Carbonara", 3, 30, ["spaghetti", "pancetta", "parmesan cheese", "eggs", "garlic", "salt", "pepper"], "A classic Italian pasta dish, perfect for a quick and easy dinner.", "lunch")
chocolate_chip_cookies = Recipe("Chocolate Chip Cookies", 1, 60, ["all-purpose flour", "baking soda", "salt", "butter", "granulated sugar", "brown sugar", "vanilla extract", "eggs", "chocolate chips"], "A classic and delicious dessert, perfect for any occasion.", "dessert")

book = Book("My Recipe Book")

book.add_recipe(r1)
book.add_recipe(r2)
book.add_recipe(mushroom_soup)
book.add_recipe(spaghetti_carbonara)
book.add_recipe(chocolate_chip_cookies)


book.get_recipe_by_name("Pasta with tomato sauce")

book.get_recipes_by_types("dessert")
book.get_recipes_by_types("lunch")

book.get_recipe_by_name("Cream of Mushroom Soup")