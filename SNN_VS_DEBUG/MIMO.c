
#include "SNN.h"

int weighted_sum(double* weight, double* input, int LEN) {
	double output = 0;
	for (int i = 0; i < LEN; i++) {
		output += weight[i] * input[i];
	}
	return output;
}

double MIMO(double* input, double* LEN, double* output_vector, int LEN_O, int LEN_I, double weight[LEN_O][LEN_I]) {

	for (int i = 0; i < LEN_O; i++) {
		for (int j = 0; j < LEN_I; j++) {
			output_vector[j] += input[j]*weight[i][j];
		}
	}
}