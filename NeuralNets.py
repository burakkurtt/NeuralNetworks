import numpy as np

class neuralNets:
    def __init__(self, inputNumber, hiddenLayer, outputNumber):
        self.input = inputNumber
        self.hl = hiddenLayer
        self.out = outputNumber
        # initialize the activation values
        self.actIn = []
        self.actHidden = []
        self.actOut = []
        self.actIn = [1.0]*self.input
        self.actHidden = [1.0]*self.hl
        self.actOut = [1.0]*self.outs

        # Initialize the output weights
        self.W2 = matrix(self.hl, self.out)
        #Initilize the hidden layer weights
        self.W1 = matrix(self.input, self.hl)








# Create matrix for given IxJ
def matrix(I,J):
    m = []
    for i in range(I):
        m.append([0.0]*J)
    return m
