class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
       res = ""
       #ordena por orden alfabetico las palabras 
       # asi puedes tomar solo es ultimo y el primero y si se puede iterar
       #a traves de ellos quiere decir que las palabras de en medio también
       #incluyen las mismas letras que el primero y el ultimo
       # entrada:  ["flower","flow","flight"]
       # ordenado: ['flight', 'flow', 'flower']
       # output: "fl"
       v = sorted(v)
       print(v)
       first = v[0]
       #toma ultimo elemento
       last = v[len(v)-1]
    
        #va a iterar dentro del rango de la longitud de la palabra mas corta
       for i in range(0, min(len(first), len(last))):
           if last[i] != first[i]:
               return res
           else:
               res += first[i]

       return res
