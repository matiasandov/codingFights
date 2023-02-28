#include <vector>
using namespace std;
//1 tomar los ultimos d elementos y agregarlos en un vector en la primeras posiciones
//2. tomas los elementos del 0 hasta arr.size()-d y los pones despés de los que ya pusiste

vector<int> rotateLeft(int d, vector<int> arr) {


    vector<int> result;
    //int dCont = 0;
    for (int i = 0; i <= d; i++) {
        result[i] = arr[arr.size() - i];
    }

    //en todo caso  si no funciona, intenta con darle -1 o quitarle el igual
    for (int j = 0; j < (arr.size() - d); j++) {
        result.push_back(arr[j]);
    }

    return result;

}

//1.tomar las primeras de posiciones y ponerlas en otro array y hacerles pop cada vez que las saques

//2. concatenas lo que resta del vector con el vector de las posiciones que borraste
