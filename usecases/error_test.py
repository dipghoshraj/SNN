import sys
sys.path.append('E:/deep_learning_algo_version_1')
from common.error.error import find_error

def find_error_tets_succeeded():
    
    pred_value, expected_value= 2.0, 4.2
    error = find_error(pred_value, expected_value)
    print(error)


if __name__ == '__main__':
    find_error_tets_succeeded()