fruits = "orange", "lemon", "apple", "peach", "plum", "raspberry", "blueberry", "apricot"

cond = True

while cond :

    ch = input(" What is Your favourite fruit ?")
    for fr in fruits :

        if fr == ch :
          cond = False

   # if cond == False :
    #    break
else    :

    print(" That is my favourite fruit also ! ")


