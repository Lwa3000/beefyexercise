shopping_list = {"Target": ["socks", "soap", "detergent", "sponges"], 
                 "Bi-Rite": ["butter", "cake", "cookies", "bread"],
                 "Berkeley Bowl": ["oranges", "bananas", "milk"], }


def show_menu():
    print menu

    print """
    0 - Main Menu
    1 - Show all lists.
    2 - Show a specific list.
    3 - Add a new shopping list.
    4 - Add an item to a shopping list.
    5 - Remove an item from a shopping list.
    6 - Remove a list by nickname.
    7 - Exit when you are done.
    """

def show_all_lists():
    print shopping_list.keys()

def show_specific_list(store):
    print shopping_list[store]

