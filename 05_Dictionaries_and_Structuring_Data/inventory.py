stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventry:")
    item_total = 0
    for k, v in inventory.items():
        print(str(stuff[k]) + '  ' + k )
        item_total = item_total + v
    print("Total number if items: " + str(item_total) )

displayInventory(stuff)
