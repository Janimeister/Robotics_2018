from keras.models import Sequential
from keras.layers import Dense
from keras import losses
import numpy as np
import random
import keras.backend as K

def main():
    print("Start:")

#Initializing the neural network, its layer, activation functions and optimizer
def nn_initialize():
    
    #Defining model
    model = Sequential()
    
    # Input layer
    model.add(Dense(units=3, input_shape=(1,), activation='sigmoid'))
    
    #Hidden layer
    model.add(Dense(units=32, activation='sigmoid'))
    
    #Output layer
    model.add(Dense(units=3, activation='linear'))
    
    #Compiling model
    model.compile(loss=losses.binary_crossentropy, optimizer='RMSprop', metrics = ["accuracy"])
    
    return model

#Training with the dummy data, gets model and state as input, returns trained model
def nn_train_dummy(model, state, steps, i):

    #Learningrate
    alpha = 0.02
    
    #Prediction from nn_predict()
    prediction = nn_predict(model, state)
    
    #Test print
    print("Prediction: " + str(prediction))

    #Calculating highest prediction for detecting highest value among inputs
    highest_prediction = np.amax(prediction)

    #Test print
    print("Highest: " + str(highest_prediction))

    #Taking new state
    state_new = dummy_generate(state, steps, i)

    #Making new prediction for calculating new Qvalue
    prediction_new = nn_predict(model, state_new)

    #Making new highest prediction for calculating reward based on action
    highest_prediction_new = np.amax(prediction_new)
    
    #Gamma value, calculated from the highest prediction
    gamma = highest_prediction_new / 3

    #Defining reward
    reward_new = reward(highest_prediction_new)
    
    #Calculating the Q-value
    Qvalue = np.amax(prediction) + alpha * (reward_new + gamma + np.amax(prediction_new))
    #Qvalue = np.array(Qvalue)

    #Getting index of highest prediction
    i,j = np.unravel_index(prediction.argmax(), prediction.shape)
    index = [i,j]
    print("Index of highest prediction: " + str(index))
    prediction[index] = Qvalue
  
    #Train the model with one iteration and input (state)
    model.fit(state, prediction, epochs=1, verbose=1)

    return model

#Training with the actual sensor data, gets model and state as input, returns trained model
def nn_train_sensor(model, state):

    #Learningrate
    alpha = 0.02

    #Prediction from nn_predict()
    prediction = nn_predict(model, state)
    print("Prediction is: " + str(prediction))
    
    #Highest prediction from nn_predict()
    highest_prediction = np.amax(prediction)
    print("Highest prediction: " + str(highest_prediction))

    #Defining action
    actioni = action(highest_prediction)

    #Taking new state
    state_new = data(state)

    #Making new prediction for calculating new Qvalue
    prediction_new = nn_predict(model, state_new)

    #Making new highest prediction for calculating reward based on action
    highest_prediction_new = np.amax(prediction_new)
    
    #Gamma value, calculated from the highest prediction
    gamma = highest_prediction_new / 3

    #Defining reward
    reward_new = reward(highest_prediction_new)

    #Calculating the Q-value
    Qvalue = np.amax(prediction) + alpha * (reward_new + gamma + np.amax(prediction_new))
    #Qvalue = np.array(Qvalue)

    #Getting index of highest prediction
    i,j = np.unravel_index(prediction.argmax(), prediction.shape)
    index = [i,j]
    print("Index of highest prediction: " + str(index))
    prediction[index] = Qvalue
    
    #Train the model with one iteration and input (state)
    model.fit(state, prediction, epochs=1, verbose=1)
    
    return model, actioni

#Prediction making, gets model and state as input, returns highes prediction among the values
def nn_predict(model, state):
    
    #Make new prediction
    prediction = model.predict(state)

    #take prediction with previous state, calculate reward

    #take action, return only it. put above to train. nn_predict only for saving previous values.
    
    #rules over here!
    
    return (prediction)

#Creating dummy training data
def dummy_data():

    #Random floats between 0 and 1
    dummy = np.random.rand(3,)
    dummy = np.array(dummy)
    print("Training data: " + str(dummy))
    
    return dummy

def dummy_generate(dummy, steps, i):

    #Generating increasing/decreasing values

    #Modifying inputs to increase/decrease for half amount of iterations
    if(i < steps/2 and i > 0 ):
        
        #Error handling, if value >= 1
        if(dummy[0] + 0.1 >= 1):
            dummy[0] = np.random.rand()
        else:
            dummy[0] += 0.1
            
        #Error handling, if value <= 0
        if(dummy[1] - 0.1 <= 0):
            dummy[1] = np.random.rand()
        else:
            dummy[1] -= 0.1

        #Error handling, if value >= 1
        if(dummy[2] + 0.1 >= 1):
            dummy[2] = np.random.rand()
        else:
            dummy[2] += 0.1
        
        print("Training data: " + str(dummy) + "\nIteration: " + str(i))

    #Vice Versa
    if(i > steps/2 and i != steps):
        
        #Error handling, if value <= 0
        if(dummy[0] - 0.1 <= 0):
            dummy[0] = np.random.rand()
        else:
            dummy[0] -= 0.1
            
        #Error handling, if value >= 1
        if(dummy[1] + 0.1 >= 1):
            dummy[1] = np.random.rand()
        else:
            dummy[1] += 0.1
            
        #Error handling, if value <= 0
        if(dummy[2] - 0.1 <= 0):
            dummy[2] = np.random.rand()
        else:
            dummy[2] -= 0.1
            
        print("Training data: " + str(dummy) + "Iteration: " + str(i))
        

    return dummy
    

#Creating training data from sensors, communication with robot.py functions
#Called in robot.py
def data(sensor):

    state = sensor

    #Function to scale the values from sensors to range between 0 and 1
    for i in range(len(state)):
        result = ((state[i]-0)/(85-0))
        
    #Change states to 0-1, no higher values allowed due to sigmoid-fucntion
    return state

#Calculating reward value by state, defined once every iteration
def reward(highest_prediction):

    if(highest_prediction < 0.10):
        reward = -1
    if(highest_prediction >= 0.10 and highest_prediction < 0.20):
        reward = -0.5
    if(highest_prediction >= 0.30 and highest_prediction < 0.40):
        reward = 0
    if(highest_prediction >= 0.40 and highest_prediction < 0.50):
        reward = 0.5
    if(highest_prediction >= 0.50 and highest_prediction < 1):
        reward = 1
        
    return reward

def action(highest_prediction):
    if(highest_prediction < 0.20):
        action = 0
    if(highest_prediction >= 0.20 and highest_prediction < 0.40):
        action = 2
    if(highest_prediction >= 0.40 and highest_prediction < 0.60):
        action = random.randint(2, 4)
    if(highest_prediction >= 0.60 and highest_prediction < 0.80):
        action = 3
    if(highest_prediction >= 0.80 and highest_prediction < 1):
        action = 1
        
    return action

def initialize():
    #Initializing neural network
    model = nn_initialize()

    #Steps
    steps = 200

    #Making first dummy_data set
    dummy = dummy_data()

    #Making first sensor data
    #data = data(sensor1, sensor2, sensor3)
    
    #Training the neural network with dummy data,
    for i in range(steps):
        dummy = dummy_generate(dummy, steps, i) #Dummy_data()
        model = nn_train_dummy(model, dummy, steps, i)

    return model
    
main()
