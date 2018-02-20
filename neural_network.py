from keras.models import Sequential
from keras.layers import Dense
from keras import losses
import numpy as np
import random

def main():
    #Initializing neural network
    model = nn_initialize()
    #Training the neural network with dummy data
    for i in range(500):
        dummy_state = dummy_data()
        model = nn_train(model, dummy_state)

def nn_initialize():
    model = Sequential()
    # Input layer
    model.add(Dense(units=4, input_dim=self.state_size, activation='relu'))
    #Hidden layer
    model.add(Dense(units=8, activation='relu'))
    #Hidden layer
    model.add(Dense(units=8, activation='relu'))
    #Output layer
    model.add(Dense(units=4, activation='sigmoid'))
    #Compiling model
    model.compile(loss=losses.mean_squared_error, optimizer='RMSprop')
    
    return model

def nn_train(model, state):
    #Train the model with one iteration and input (state)
    model.fit(state, reward_value, epochs=1, verbose=0)

    return model

def nn_predict(model):
    #Make new prediction
    prediction = model.predict(state)

    return (model)

def dummy_data():
    dummy = np.random.randint(0,200, size=(4,1))
    
    return dummy

def data(sensor1, sensor2, sensor3, sensor4):
    sensor1 = 1
    sensor2 = 2
    sensor3 = 3
    sensor4 = 4

    state = [[sensor1],
             [sensor2],
             [sensor3],
             [sensor4]]

    return state
main()


