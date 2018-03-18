import numpy as np
import random

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

        # Randomized the matrix
        self.W2 = randomizedMatrix(self.W2, -0.2, 0.2)
        self.W1 = randomizedMatrix(self.W1, -0.2, 0.2)

        # Regularization Loss matrix
        self.regLoss2 = matrix(self.hl, self.out)
        self.regLoss1 = matrix(self.input, self.hl)

    def forward(self, inputs):




# Create matrix for given IxJ
def matrix(I,J):
    m = []
    for i in range(I):
        m.append([0.0]*J)
    return m
# Randomized matrix function
def randomizedMatrix(M, min, max):
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = random.uniform(min, max)
    return  M