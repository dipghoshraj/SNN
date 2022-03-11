#include "SNN.h"

int weighted_sum(double* weight, double* input, int LEN) {
	double output = 0;
	for (int i = 0; i < LEN; i++) {
		output += weight[i] * input[i];
	}
	return output;
}

double MISO(double* weight, double* input, int LEN) {
	double prediction = 0;
	prediction = weighted_sum(weight, input, LEN);
	return prediction;
}