def UrlIFY(word, leng):
    cont = 0
    #word = word.replace(" ","%20")
    res = ""
    for i in word:
        if i == " " and cont < leng:
            res +=  "%20"
            cont = cont +1
        else:
            res +=  i
            cont = cont +1
    return res


word = "Mr Jhon Smith  "
leng = 13

print(UrlIFY(word, leng))