"""
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""



class Solution:
    def intToRoman(self, num: int) -> str:
        M=["","M","MM","MMM"]
        C=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        X=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        I=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        return M[num//1000]+C[num%1000//100]+X[num%1000%100//10]+I[num%1000%100%10]
