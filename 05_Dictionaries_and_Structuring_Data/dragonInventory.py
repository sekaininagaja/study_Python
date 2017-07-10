def displayInventory(inventory):
    print("Inventry:")
    item_total = 0
    for k, v in inventory.items():
        print(str(stuff[k]) + '  ' + k )
        item_total = item_total + v
    print("Total number if items: " + str(item_total) )

def addToInventory(inventory, add):
    item_total = 0
    # dragonLoot のアイテムがinv内に存在するか確認
    for i in range(len(dragonLoot)):
        item_total = item_total + i.get(add, 0)
    return item_total

inv = {'gorl coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gord coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
