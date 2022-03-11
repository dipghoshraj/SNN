#include <stdio.h>
#include <stdlib.h>

#include "SNN.h"
#include "test_SNN.h"


double temprature[] = { 12, 34, 23, 45 };
double humidity[] = { 10, 45, 46, 23 };
double air_quality[] = { 24, 46, 34, 97 };

double weight_MISO[] = { 2,2,3 };
int LEN = 4;
int FEATURE = 3;

double test_MISO() {

	for (int i = 0; i <= LEN; i++) {
		double train_ex[] = { temprature[i], humidity[i], air_quality[i] };
		printf("Prediction value %f \r\n", MISO(train_ex, weight_MISO, FEATURE));
	}
}