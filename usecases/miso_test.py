import sys, os
path = os.path.abspath(__file__ + "/../../")
sys.path.append(path)

from algo.miso.miso import miso
def succeess_test_miso():
    '''
    successfull test for the miso algo
    '''

    input, weight =  [7.8, 2.3, 4.1], [1.0, 1.3, 2.0]
    siso_output  = miso(input, weight)
    print(siso_output)


def fails_test_miso():
    '''
    failed test for the miso algo
    '''
    input, weight = 4.1, [1.0, 1.3, 2.0]
    siso_output  = miso(input, weight)
    print(siso_output)


if __name__ == '__main__':
    succeess_test_miso()