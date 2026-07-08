from inventory import inventory
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    return sum(item["quantity"] * item["price"] for item in items)


def main():
    print("===== Inventory Management System =====\n")

    print("Inventory Items:")
    for item in inventory:
        print(
            f"{item['item_name']} | Quantity: {item['quantity']} | Price: ${item['price']:.2f}"
        )

    print(f"\nTotal Stock Value: ${total_stock_value(inventory):.2f}")

    highest = highest_stock_item(inventory)
    lowest = lowest_stock_item(inventory)

    print(f"\nHighest Stock Item: {highest['item_name']} ({highest['quantity']})")
    print(f"Lowest Stock Item: {lowest['item_name']} ({lowest['quantity']})")


if __name__ == "__main__":
    main()