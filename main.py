import RestaurantCaller
import UserEnd
from Restaurant import Restaurant


def run_restaurant(rest: Restaurant):
    menu = "1. Occupy Table \n" \
           "2. Vacate Table \n" \
           "3. Add Table \n" \
           "4. Remove Table\n"
    menu_no = int(input(menu))
    occupancy = int(input("Specify the table size"))
    rest_functions = [rest.add_table, rest.occupy_table, rest.remove_table, rest.vacate_table]
    rest_functions[menu_no + 1]()
    rest_returns = ["Table Occupied Successfully", "Table vacated",
                    "New Table has been added", "Table has been removed"]

    print(rest_returns, '\n')



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
                created_restaurant = RestaurantCaller.getRestaurant(name)
                run_restaurant(created_restaurant)

            else:
                RestaurantCaller.createRestaurant()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
