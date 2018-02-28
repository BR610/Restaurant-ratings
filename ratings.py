"""Restaurant rating lister."""
import sys

restaurant_data = sys.argv[1]
restaurant_ratings = {}

for line in open(restaurant_data):
    line = line.rstrip().split(':')
    restaurant_ratings[line[0]] = line[1]

new_restaurant = raw_input("What is the name of the new restaurant? ").title()
new_rating = raw_input("What rating will you give this new restaurant (out of 5)? ")

restaurant_ratings[new_restaurant] = new_rating

for key, value in sorted(restaurant_ratings.items()):
    print "{} is rated at {}.".format(key, value)


# put your code here
