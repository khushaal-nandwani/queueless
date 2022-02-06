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
    getRestaurant(input_name)


def getRestaurant(name: str) -> Restaurant:
    #  name, table4count, table2count
    # TODO: get restaurant details from the database and initialize a new
    #  restaurant
    # restaurant_details = {name: ,tables_of_4, tables_of_2}
    return Restaurant(name, tables_of_4, tables_of_2)



