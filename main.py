import RestaurantCaller
import UserEnd
from Restaurant import Restaurant


def run_restaurant(rest: Restaurant):
    print("Welcome to Queueless, Please select an option from below \n")

    menu_no = 1
    decided = True
    while(decided):
        menu = "1. Occupy Table \n" \
               "2. Vacate Table \n" \
               "3. Add Table \n" \
               "4. Remove Table\n" \
               "5. Exit\n"
        menu_no = int(input(menu))
        if menu_no == 5:
            return
        if menu_no >= 1 and menu_no <= 4:
            break
        print("Please select a valid option")

    occupancy = int(input("Specify the table size"))
    rest_functions = [rest.add_table, rest.occupy_table, rest.remove_table, rest.vacate_table]
    rest_functions[menu_no + 1]()
    rest_returns = ["Table Occupied Successfully", "Table vacated",
                    "New Table has been added", "Table has been removed"]
    # TODO: update the database
    print(rest_returns[menu_no + 1], '\n')



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
                rest: Restaurant
                rest = RestaurantCaller.createRestaurant()
                run_restaurant(rest)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
