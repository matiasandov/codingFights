/**
 * @param {string} s
 * @return {string}
 */



var longestPalindrome = function(s) {
    //caso 0
    if (s.length < 1){
        return ""
    }

    //len
    let len = s.length;
    //inicio de palindromo maximo
    let start = 0;
    //len max
    let maxLen = 1;

    //inicio de la iteracion actual
    let low = 0;
    //fin de la iteracion actual
    let high = 0;

    for(let i = 1; i < len; i++){


        //-----caso par------
        low = i-1;
        high = i;

        while(low >= 0 && high < len && s[low] == s[high]){
            low = low - 1;
            high = high +1;
        }

        //una vez que acabe el loop regresas a posiciones anteriores
            low = low + 1;
            high = high - 1;

        //actualizas maxLen si es mayor
        if( high-low+1 > maxLen && s[high]==s[low] ){
            maxLen = high-low+1;
            start = low;
        }

        //---------------------------------
        //caso impar: la unica diferencia es como inicializas low y high ya que i ira en medio y high and low seran espejos
        low = i-1;
        high = i+1;



         while(low >= 0 && high < len && s[low] == s[high]){
            low = low - 1;
            high = high +1;
        }

        //una vez que acabe el loop regresas a posiciones anteriores
            low = low + 1;
            high = high - 1;

        //actualizas maxLen si es mayor
        if( high-low+1 > maxLen && s[high]==s[low] ){
            maxLen = high-low+1;
            start = low;
        }



    }

    return s.slice(start, start + maxLen);




    
    
};
