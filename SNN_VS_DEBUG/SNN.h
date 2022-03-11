#pragma once
#ifndef _SNN_H
#define _SNN_H
double SISO(double input, double weight);
void SIMO(double* weight, double input, double* output_vector, int LABLES_COUNT);
double MISO(double* weight, double* input, int LEN);
#endif // !_SISO_H

