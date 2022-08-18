import  random
passw=''
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
length=3
exit=[]
f=open("res.txt","w")
for i in range(3*10**6):
    passw=''
    for i in range(length):
        passw+=random.choice(letters)
    if passw not in exit:
        exit.append(passw)
        f.write(passw)
        f.write("\n")
f.close()
print(len(exit))