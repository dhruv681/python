num= list(input('type random amount of letters and words and i will put out the numbers:'))

numb=[]
for word in num:
    if word.isdigit():
        numb.append(int(word))
print('so your numbers are ',numb)

