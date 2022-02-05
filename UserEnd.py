def start_user_end():
    search_method = int(input("Search using (1) locality (2) location"))
    if search_method == 1:
        handle_localities()


def search(search_keyword) -> list:
    pass


def get_restaurants_in_locality(locality) -> list:
    pass


def show_restaurant_status(selected_restaurant):
    """ Prints the number of tables with their sizes available and total tables
    in that restaurant"""
    pass


def handle_localities():
    search_keyword = input("Type in keyword to search for localities in "
                           "Toronto: ")

    possible_localities = search(search_keyword)

    # print the possible localities
    for i in range(1, len(possible_localities) + 1):
        print(i, possible_localities[i])

    print("Enter -1 to research")
    locality_no = int(input("Select the locality number: "))

    if locality_no == -1:
        handle_localities()
    else:
        locality = possible_localities[locality_no - 1]
        restaurants = get_restaurants_in_locality(locality)
        # print the restaurants in the selected locality
        for i in range(1, len(restaurants) + 1):
            print(i, restaurants[i])

        restaurant_no = int(input("Select the restaurant number: "))
        selected_restaurant = restaurants[restaurant_no]
        show_restaurant_status(selected_restaurant)






