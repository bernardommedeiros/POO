#include <iostream>
#include <iomanip>
using namespace std;

class Triangulo {
    public 
    double b = 0, h = 0
    double calc_area(){
        return b * h / 2
    }
}

int main() {
    Triangulo = x; //variavel não precisa ser instanciada, exemplo em java que necessita ser instanciada Triangulo x = new Triangulo()
    cout << x.b << " " << x.h << endl;
    cout << "informe o valor da base:";
    cin >> x.b
    cout <<"informe o valor da altura:"
    cin >> x.h;
    cout << fixed << setprecision(2);
    cout << "Área =" << x.calc_area() << endl;
}