import random
passwordlength=int(input("enter the length of password: "))
list=[]
password=''
if(passwordlength<6):
    print("password should have atleast 6 characters")
    flag=False
elif(passwordlength>=6):
    for i in range(33,119):
        list.append(chr(i))
        flag=True
while(flag):
    randomCharacter = random.choice(list)
    if(len(password) is passwordlength):
        break
    elif (randomCharacter not in password):
         password = password + (randomCharacter)
    else:
        continue
else:
 print("thank you")
print(password)
