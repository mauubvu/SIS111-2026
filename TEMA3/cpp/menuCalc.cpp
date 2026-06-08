#include <iostream>
#include <vector>
#include <string>
using namespace std;

void mostrarMenu() {
    cout << "\n---MENU---\n"
         << "(1) Sumar\n"
         << "(2) Restar\n"
         << "(3) Multiplicar\n"
         << "(4) Dividir\n"
         << "(5) Salir\n";
}

vector<double> pedirNumeros() {
    cout << "ENTER vacío para terminar\n";
    vector<double> nums;
    string linea;
    while (true) {
        cout << "Número: ";
        getline(cin, linea);
        if (linea.empty()) break;
        try {
            nums.push_back(stod(linea));
        } catch (...) {
            cout << "Entrada inválida.\n";
        }
    }
    return nums;
}

double sumar(vector<double>& nums) {
    double res = 0;
    for (double n : nums) res += n;
    return res;
}

double restar(vector<double>& nums) {
    double res = nums[0];
    for (int i = 1; i < nums.size(); i++)
        res -= nums[i];
    return res;
}

double multiplicar(vector<double>& nums) {
    double res = 1;
    for (double n : nums) res *= n;
    return res;
}

bool dividir(vector<double>& nums, double& res) {
    res = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == 0) return false;
        res /= nums[i];
    }
    return true;
}

int main() {
    string opcion;
    while (true) {
        mostrarMenu();
        cout << "Opción: ";
        getline(cin, opcion);
        if (opcion == "5") break;
        if (opcion != "1" && opcion != "2" &&
            opcion != "3" && opcion != "4") {
            cout << "Inválida.\n"; continue;
        }
        auto nums = pedirNumeros();
        if (nums.size() < 2) {
            cout << "Mínimo 2 números.\n"; continue;
        }
        double res;
        if (opcion == "1")
            cout << "Suma: " << sumar(nums) << "\n";
        else if (opcion == "2")
            cout << "Resta: " << restar(nums) << "\n";
        else if (opcion == "3")
            cout << "Multiplicación: "
                 << multiplicar(nums) << "\n";
        else if (opcion == "4") {
            if (!dividir(nums, res))
                cout << "No definida (div/0).\n";
            else cout << "División: " << res << "\n";
        }
    }
    return 0;
}