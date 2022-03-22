def find_error(pred_value, expected_value):
    '''    
    Args:
        pred_value: input value in number.
        expected_value: input value in number.
    Returns:
            output return in number
    Raises:
        ValueError: datatype error.
    '''

    if not isinstance(pred_value, float) or not isinstance(expected_value, float):
        raise ValueError('pred_value/expected_value must be float')

    pred_difference = (pred_value - expected_value)
    error = pred_difference * pred_difference

    return error