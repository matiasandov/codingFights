class Solution:
    def partitionString(self, s: str) -> int:
        temp = set()
       #siempre al menos habra 1 y puede sobrar uno al final siempre porque si tenemos "aba" se detiene en en 3ra
        res = 1
        for i in s:
            if i in temp:
                res += 1
                temp = set()
            temp.add(i)
        return res