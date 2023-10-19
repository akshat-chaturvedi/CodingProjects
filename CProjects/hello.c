#include <stdio.h>

int main()
{
	double kelvin, celsius;
	int lower, upper, step;

	lower = 0;
	upper = 500;
	step= 25;

	kelvin = lower;
	
	while (kelvin <= upper) {
		celsius = kelvin + 273.15;
		printf("%3.0f\t%6.3f\n", kelvin, celsius);
		kelvin = kelvin + step;
	}
}
