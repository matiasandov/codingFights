def sum_to_one(digits):
    #----------------?? checar constraints
    if(int(digits) < 10):
        #o maybe tienes que regreaarlo como int()
        #print(digits)
        return int(digits)

    sum = 0
    for i in range (0,len(digits)):
        act = int(digits[i])
        #print('act :', act)
        sum = sum + act
    #!!!!!!!!!!!!necesitas regresar la recursion porque sino el valor se pierde!!!!!!!!!!!!
    return sum_to_one(str(sum))

  

h = sum_to_one("9875")
print(h)