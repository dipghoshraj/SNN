# type 1: Single Input single output neural network
# siso output :  y1 = activition(w1 * i1);

def siso(input: float, weight: float):
    '''
    Args:
        input: input value in number.
        weight: input value in number.
    Returns:
            output return in number
    Raises:
        ValueError: datatype error.
    '''

    if not isinstance(input, float) or not isinstance(input, float):
        raise ValueError('input and weight must be float value')
    return (input * weight)
    
