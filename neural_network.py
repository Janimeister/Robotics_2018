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
        model = nn_train_dummy(model, dummy_state)

#Initializing the neural network, its layer, activation functions and optimizer
def nn_initialize():

    #Defining model
    model = Sequential()
    
    # Input layer
    model.add(Dense(units=4, input_dim=4, activation='sigmoid'))
    
    #Hidden layer
    model.add(Dense(units=32, activation='sigmoid'))
    
    #Output layer
    model.add(Dense(units=4, activation='sigmoid'))
    
    #Compiling model
    model.compile(loss=losses.mean_squared_error, optimizer='RMSprop')
    
    return model

#Training with the dummy data, gets model and state as input, returns trained model
def nn_train_dummy(model, state):

    #Learningrate
    alpha = 0.001
    
    #Highest prediction from nn_predict()
    highest_prediction = nn_predict(model)
    
    #Gamma value, calculated from the highest prediction
    gamma = highest_prediction / 3

    #Getting state from the data
    state = dummy_data()
    
    #Calculating the Q-value
    Qvalue = highest_prediction + alpha * (reward + gamma + nn_predict(model, state))

    #Train the model with one iteration and input (state)
    model.fit(state, Qvalue, epochs=1, verbose=0)

    return model

#Training with the actual sensor data, gets model and state as input, returns trained model
def nn_train_sensor(model, state):

    #Learningrate
    alpha = 0.001
    
    #Highest prediction from nn_predict()
    highest_prediction = nn_predict(model)
    
    #Gamma value, calculated from the highest prediction
    gamma = highest_prediction / 3

    #Getting state from the sensor data
    state = data(sensor1, sensor2, sensor3, sensor4)
    
    #Calculating the Q-value
    Qvalue = highest_prediction + alpha * (reward + gamma + nn_predict(model, state))

    #Train the model with one iteration and input (state)
    model.fit(state, Qvalue, epochs=1, verbose=0)

    return model

#Prediction making, gets model and state as input, returns highes prediction among the values
def nn_predict(model, state):
    
    #Make new prediction
    prediction = model.predict(state)

    #Defining the highest prediction
    highest_prediction = np.amax(prediction)
    
    #take highest value from prediction
    #calculate q value
    #highest prediction + alpha (0.001) * (reward + gamma * new prediction)
    #first high gamma, doesn't work so good on long term as low
    
    #take prediction with previous state, calculate reward

    #take action, return only it. put above to train. nn_predict only for saving previous values.
    
    #rules over here!
    
    return (highest_prediction)

#Creating dummy training data
def dummy_data():
    dummy = np.random.random_sample((4,0))
    
    return dummy

#Training data from sensors, communication needed between this and Arduino
def data(sensor1, sensor2, sensor3, sensor4):
    sensor1 = 1
    sensor2 = 2
    sensor3 = 3
    sensor4 = 4

    state = [sensor1,
             sensor2,
             sensor3,
             sensor4]
    
    #change states to 0-1, no higher values allowed due to sigmoid-fucntion
    return state
main()

#reward also -1   0    1
