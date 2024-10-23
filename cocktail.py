class Cocktail:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    
    def __str__(self):
        return f"{self.name} - Ingredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}\n"
    