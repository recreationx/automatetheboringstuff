# from fantasy_game_inventory import displayInventory


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


def addToInventory(inventory: dict, addedItems: list):
    """
    Add items to the inventory.

    Args:
        inventory (dict): The inventory to be added to.

    Returns:
        dict: The updated inventory.
    """
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
