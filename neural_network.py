from keras.models import Sequential
from keras.layers import Dense
from keras import losses
import numpy as np
import random
#import serial
#import time
#import robot.py as rpy

def main():

    #Initializing neural network
    model = nn_initialize()
    
    #Training the neural network with dummy data,
    for i in range(500):
        dummy_state = dummy_data()
        model = nn_train_dummy(model, dummy_state)

#Initializing the neural network, its layer, activation functions and optimizer
def nn_initialize():

    #Test input shape
    #dummy = dummy_data()
    #print(dummy.ndim)
    
    #Defining model
    model = Sequential()
    
    # Input layer
    model.add(Dense(units=4, input_shape=(1,), activation='sigmoid'))
    
    #Hidden layer
    model.add(Dense(units=32, activation='sigmoid'))
    #Output layer
    model.add(Dense(units=4, activation='softmax'))
    
    #Compiling model
    model.compile(loss=losses.categorical_crossentropy, optimizer='RMSprop')
    return model

#Training with the dummy data, gets model and state as input, returns trained model
def nn_train_dummy(model, state):

    #Learningrate
    alpha = 0.001
    #Highest prediction from nn_predict(),
    #THROWS ERROR: Sequential object has no attribute ndim
    #Tried to format input data, but the problem has nothing to do with its dim it seems...
    #highest_prediction = nn_predict(model, state)
    prediction = nn_predict(model, state)
    #Gamma value, calculated from the highest prediction

    #Getting state from the data
    #state = dummy_data()
    highest_prediction = np.amax(prediction)
    gamma = highest_prediction / 3
    reward = 1
    #Calculating the Q-value
    Qvalue = np.amax(prediction) + alpha * (reward + gamma + prediction)
    Qvalue = np.array(Qvalue)
    print(Qvalue.shape)
    #Train the model with one iteration and input (state)
    model.fit(state, Qvalue, epochs=1, verbose=1)

    return model

#Training with the actual sensor data, gets model and state as input, returns trained model
def nn_train_sensor(model, state):

    #Learningrate
    alpha = 0.001
    
    #Highest prediction from nn_predict()
    highest_prediction = nn_predict(model, state)
    
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

    #Palauta koko taulukko, vasta myöhemmin max
    
    #take highest value from prediction
    #calculate q value
    #highest prediction + alpha (0.001) * (reward + gamma * new prediction)
    #first high gamma, doesn't work so good on long term as low
    
    #take prediction with previous state, calculate reward

    #take action, return only it. put above to train. nn_predict only for saving previous values.
    
    #rules over here!
    
    return (prediction)

#Creating dummy training data
def dummy_data():

    #Random floats between 0 and 1
    dummy = np.random.rand(4,)
    dummy = np.array(dummy)
    print("Training data: " + str(dummy))

    #Trying to solve problems with model.predicts by modifying form of input data
    #dummy = Input(dummy(shape = (4, 0)))
    #dummy = BatchNormalization(dummy)
    
    return dummy

#Creating training data from sensors, communication with robot.py functions
def data(sensor1, sensor2, sensor3, sensor4):

    #Fetching sensor datas with robot.py's function
    #sensor1 = #Add function here
    #sensor2 = #Add function here
    #sensor3 = #Add function here
    #sensor4 = #Add function here

    state = [sensor1,
             sensor2,
             sensor3,
             sensor4]
    
    #change states to 0-1, no higher values allowed due to sigmoid-fucntion
    return state
main()

#reward also -1   0    1
