
def hidden_layer_predictions(input: list, input_weight:list, hiddenlayer_weight:list):
    '''
    Args:
        input: input value in list.
        input_weight: input value in list.
        hiddenlayer_weight: input value in list.
    Returns:
            output return in number
    Raises:
        ValueError: datatype error.
    '''

    h_layer = hidden_layer(input, input_weight)
    output = []

    for i, _hweight in enumerate(hiddenlayer_weight):
        if not isinstance(input, list) or not isinstance(_hweight, list):
            raise ValueError('input and weight must be list')
        output.append(elementwise_multiply(h_layer, _hweight))
    
    return output

 
def hidden_layer(input, input_weight):
    '''
    Args:
        input: input value in list.
        input_weight: input value in list.
    Returns:
        h_layer return in list
    Raises:
        ValueError: datatype error.
    '''
    
    h_layer = []
    for i, _weight in enumerate(input_weight):
        if not isinstance(input, list) or not isinstance(_weight, list):
            raise ValueError('input and weight must be list')
        h_layer.append(elementwise_multiply(input, _weight))

    return h_layer
        

def elementwise_multiply(input, weight):
    '''
    Args:
        input: input value in list.
        weight: input value in list.
    Returns:
        output return in number
    Raises:
        ValueError: datatype error.
    '''
    output = 0

    for i, _weight in enumerate(weight):
        if not isinstance(input[i], float) or not isinstance(_weight, float):
            raise ValueError('input and weight must be float')
        output += input[i] * _weight
    return output
