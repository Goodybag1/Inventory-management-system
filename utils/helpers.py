def highest_stock_item(inventory):
    """Returns the inventory item with the highest quantity."""
    return max(inventory, key=lambda item: item["quantity"])


def lowest_stock_item(inventory):
    """Returns the inventory item with the lowest quantity."""
    return min(inventory, key=lambda item: item["quantity"])


def average_item_price(inventory):
    """Returns the average price of all inventory items."""
    if not inventory:
        return 0

    total = sum(item["price"] for item in inventory)
    return total / len(inventory)