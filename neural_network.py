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
    model.add(Dense(units=3, input_dim=16, activation='sigmoid'))
    #Hidden layer
    model.add(Dense(units=32, activation='sigmoid'))
    #Output layer
    model.add(Dense(units=4, activation='sigmoid'))
    #Compiling model
    model.compile(loss=losses.mean_squared_error, optimizer='RMSprop')
    
    return model

def nn_train(model, state):
    alpha = 0.001
    highest_prediction = nn_predict(model)
    gamma = highest_prediction / 3

    state = data
    Qvalue = highest_prediction + alpha * (reward + gamma + nn_predict(model, state))

    #Train the model with one iteration and input (state)
    model.fit(state, reward_value, epochs=1, verbose=0)

    return model

def nn_predict(model, state):
    #Make new prediction
    prediction = model.predict(state)
    highest_prediction = np.amax(prediction)
    #take highest value from prediction
    #calculate q value
    #highest prediction + alpha (0.001) * (reward + gamma * new prediction)
    #first high gamma, doesn't work so good on long term as low
    
    #take prediction with previous state, calculate reward

    #take action, return only it. put above to train. nn_predict only for saving previous values.
    
    #rules over here!
    
    return (highest_prediction)

def dummy_data():
    dummy = np.random.random_sample((4,0))
    
    return dummy

def data(sensor1, sensor2, sensor3, sensor4):
    sensor1 = 1
    sensor2 = 2
    sensor3 = 3
    sensor4 = 4

    state = [sensor1,
             sensor2,
             sensor3,
             sensor4]
    #change states to 0-1, no higher values allowed
    return state
main()

#reward also -1   0    1
