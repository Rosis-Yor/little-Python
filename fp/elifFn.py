name = input("Enter Your name : ")

nameLen = len(name)

if nameLen < 4 :
    print(" Your name is less than 4 characters")

elif nameLen < 10 :
    print(" Your name is at least 4 characters and less than 10")

else :
    print(" Your name is very long ")