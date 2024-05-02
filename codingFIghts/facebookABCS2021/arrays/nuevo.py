def isPalindrome( x):
    # Check for negative numbers and numbers ending with 0
    # ex -10 or 10 en automatico no son
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        
        print("------")
        
        # #agregas ultima unidad
        # print(f" {x} % 10:", x % 10)
        # print("+")
        # print("reversed_half * 10:", reversed_half * 10)
        # print("=")
        
        #con el residuo de entre 10 ultima unidad y lo que tenias le agregas un cero = multiplo de 10 + 1
        reversed_half = reversed_half * 10 + x % 10
        print("reversed_half: ", reversed_half)
        
        
        #quitas ultima unidad de x
        x //= 10
        print("x: ", x)
    
        

    # If the length of x is odd, we need to eliminate the middle digit
    # by dividing reversed_half by 10.
    return x == reversed_half or x == reversed_half // 10

print(isPalindrome(12321))