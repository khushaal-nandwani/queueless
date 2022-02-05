""" This file initializes or creates a new restaurant """
from Restaurant import Restaurant


def createRestaurant():
    print("Initializing a restaurant\n")
    input_name = input("Name:")
    tables_of_size_4 = int(input("How many tables do you "
                             "have which could accommodate 4 people?"))
    tables_of_size_2 = int(input("How many tables do you "
                             "have which could accommodate 2 people?"))
    # TODO: update database


    # TODO: add those tables to the restaurant object below
    restaurant = Restaurant(input_name, )
    # TODO: update the restaurant to the database


def getRestaurant(name: str):
    #  name, table4count, table2count
    # TODO: get restaurant details from the database and initialize a new
    #  restaurant

    # arr1 = [
    # [capacity, taken, total_tables]
    #   [4, x, y]
    #   [2, a, z]
    # ]
    pass



