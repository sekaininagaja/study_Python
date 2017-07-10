allGuests = {'Allice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    newBrought = 0
    for k, v in guests.items():
        newBrought = newBrought + v.get(item, 0)
    return newBrought

print('Number og things being broughe:')
print(' - Apples          ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups            ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes           ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches  ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies      ' + str(totalBrought(allGuests, 'apple pies')))
