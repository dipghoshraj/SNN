from .siso import algo_siso
from .simo import algo_simo
from .miso import algo_miso
from .mimo import algo_mimo

def siso(input: float, weight: float):
    return algo_siso(input, weight)

def simo(input: float, weight: list):
    return algo_simo(input, weight)

def miso(input: list, weight: list):
    return algo_miso(input, weight)

def mimo(input: list, weight: list):
    return algo_mimo(input, weight)