from keras.models import Sequential
from keras.layers import Dense
from keras import losses
import numpy as np
import random

def main():
    
    model = Sequential()
    # Input layer
    model.add(Dense(units=4, input_dim = 100, activation='relu'))
    #Hidden layer
    model.add(Dense(units=8, activation='relu'))
    #Output layer
    model.add(Dense(units=4, activation='linear'))

    #Model used for training
    model.compile(loss=losses.mean_squared_error, optimizer='RMSprop')

    data = np.random.random((100, 100))
    labels = np.random.randint(10, size=(100, 4))


    model.fit(data, labels, epochs=100)

    #Eteen, Taakse, Oikea, Vasen
    dummydata = [[10],
                 [5],
                 [7.5],
                 [4]]


    



main()
