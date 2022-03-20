from .siso import algo_siso
from .simo import algo_simo

def siso(input, weight):
    return algo_siso(input, weight)

def simo(input, weight):
    return algo_simo(input, weight)