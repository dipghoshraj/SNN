
import sys
sys.path.append('E:/deep_learning_algo_version_1')
from algo import simo

def succeess_test_siso():
    '''
    successfull test for the siso algo
    '''

    input, weight =  2.3, [7.8, 2.3, 4.1]
    siso_output  = simo(weight, input)
    print(siso_output)


def fails_test_siso():
    '''
    failed test for the siso algo
    '''
    input, weight = 3, 5
    siso_output  = simo(weight, input)
    print(siso_output)


if __name__ == '__main__':
    succeess_test_siso()