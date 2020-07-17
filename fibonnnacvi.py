user=int(input('Enter a number and i will make the fibonacci sequance go that many times:'))
a=0
b=1
point=0
if user < 0:
    print('It should have ben positive but your sequence is:')
    while point < user:
        print ('-',a)
        nt=a+b
        a = b
        b = nt
        point += 1
elif user == 1:
    print('Anything over 1 please')
elif user == 0:
    print('There would not be a sequence if it had 0 positions')
else:
    print('Your sequence is:')
    while point < user:
        print (a)
        nt=a+b
        a = b
        b = nt
        point += 1
