import numpy as np
import pandas as pd


class NeuralNetwork:
    def __init__(self):
        self.data = pd.read_csv("train.csv")
        self.eps = 0.001
        self.X = np.resize(self.data.iloc[:, 1:].to_numpy(), (self.data.shape[0], 28 * 28))
        self.y = np.resize(self.data.iloc[:, 0].to_numpy(), (self.data.shape[0], 1))
        self.outLayerWidth = 0
        self.recognizedDict = {}
        self.reorganizedY()
        self.weights0 = 2 * np.random.random((28 * 28, 20)) - 1
        self.weights1 = 2 * np.random.random((20, 15)) - 1
        self.weights2 = 2 * np.random.random((15, self.outLayerWidth)) - 1


    def reorganizedY(self):
        uniqueValues = np.unique(self.y)
        countOfBits = int(np.ceil(np.sqrt(len(uniqueValues))))
        changeDict = dict(map(lambda x: [x, str(bin(x))[2:].rjust(countOfBits, "0")], uniqueValues))
        newY = []
        for i in self.y:
            newY.append(list(map(int, changeDict.get(i[0]))))
        self.y = np.array(newY)
        self.outLayerWidth = countOfBits
        self.recognizedDict = dict(map(lambda x: [changeDict.get(x), x], changeDict.keys()))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def learning(self, epochs=1000):
        for i in range(epochs):
            y0_pred = self.sigmoid(np.dot(self.X, self.weights0))
            y1_pred = self.sigmoid(np.dot(y0_pred, self.weights1))
            y2_pred = self.sigmoid(np.dot(y1_pred, self.weights2))


            layer_y2_delta = (y2_pred - self.y) * y2_pred * (1 - y2_pred)
            layer_y1_delta = layer_y2_delta.dot(self.weights2.T) * y1_pred * (1 - y1_pred)
            layer_y0_delta = layer_y1_delta.dot(self.weights1.T) * y0_pred * (1 - y0_pred)

            self.weights2 -= (self.eps * y1_pred.T.dot(layer_y2_delta))
            self.weights1 -= (self.eps * y0_pred.T.dot(layer_y1_delta))
            self.weights0 -= (self.eps * self.X.T.dot(layer_y0_delta))
            print(i)

    def predict(self, x):
        x = np.resize(x, (1, 28 * 28))
        y0_pred = self.sigmoid(np.dot(x, self.weights0))
        y1_pred = self.sigmoid(np.dot(y0_pred, self.weights1))
        y2_pred = list(self.sigmoid(np.dot(y1_pred, self.weights2)).round()[0])
        y2_pred = list(map(int, y2_pred))
        pred = self.recognizedDict.get(''.join(map(str, y2_pred)), "_")

        return str(pred)
