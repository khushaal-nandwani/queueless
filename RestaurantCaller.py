""" This file initializes or creates a new restaurant """
from Restaurant import Restaurant


def createRestaurant():
    print("Initializing a restaurant\n")
    input_name = input("Name:")
    tables_of_size_4 = input("How many tables do you "
                             "have which could accommodate 4 people?")
    tables_of_size_2 = input("How many tables do you "
                             "have which could accommodate 2 people?")

    # TODO: initialize the tables as requested
    # TODO: add those tables to the restaurant object below
    restaurant = Restaurant(input_name, )
    # TODO: update the restaurant to the database


def getRestaurant(name: str):
    # TODO: get restaurant details from the database and initialize a new
    #  restaurant
    pass



