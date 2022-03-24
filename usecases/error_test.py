import sys, os
path = os.path.abspath(__file__ + "/../../")
sys.path.append(path)

from common.error.error import find_error

def find_error_tets_succeeded():
    
    pred_value, expected_value= 2.0, 4.2
    error = find_error(pred_value, expected_value)
    print(error)


if __name__ == '__main__':
    find_error_tets_succeeded()