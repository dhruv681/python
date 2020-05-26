num= list(input('type random amount of letters and words and i will put out the numbers:'))

numb=[]
bumb=[]
for word in num:
    if word.isdigit():
        numb.append(int(word))
    else:bumb.append(word)

print(numb,bumb)
