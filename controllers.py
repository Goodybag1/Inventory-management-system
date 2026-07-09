from database import get_inventory
from utils.helpers import (
    highest_stock_item,
    lowest_stock_item,
    average_item_price,
)


def total_stock_value(items):
    """Calculates the total stock value."""
    if not items:
        return 0

    return sum(item["quantity"] * item["price"] for item in items)


def display_inventory():
    """Displays inventory information."""
    inventory = get_inventory()

    print("===== Inventory Management System =====\n")

    print("Inventory Items:")
    print("-" * 50)
    print(f"{'Item':<15}{'Quantity':<15}{'Price'}")
    print("-" * 50)

    for item in inventory:
        print(f"{item['item_name']:<15}{item['quantity']:<15}${item['price']:.2f}")

    print("-" * 50)

    print(f"\nTotal Stock Value: ${total_stock_value(inventory):.2f}")
    print(f"Average Item Price: ${average_item_price(inventory):.2f}")

    highest = highest_stock_item(inventory)
    lowest = lowest_stock_item(inventory)

    print(f"\nHighest Stock Item: {highest['item_name']} ({highest['quantity']})")
    print(f"Lowest Stock Item: {lowest['item_name']} ({lowest['quantity']})")