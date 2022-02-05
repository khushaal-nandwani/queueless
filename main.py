import RestaurantCaller


def run():
    print("Welcome to Track my Seat\n")
    option = int(input("Start Search (1) or Log In as a Business (2):"))

    # User
    if option == 1:
        print("Please enter the locality")

    # Restaurant Owner
    else:
        name = input("Name:")
        valid = True
        if valid:
            correct_password = "haha"   # TODO: get this from database
            password = input("Password:")
            if correct_password == password:
                RestaurantCaller.getRestaurant(name)
            else:
                RestaurantCaller.createRestaurant()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
