def longest_common_prefix(strs):
    #prefix no puede iniciar vacio nunca
    prefix = strs[0]
    count = 0
    #found = 0
    
    #for que recorre lista, no incluye la ultima posicion para que al comparar no se salga del rango
    for i in range(0, len(strs)-1):
        tempPrefix = ""
        found = 0
        
        #for que recorre caracteres las palabras, elegira la length de la palabra mas corta para no salirse del rango
        #se evalua que haya un string "" porque podria afectar en la comparacion
        leng = min( len(strs[i]), len(strs[i+1]) )
        if leng == 0:
            return ""
        else:
            for j in range(leng):
                
                #si siguen siendo iguales los caracteres, se iran acumulando
                if strs[i][j] == strs[i+1][j] and found == 0 :
                    tempPrefix += strs[i][j]
                    count += 1
                    
                #si son distintos, se evalua si jamas son iguales o si el prefijo actual esta dentro
                else:
                    
                    
                    if count == 0:
                        return ""
                        
                    
                    
                    elif count != 0 and tempPrefix in prefix and len(tempPrefix) <= len(prefix):
                        prefix = tempPrefix
                        #si ya se encontro un prefijo y el caracter actual es distinto, se pone bandera para que deje de aumentar caracteres a tempPrefix en el primer if de arriba
                        found += 1
                        


                        #break
            found = 0
            count = 0 
                            

                #esto debe ser en cada iteracion que se actualice
            if tempPrefix in prefix and len(tempPrefix) <= len(prefix):
                prefix = tempPrefix

    return prefix
                
a = ['flower','flow','flight']
pre = longest_common_prefix(a)
print('final : ', pre)