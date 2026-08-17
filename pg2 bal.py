#Swetha
#minimum balance
def minbal(b):
    m=1000
    penalty=50
    print('current balance',b)
    if b<m:
        b+=penalty
        print('balance',m,'penalty of',penalty,'is applied')
        print('new balance',b)
    else:
        print('no need of penalty')
    return b
bal=int(input('enter ur balance;'))
r=minbal(bal)
