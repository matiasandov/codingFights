#usare un diccionario para usar los valores como keys como en el de anagram y en cada value irá su ocurrencia
#se devolverá el par cuyo value sea 1
# no pude con lo del diccionario
def find_unique(haystack):
    # Write your code here

    #de toda la lista checas elemento por elemento, cuantas veces aparece, si solo aparece una vez, lo guardas en unique 
    unique =[i for i in haystack if haystack.count(i)==1]
    #como devulves una lista, sacas el primer elemento y lo regresas
    return unique.pop()

def unique(word):
    
    for i in word:
        unique = word.count(i)
        if unique >1:
            return False
        
    return True
        
print(unique("abc"))