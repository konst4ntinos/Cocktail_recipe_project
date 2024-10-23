from database import cocktail_db  

def suggest_cocktails(available_ingredients):
    print("\nHere are the cocktails you can make:\n")
    found_cocktails = False
    
    
    available_set = set(available_ingredients)
    
    for cocktail in cocktail_db:
        ingredients_set = set(cocktail.ingredients)
        
        if ingredients_set.intersection(available_set):
            print(cocktail)
            found_cocktails = True
    
    if not found_cocktails:
        print("Sorry, no cocktails can be made with the ingredients you have.")