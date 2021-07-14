# Module implements the user interface for the application.

import datastorage

def prompt_for_action():
    """
    Prompts the user for an action.

            "QUIT"
            "ADD"
            "REMOVE"
            "INVENTORY_REPORT"
            "REORDER_REPORT"
    """
    while True:
        print()
        print("What would you like to do?")
        print()
        print("A. Add an item to the inventory")
        print("R. Remove an item from the inventory")
        print("C. Generate a report of the current inventory levels.")
        print("O. generate a report of the inventory items to re-order")
        print("Q. Quit")
        print()
        user_input = input("Enter your selection: ")
        print()
        if user_input.upper() == "A":
            return "ADD"
        elif user_input.upper() == "R":
            return "REMOVE"
        elif user_input.upper() == "C":
            return "INVENTORY_REPORT"
        elif user_input.upper() == "O":
            return "REORDER_REPORT"
        elif user_input.upper() == "Q":
            return "QUIT"
        else:
            print("Invalid selection. Please try again.")

def prompt_for_product_code():
    """
    Prompts the user for a product code.

    Returns:
        A string containing the product code.
    """
    while True:
        print()
        print("Please enter the product code.")
        print()
        n = 1
        for code, description, desired_number in datastorage.products():
            print("{}. {}: {}".format(n, code, description))
            n += 1
        user_input = input("> ").strip()
        if user_input == "":
            return None
        try:
            n = int(user_input)
        except ValueError:
            print("Invalid selection. Please try again.")
            continue

        if n < 1 or n > len(datastorage.products()):
            print("Invalid selection. Please try again.")
            continue

        product_code = datastorage.products()[n-1][0]
        return product_code


def prompt_for_location():
    """ Prompt the user to select a location. """
    while True:
        print()
        print("Please select a location.")
        print()
        n = 1
        for location, description in datastorage.locations():
            print("{}. {}: {}".format(n, location, description))
            n += 1
        user_input = input("> ").strip()
        if user_input == "":
            return None
        try:
            n = int(user_input)
        except ValueError:
            print("Invalid selection. Please try again.")
            continue

        if n < 1 or n > len(datastorage.locations()):
            print("Invalid selection. Please try again.")
            continue

        location = datastorage.locations()[n-1][0]
        return location


def show_error(err_msg):
    """Displays an error message to the user."""
    print()
    print(err_msg)
    print()


def show_report(report):
    """Displays a report to the user."""
    print()
    print(report)
    print()