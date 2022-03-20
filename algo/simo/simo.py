def simo(weights, input):
    '''
    Args:
        input: input value in number.
        weight: input value in array of number.
    Returns:
            output return in array of number.
    Raises:
        ValueError: datatype error.
        ValueError: invalid weights error.
    '''

    if not isinstance(weights, list):
        raise ValueError('weight must be an list of float values')

    output = []

    for _weight in weights:
        if not isinstance(_weight, float) or not isinstance(input, float):
            raise ValueError('input and weight must be float value')
        output.append(input * _weight)
    return output

    