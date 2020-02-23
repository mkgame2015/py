inventory = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby','Mi']

def addToInventory(inv,loot):
    for i in loot:
        if i in inv.keys():
            inv[i] += 1
        else:
            inv.setdefault(i,1) 
    return inv 

addToInventory(inventory,dragonLoot)


def displayInventory(inv):
    print('Inventory :')
    sum = 0
    for i,v in inv.items():
        print(str(v) +' ' +i)
        sum = sum+v
    print('Total number of items:'+str(sum))

displayInventory(inventory)


