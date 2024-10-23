from user_input import get_user_ingredients 
from suggestions import suggest_cocktails     

def main():
    print("Welcome to the Cocktail Program!\n")
   
    user_ingredients = get_user_ingredients()
    
    
    if not user_ingredients:
        print("It seems you didn't enter any ingredients. Please try again.")
        return  
    
    
    suggest_cocktails(user_ingredients)


if __name__ == "__main__":
    main()