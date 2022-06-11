def displayInventory(inventory: dict):
    """
    Display the inventory in a formatted list.

    Args:
        inventory (dict): The inventory to be displayed.

    Returns:
        None
    """
    print("Inventory:")
    for k, v in inventory.items():
        print(f"{v} {k}")
    print("Total number of items:", sum(inventory.values()))


stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
displayInventory(stuff)
