import sys
sys.path.append('E:/deep_learning_algo_version_1')
from common.hlayer.hlayer import hidden_layer_predictions

def hidden_layer_test_success():
    """
    """

    input = [10, 15, 22]
    input_weight = [
        [1.0, 2.0, 3.0],
        [1.0, 2.5, 3.1],
        [1.9, 2.1, 3.0],
        [1.3, 2.0, 3.3],
    ]
    hiddenlayer_weight =[
        [1.2, 2.0, 3.1, 3.2],
        [1.1, 2.0, 3.2, 3.8],
        [1.7, 2.5, 3.6, 3.2],
    ]

    h_layer = hidden_layer_predictions(input, input_weight, hiddenlayer_weight)
    print(h_layer)


if __name__ == '__main__':
    hidden_layer_test_success()