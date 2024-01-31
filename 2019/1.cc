#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int calc_fuel(int mass) { return (mass / 3) - 2; }

int calc_all_fuel(std::string filepath) {
  ifstream in(filepath);

  std::string str;
  int total_fuel = 0;
  while (std::getline(in, str)) {
    int mass = std::stoi(str);
    int fuel = calc_fuel(mass);
    cout << "Mass: " << mass << "\tFuel: " << fuel << std::endl;
    total_fuel += fuel;
  }
  return total_fuel;
}

int main() {
  int total_fuel = calc_all_fuel("1_input.txt");
  cout << "Total fuel: " << total_fuel << std::endl;

  return 0;
}
