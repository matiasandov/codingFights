"""
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Excepciones 
"""



class Solution:
    #la mejor
    def intToRoman(self, num: int) -> str:
        M=["","M","MM","MMM"]
        C=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        X=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        I=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        
        return M[num//1000]+C[num%1000//100]+X[num%1000%100//10]+I[num%1000%100%10]
    
    
    
    
    
    
    
    
#mi solucion 
    def romanToInt(self, s):
            """
            :type s: str
            :rtype: int
            """
            
            dicc = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L":50,
                "C":100,
                "D": 500,
                "M": 1000,
            }
            #SPACE COMP N**2 
            dicc2 = {
                "I": {"X": 9, "V": 4},
                "X": {"C": 90, "L": 40},
                "C": {"M": 900, "D": 400}
            }

            i = 0
            size = len(s)
            sum = 0

            #The KeyError: 'I' error occurs because the code is trying to access a key in dicc2 that does not exist. 
            while i < size :
                if s[i] in dicc2 and i+1 < size:
                    if s[i+1] in dicc2[s[i]]:
                        digit = dicc2[s[i]][s[i+1]]
                        sum += digit
                        #skip pair
                        i = i+2
                    #sin este else te quedas en un loop infinito!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    else:
                        sum += dicc[s[i]]
                        i += 1
                else:
                    sum += dicc[s[i]]
                    i += 1
            
            return sum
