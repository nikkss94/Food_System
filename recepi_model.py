class RecipePreview(object):

    def __init__(self, _id, title, usedIngredientCount, missedIngredientCount, likes):
        self.recipeId = _id
        self.title = title
        self.usedIngredientCount = usedIngredientCount
        self.missedIngredientCount = missedIngredientCount
        self.likes = likes

    def getId(self):
        return self.recipeId

    def getTitle(self):
        return self.title

    def getUsedIngredientCount(self):
        return self.usedIngredientCount

    def getMissedIngredientCount(self):
        return self.missedIngredientCount

    def getLikes(self):
        return self.likes