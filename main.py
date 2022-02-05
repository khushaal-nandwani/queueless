import RestaurantCaller
import UserEnd


def run():
    print("Welcome to Track my Seat\n")
    option = int(input("Start Search (1) or Log In as a Business (2):"))

    # User End
    if option == 1:
        UserEnd.start_user_end()

    # Restaurant Owner
    else:
        username = input("Username:")
        valid = True    # TODO: validate from API
        if valid:
            correct_password = "haha"   # TODO: get this from database/Api
            password = input("Password:")
            if correct_password == password:
                RestaurantCaller.getRestaurant(name)
            else:
                RestaurantCaller.createRestaurant()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
