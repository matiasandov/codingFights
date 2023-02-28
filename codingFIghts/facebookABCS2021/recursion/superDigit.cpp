using namespace std;
#include <iterator>
#include <set>
#include <sstream>
#include <stdio.h>
#include <algorithm>


int superDigit(string n, int k) {
    //si es un solo digito lo regresas
    if(n.size() == 1) return stoi(n);

    long super = 0;
    //para cada caracter
    for (char& c : n) 
        //lo sumas
        super += c - 48;//48 is 0 in ASCII
    
    super *= k;
    //lo pasas multiplicado por uno no mas
    return superDigit(to_string(super), 1);
}