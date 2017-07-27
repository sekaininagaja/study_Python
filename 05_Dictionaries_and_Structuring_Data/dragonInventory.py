dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

# dragon_loot のアイテムがinv内に存在するか確認し、存在していたら+1する
def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        item_name = added_items[i]
        item_total = 0
        if item_name in inventory:
            item_total = int(inventory[item_name]) + 1
            inventory[item_name] = item_total         
        else:
            inventory[item_name] = 1
            #inventory.setdefault(item_name, 1)
    i = i+1
    return inventory

def display_inventory(inventory):
    print("Inventry:")
    item_total = 0
    for k, v in inventory.items():
        print(str(inventory[k]) + '  ' + k )
        item_total = item_total + v
    print("Total number if items: " + str(item_total) )

# for debug
#import pdb;pdb.set_trace()

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
