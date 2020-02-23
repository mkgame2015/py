# theBoard = {'top-L':' ','top-M':' ','top-R':' ','Mid-L':' ','Mid-M':' ','Mid-R':' ','low-L':' ','low-M':' ','low-R':' '}

# def printBoard(board):
#     print(theBoard['top-L']+'|'+theBoard['top-M']+'|'+theBoard['top-R'])
#     print('-+-+-')
#     print(theBoard['Mid-L']+'|'+theBoard['Mid-M']+'|'+theBoard['Mid-R'])
#     print('-+-+-')
#     print(theBoard['low-L']+'|'+theBoard['low-M']+'|'+theBoard['low-R'])

# turn = 'x'

# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space ?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'x':
#         turn  = 'o'
#     else:
#         turn = 'x'

# printBoard(theBoard)

##################################################################
# totalBrought()

allGuest = {'Tom':{'apples':5,'prezels':12},
            'Mi':{'ham sandwiches':3,'apples':2},
            'Dav':{'cups':3,'apple pies':1}}

def totalBrought(guest,item):
    numBrought = 0 
    count=0
    for k,v in guest.items():
        if k !='':
            count += 1
            print(count)
        numBrought = numBrought + v.get(item,0)
    return numBrought

print('Apples '+ str(totalBrought(allGuest,'apples')))
           

