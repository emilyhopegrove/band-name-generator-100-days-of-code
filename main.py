import random
import time


def band_name():
    """
    Generates a band name based on the user's hometown and favorite childhood pet's name.

    Returns:
        A string representing the band name.
    """

    print("Welcome to the Band Name Generator game!")
    print("Ready player one?")

    while True:
        play_game = input("\nAre you ready to play? (Yes/No) ")
        if play_game.lower() == "yes":
            print("\nLet's play!")
            break
        elif play_game.lower() == "no":
            print("\nMaybe next time!")
            return
        else:
            print("\nInvalid input. Please enter Yes or No.")

    print("\nWelcome back to the Band Name Generator game!")



    #error handling: 
    #ask for user input for city and pet names and ensure they only input aphabetical characters
    #ensure spaces are acceptable so that multiple worded city or pet names are allowed
    while True:
        # Ask for user input for city/pet name and split it into a list of words
        # Check if all the words in the city input are alphabetical
        # If yes, capitalize the first letter of each word and join them back together with a space
        city = input('What city did you grow up in? ')
        if all(word.isalpha() for word in city.split()):  
            city = ' '.join(word.capitalize() for word in city.split())
            break
        else:
            # If the input is not valid, print an error message and continue the loop
            print('Please enter a valid city name (only alphabetical characters are allowed).')
            continue

    print("")
    
    while True:
        pet_name = input('What is the name of your favorite childhood pet? ')
        if all(word.isalpha() for word in pet_name.split()):
            pet_name = ' '.join(word.capitalize() for word in pet_name.split())
            break
        else:
            print('Please enter a valid pet name (only alphabetical characters are allowed).')
            continue
    

    intros = {
        "rockin' sockin'": ["The", "Sockin'"],
        "radical": ["The", "Radical"],
        "electric": ["The", "Electric"],
        "cosmic": ["The", "Cosmic"],
        "groovy": ["The", "Groovy"],
        "majestic": ["The", "Majestic"],
        "phenomenal": ["The", "Phenomenal"],
        "fabulous": ["The", "Fabulous"],
        "sensational": ["The", "Sensational"],
        "spectacular": ["The", "Spectacular"],
        "incredible": ["The", "Incredible"],
        "amazing": ["The", "Amazing"],
        "awesome": ["The", "Awesome"],
        "fantastic": ["The", "Fantastic"],
        "legendary": ["The", "Legendary"],
        "marvelous": ["The", "Marvelous"],
        "superb": ["The", "Superb"],
        "terrific": ["The", "Terrific"],
        "unforgettable": ["The", "Unforgettable"],
        "wonderful": ["The", "Wonderful"]
    }
    adjective = random.choice(['clutch', 'baller', 'sweet', 'cool', 'awesome', 'fantastic', 'magical', 'delicious', 'weird'])

    intro_key = random.choice(list(intros.keys()))
    intro = intros[intro_key]
    band_name_str = generate_band_name(city, pet_name, intro)

    print('')
    print(f'Wow! That is so {adjective}! Your band name is ')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)

    print(f'"{band_name_str}"')
    
    time.sleep(1)
    while True:
        play_again = input('Do you want to play again? (Yes/No) ').lower()
        if play_again == 'yes':
            band_name()
            break
        elif play_again == 'no':
            print('Okay, thanks for playing!')
            return
        else:
            print('Please enter a valid response (Yes/No).')
            continue

    print("")
        
            


def generate_band_name(city, pet_name, intro):
    """
    Generates a band name based on the user's hometown, favorite childhood pet's name, and an intro.

    Args:
        city: A string representing the user's hometown.
        pet_name: A string representing the user's favorite childhood pet's name.
        intro: A list of strings representing the intro for the band name.

    Returns:
        A string representing the band name.
    """
    intro_str = ' '.join(intro)
    if pet_name.endswith('s'):
        band_name = f"{intro_str} {city} {pet_name}es"
    elif pet_name.endswith('y'):
        if pet_name.endswith('ey'):
            band_name = f"{intro_str} {city} {pet_name[:-2]}ies"
        else:
            band_name = f"{intro_str} {city} {pet_name[:-1]}ies"
    else:
        band_name = f"{intro_str} {city} {pet_name}s"
    return band_name

#ask user if they are ready to play again
    while True:
    # Generate a random band name
        band_name = generate_band_name()
    
        # Display the band name to the user
        print("Your band name is: " + band_name)
    
        # Ask the user if they want to play again
        play_again = input("Do you want to generate another band name? (y/n)").lower()
    
        if play_again == "y":
            continue  # Start the loop again to generate a new band name
        else:
            print("Thanks for playing!")
            break  # Exit the loop and end the game

band_name()

