def check():
    if (a < 0):
        print('invalid number')
        exit()

    return 0


def car():
    if (a <= b):
        c = b - a
    else:
        print('invalid source')
        exit()
    return 0


def mini():
    print('mini per km is 10rs your {} km is {}'.format(c, 10 * c))
    return 0


def micro():
    print('micro per km is 30rs your {} km is {}'.format(c, 30 * c))
    return 0


def prime():
    print('prime per km is 50rs your {} km is {}'.format(c, 50 * c))
    return 0


def sel():
    if (d == 1):
        mini()
    elif (d == 2):
        micro()
    elif (d == 3):
        prime()
    else:
        print('invalid enter again')


a = int(input("enter the source in km:"))
b = int(input("enter the destination in km:"))
check()
y = True
n = False
c = b - a
car()
print('your km is :', c)
print('1.mini,2.micro,3.prime')
d = int(input("select car:"))

while input('do you want countinue say (y/n):') != 'n':
    sel()
    break
while input('do you wish another ride (y/n)') != 'n':
    a = int(input("enter the source:"))
    b = int(input("enter the destinastion:"))
    check()
    car()
    print('1.mini,2.micro,3.prime')
    d = int(input("select car:"))
    sel()
