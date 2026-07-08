def highest_stock_item(inventory):
    return max(inventory, key=lambda item: item["quantity"])


def lowest_stock_item(inventory):
    return min(inventory, key=lambda item: item["quantity"])