import sys


def manage_inventory():
    print("=== Inventory System Analysis ===")

    inventory = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, qty_str = arg.split(":", 1)

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity = int(qty_str)
            inventory[name] = quantity
        except ValueError:
            print(f"Quantity error for '{name}': "
                  f"invalid literal for int(): '{qty_str}'")

    if not inventory:
        print("Inventory is empty.")
        return

    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item, qty in inventory.items():
        percentage = (qty / total_qty) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")

    most_abundant = item_list[0]
    least_abundant = item_list[0]

    for item in item_list:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant} "
          f"with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} "
          f"with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    manage_inventory()
