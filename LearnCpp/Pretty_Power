#include <iostream>
#include <cmath>

using std::cout;
using std::cin;

double power(double base, int exponent) {

	double result = 1;
	
	for(int i=0; i < exponent; i++) {
		result = result * base;
	}	
	return result;
}

void print_pow(double base, int exponent) {

	double myPower = power(base, exponent);
	
	cout << "The value of " << base << " to the power of " << exponent << " is " << myPower << "\n";
	
}

int main() {
	
	double base;
	int exponent;
	
	cout << "What is the base? \n";
	cin >> base;
	cout << "What is the exponent? \n";
	cin >> exponent;
	
	print_pow(base, exponent);
	print_pow(2, 5);
}
