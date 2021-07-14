# This module implements the report-generation logic for the InventoryControl
# system.

import datastorage

def generate_inventory_report():
    """
    Generates a report of all the items in the inventory.
    """
    # Get all the items in the inventory.
    product_names = {} # Dictionary of product names and codes.
    for product_code, name, desired_number in datastorage.products():
        product_names[product_code] = name
    
    location_names = {} # Dictionary of location names and codes.
    for location_code, name in datastorage.locations():
        location_names[location_code] = name

    
    # Calculate the total number of items in the inventory.
    grouped_items = {} # Dictionary of product names and the number of items.
    for product_code, location_code in datastorage.items():
        if product_code not in grouped_items:
            grouped_items[product_code] = {}
        
        if location_code not in grouped_items[product_code]:
            grouped_items[product_code][location_code] = 1
        else:
            grouped_items[product_code][location_code] += 1

    # Create the report.
    report = []
    report.append("Inventory Report")
    report.append("")

    for product_code in sorted(grouped_items.keys()):
        product_name = product_names[product_code]
        report.append("{0}:".format(product_name))
        for location_code in sorted(grouped_items[product_code].keys()):
            location_name = location_names[location_code]
            report.append("  {0}: {1}".format(location_name, grouped_items[product_code][location_code]))
        report.append("")
    
    return report