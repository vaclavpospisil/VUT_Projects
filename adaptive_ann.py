from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from numpy.random import rand


print("------------------------------------------------------------------")
function = input(str("Do you want to use Rastrigin (R) or Schwefel (S) function? [R/S]  "))
d = 2
R_iterations = 1

# Setting function

def Rastrigin(x1, x2):  
    
    R = 10*d + (x1**2 - 10*np.cos(2*np.pi*x1)) + (x2**2 - 10*np.cos(2*np.pi*x2))
    return R

def Schwefel(x1, x2):

    S = 418.9829*d - ((x1*np.sin(np.sqrt(abs(x1)))) + (x2*np.sin(np.sqrt(abs(x2))))) 
    return S

# Chosen function

if function == "R":
    N = 1000
    LOW = -5.12
    HIGH = 5.12
    TS = np.random.uniform(low=-5.12, high=5.12, size=(N,2))
    F = np.reshape(Rastrigin(TS[:, 0], TS[:, 1]), (TS.shape[0], 1))
    print("The Rastrigin function has been selected!")

elif function == "S":
    N = 1000
    LOW = -500
    HIGH = 500
    TS = np.random.uniform(low=-500, high=500, size=(N,2))
    F = np.reshape(Schwefel(TS[:, 0], TS[:, 1]), (TS.shape[0], 1))
    print("The Schwefel function has been selected!")

print("Number of iterations: %f" % (R_iterations))
print("Parametres of ANN:")
print("Size of the training set: %f" % (N))
print("Number of layers: 4 with 100 neurons in each")
print("Activation function is tahn, last is linear")
print("Loss: mse")
print("Optimizer: sgd")
print("Metrics: mean_squared_error")
print("Validation_split: 0.2")
print("Epochs: 250")
print("Batch_size: 3")

# ANN
net = None 
for i in range(R_iterations):
    net = Sequential(name='ANN')
    net.add(Dense(100, input_dim=2, activation='tanh'))
    net.add(Dense(100, input_dim=2, activation='tanh'))
    net.add(Dense(100, input_dim=2, activation='tanh'))
    net.add(Dense(1 , activation='linear'))
    net.compile(loss='mse', optimizer='sgd', metrics=['mean_squared_error'])
    net.summary()
    net.fit(TS, F, validation_split=0.2, batch_size=3, epochs=250, verbose=0)
    net.save("Net.model")

    max_iter = 1000
    N_dim = 2
    step_x = 0.1


    if function == "R":
        fx = lambda x: 10*d + np.sum((x**2) - 10*np.cos(2*np.pi*x))
        lim_x = [-5.12, 5.12]
    elif function == "S":
        fx = lambda x: 418.9829*d - np.sum(x * np.sin(np.sqrt(np.abs(x))))
        lim_x = [-500, 500]
    
    x = lim_x[0] + rand(1, N_dim) * (lim_x[1]-lim_x[0])
    y = fx(x)

    x_hist = x
    y_hist = np.array(y)

    x_best = x
    y_best = y
    y_best_hist = y

    for iter in range(1, max_iter):
        x += step_x * rand(1, N_dim) * 2 - step_x
        x[x < lim_x[0]] = lim_x[0]
        x[x > lim_x[1]] = lim_x[1]

        y = fx(x)
        
        if y < y_best:
            y_best, x_best = y, x
        
        x_hist = np.append(x_hist, x, axis=0)
        y_hist = np.append(y_hist, y)
        y_best_hist = np.append(y_best_hist, y_best)

    i = np.where(y_hist == y_best)
    value = x_hist[i]
    X = value[0][0]
    Y = value[0][1]
    TS = np.append(TS, [[X, Y]], axis=0)

if function == "R":
    global_minimum = Rastrigin(0,0)
    found_minimum = Rastrigin(X,Y)
if function == "S":
    global_minimum = Schwefel(420.9687,420.9687)
    found_minimum = Schwefel(X,Y)

print("Global minimum is: ", global_minimum)
print("Found minimum is:" , found_minimum)