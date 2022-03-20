
from wsgiref.util import request_uri


def mimo(input, weight):
    '''
    Args:
        input: input value in number.
        weight: input value in array of number.
    Returns:
            output return in float.
    Raises:
        ValueError: datatype error.
    '''

    if len(input) != len(weight):
        raise KeyError('input and weight must be the same length')
    
    if not isinstance(input, list) or not isinstance(weight, list):
        raise ValueError('input and weight must be list of number')    
    output = []

    for i in range(len(input)):
        if not isinstance(input[i], float):
            raise ValueError('input must be float')         
        output.append(elementwise_multiply(input, weight[i]))
    
    return output


def elementwise_multiply(input, weight):
    
    if len(input) != len(weight):
        raise KeyError('in elementwise_multiply input and weight must be the same length')

    output = 0
    for i in range(len(input)):
        if not isinstance(input[i], float) or not isinstance(weight[i], float):
            raise ValueError('in elementwise_multiply input and weight must be float')
        output += input[i] * weight[i]

    return output