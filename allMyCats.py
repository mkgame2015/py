catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1)+'(or enter nothing to stop.):' )
    name = input()
    if name == '':
        break
    catNames = catNames + [name]

print('The cat names ars:')
for name in catNames:
    print(' '+name)