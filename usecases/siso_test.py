import sys, os
path = os.path.abspath(__file__ + "/../../")
sys.path.append(path)

sys.path.append('E:/deep_learning_algo_version_1')
from algo.siso.siso import siso
def succeess_test_siso():
    '''
    successfull test for the siso algo
    '''

    input, weight =  2.3, 7.8
    siso_output  = siso(input, weight)
    print(siso_output)


def fails_test_siso():
    '''
    failed test for the siso algo
    '''
    input, weight = 3, 4
    siso_output  = siso(input, weight)
    print(siso_output)


if __name__ == '__main__':
    succeess_test_siso()