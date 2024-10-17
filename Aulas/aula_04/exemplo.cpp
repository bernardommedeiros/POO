#include <iostream>
using namespace std;


int main() {
    int x = 10; // variavel estatica
    int* y = &x;  // nao guarda um inteiro, e sim um endereço
    cout << x << endl;
    cout << &x << endl;
    cout << y << endl;
    cout << &y << endl;
    cout << *y << endl;
    y = new int(); //variavel dinamica
    cout << y << endl;
    *y = 20;
    cout  << x + (*y) << endl;
    delete y;
}
// cout == print