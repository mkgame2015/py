def collazt(number):
    if number%2==0:
        print(number//2)
        return number//2
    if number%2==1:
        print(3*number+1)
        return 3*number+1

print('Enter nubmer:')

while True:
    try:
        number = int(input())
    except ValueError:
        print('请输入整数')
        continue

    while number!=1:
        number = collazt(number)
    break
