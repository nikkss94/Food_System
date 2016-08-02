import requests
import json
from recepi_model import *


class BaseControler(object):
    BASE_URL = "https://spoonacular.com/food-api"
    FIND_BY_INGREDIENTS_URL = "/recipes/findByIngredients/"
    FIND_BY_INGREDIENTS_REQUEST_URL = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients/"
    COMPLEX_SEARCH_URL = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/searchComplex"

    def __init__(self):
        pass

    def findByIngredientsRequest(self, ingredients, minCalories):
        payload = {"fillIngredients": "false", "ingredients": ingredients,
                   "number": "5", "minCalories": minCalories}

        our_headers = {
            "X-Mashape-Key": "Yprbv94upimshzf5FbZ1oPNXQNv5p1dek6ijsnGaropI0MNMdn",
            "Accept": "application/json"
        }

        response = requests.get(self.FIND_BY_INGREDIENTS_REQUEST_URL,
                                params=payload,
                                headers=our_headers)

        test = {}
        test = response.json()
        response_list = []

        for x in test:
            response_list.append(RecipePreview(x["id"], x["title"], x[
                                 "usedIngredientCount"], x["missedIngredientCount"], x["likes"]))

        return response_list

