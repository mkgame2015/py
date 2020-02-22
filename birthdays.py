birthdays = {'Tom':'Apr 1','Mi':'Dec 12','Carol':'Mar 4'}
while True:
    print('Enter your name:(blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + 'is the birthday of ' + name )
    else:
        print('I do not  have birthday information for ' + name)
        print('What is their birthday ?')
        bday = input()
        birthdays[name] = bday
        print('birthday database updated')
