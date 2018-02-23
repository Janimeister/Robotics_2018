from keras.models import Sequential
from keras.layers import Dense
from keras import losses
import numpy as np

def main():

    model = Sequential()
    # Input layer
    model.add(Dense(units=4, activation='relu'))
    #Hidden layer
    model.add(Dense(units=8, activation='relu'))
    #Output layer
    model.add(Dense(units=4, activation='linear'))

    #Model used for training
    model.compile(loss=losses.mean_squared_error, optimizer='RMSprop')

    data = np.random.random((100, 100))

    model.fit(data, epochs=100, batch_size=32)    
    

main()
