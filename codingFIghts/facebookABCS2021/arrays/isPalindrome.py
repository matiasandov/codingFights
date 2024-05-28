
#checar cual es la mejor manera de checar si es anagram
#manipularlo como una string
def isPalindrome(self,x):

        s = str(x)
        #checar si es negativo o divisible entre 10 exacto con residuo de 0 ejemplo 10, 20, 30, nunca seran palindromos
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        #checar si es 1 solo digito
        elif len(s) == 1:
                return True

        #reverse only the half and compare to the other half
        else:
            reversedHalf = ""
            secondHalf = ""
            #inicio SI INCLUIDO, final NO INCLUIDO, STEP

            #par 
            mid = len(s)//2

            if len(s) % 2 == 0:
                secondHalf = s[mid:len(s)]
            else:
                secondHalf = s[mid+1: len(s)]


            for i in range(len(secondHalf) -1 , -1, -1):
               
                reversedHalf+=secondHalf[i]
                
            if reversedHalf == s[0:mid]:
                return True
            else:
                False

        return False


