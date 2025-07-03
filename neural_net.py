from custom_nn import Layer, Activation_ReLU, Activation_Softmax
import numpy as np

class CustomFlappyNet:
    def __init__(self):
        self.layer1 = Layer(4, 6)  # 4 inputs → 6 hidden
        self.act1 = Activation_ReLU()
        self.layer2 = Layer(6, 2)  # 6 hidden → 2 outputs
        self.softmax = Activation_Softmax()

    def forward(self, x):
        self.layer1.forward(x)
        self.act1.forward(self.layer1.output)
        self.layer2.forward(self.act1.output)
        self.softmax.forward(self.layer2.output)
        return self.softmax.output

    def get_weights(self):
        return {
            'l1_w': self.layer1.weights.copy(),
            'l1_b': self.layer1.biases.copy(),
            'l2_w': self.layer2.weights.copy(),
            'l2_b': self.layer2.biases.copy()
        }

    def set_weights(self, weights):
        self.layer1.weights = weights['l1_w']
        self.layer1.biases = weights['l1_b']
        self.layer2.weights = weights['l2_w']
        self.layer2.biases = weights['l2_b']