import sys
sys.path.append('E:/deep_learning_algo_version_1')
from algo import mimo

def succeess_test_miso():
    '''
    successfull test for the miso algo
    '''

    input, weight = [2.0, 3.0], [[7.8, 2.3], [1.0, 1.3]]
    siso_output  = mimo(input, weight)
    print(siso_output)


def fails_test_miso():
    '''
    failed test for the miso algo
    '''
    input, weight = 4.1, [1.0, 1.3, 2.0]
    siso_output  = mimo(input, weight)
    print(siso_output)


if __name__ == '__main__':
    succeess_test_miso()