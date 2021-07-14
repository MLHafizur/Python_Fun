# We store our data in three private globals:
#
#    'items'
#
#        The list of current inventory items.  Each item in this list is a
#        (product_code, location_code) tuple.
#
#    'products'
#
#       The list of products we can hold inventory for.  Each item in this list
#       is a (code, description, desired_number) tuple, where 'code is a code
#       identifying the product, 'description' is a string describing that
#       product so the user can identify it, and 'desired_number' is the
#       desired number of items that the user wants to keep in the inventory.
#
#    'locations'
#
#       The list of locations where inventory can be stored.  Each item in this
#       list is a (code, description) tuple, where 'code is the code for an
#       inventory location, and 'description' is a string describing that
#       location so that the user knows where it is.

import json
import os.path


def init():
    """Initialize the datastorage module.
    """
    _load_items()

def items():
    """Return a list of all items in the inventory.
    """
    global _items
    return _items

def products():
    """Return a list of all products in the inventory.
    """
    global _products
    return _products

def locations():
    """Return a list of all locations in the inventory.
    """
    global _locations
    return _locations

def add_item(product_code, location_code):
    """Add an item to the inventory.

    'product_code' is the code for the product to add.
    'location_code' is the code for the location to add the item to.
    """
    global _items
    _items.append((product_code, location_code))
    _save_items()

def remove_item(product_code, location_code):
    """Remove an item from the inventory.

    'product_code' is the code for the product to remove.
    'location_code' is the code for the location to remove the item from.
    """
    global _items
    for i in range(len(_items)):
        if _items[i][0] == product_code and _items[i][1] == location_code:
            del _items[i]
            _save_items()
            return True
    return False

def set_products(products):
    """Set the list of products we can hold inventory for.

    'products' is a list of (code, description, desired_number) tuples.
    """
    global _products
    _products = products

def set_locations(locations):
    """Set the list of locations where inventory can be stored.

    'locations' is a list of (code, description) tuples.
    """
    global _locations
    _locations = locations

def _load_items():
    """Load the inventory items from the file 'items.json'.
    """
    global _items
    if os.path.exists('items.json'):
        with open('items.json', 'r') as f:
            _items = json.load(f)
    else:
        _items = []

def _save_items():
    """Save the inventory items to the file 'items.json'.
    """
    global _items
    with open('items.json', 'w') as f:
        json.dump(_items, f)
    f.close()