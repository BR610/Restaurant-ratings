"""Restaurant rating lister."""
import sys

restaurant_data = sys.argv[1]
restaurant_ratings = {}


def populate_ratings_dict(restaurant_data):
    """ Populates restaurant ratings dictionary with existing data

    Takes contents of .txt file with restaurants ratings, converts them into
    keys and values in the dictionary
    """
    for line in open(restaurant_data):
        line = line.rstrip().split(':')
        restaurant_ratings[line[0]] = int(line[1])


def add_new_restaurant():
    """ Adds new restaurant and rating to dictionary

    Gets user input for restaurant name and rating, checks if rating is an int
    between 0 & 5, adds both to dictionary if valid, otherwise asks again.
    """
    while True:
        new_restaurant = raw_input("\nWhat is the name of the new restaurant? ").title()
        new_rating = raw_input("\nWhat rating will you give this new restaurant (out of 5)? ")

        try:
            new_rating = int(new_rating)
            if 0 <= new_rating <= 5:
                restaurant_ratings[new_restaurant] = new_rating
                break

        except:
            pass

        print "That's not a valid input, try again!"


def print_ratings_dictionary_sorted():
    """ Prints the contents of the ratings dictionary in alphabetical order """
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print
        print "{} is rated at {}.".format(restaurant, rating)


def show_menu():
    """ Continuously show restaurant ratings menu until user quits """
    while True:
        print """\nRestaurant Ratings
        What do you want to do?
        A. View current restaurant ratings
        B. Add a new restaurant
        C. Quit"""

        user_choice = raw_input("\n> ").upper()

        if user_choice == "A":
            print_ratings_dictionary_sorted()
        elif user_choice == 'B':
            add_new_restaurant()
        elif user_choice == 'C':
            break
        else:
            print "\nEnter valid choice"

populate_ratings_dict(restaurant_data)
show_menu()

# put your code here
