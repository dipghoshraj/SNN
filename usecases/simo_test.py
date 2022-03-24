import sys, os
path = os.path.abspath(__file__ + "/../../")
sys.path.append(path)

from algo.simo.simo import simo
def succeess_test_simo():
    '''
    successfull test for the simo algo
    '''

    input, weight =  2.3, [7.8, 2.3, 4.1]
    siso_output  = simo(weight, input)
    print(siso_output)


def fails_test_simo():
    '''
    failed test for the simo algo
    '''
    input, weight = 3, 5
    siso_output  = simo(weight, input)
    print(siso_output)

if __name__ == '__main__':
    succeess_test_simo()