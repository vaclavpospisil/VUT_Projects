import numpy as np
import matplotlib.pyplot as plt
from ann_data_generator import data_unsorted
import random
import csv
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense

data = 0.4444444 * (data_unsorted[:,0] + 2)**2 + 2.3668639 * (data_unsorted[:,1] - 3)**2 < 1
data_sorted_lst = []

for i in range(len(data)):
    data_sorted_lst.append([data_unsorted[i,0],data_unsorted[i,1],data[i]])
data_sorted = np.array(data_sorted_lst)

print('   x_1         x_2         classification')
print(data_sorted)

data_x1_inside = []
data_x2_inside = []
data_x1_outside = []
data_x2_outside = []

for i in range(len(data)):
    if data[i] == True:
        data_x1_inside.append(data_unsorted[i,0])
        data_x2_inside.append(data_unsorted[i,1])
    else:
        data_x1_outside.append(data_unsorted[i,0])
        data_x2_outside.append(data_unsorted[i,1])

data_x_1_inside = np.array(data_x1_inside)
data_x_2_inside = np.array(data_x2_inside)
data_x_1_outside = np.array(data_x1_outside)
data_x_2_outside = np.array(data_x2_outside)

def graph_plot():

    n = np.linspace(0, 2*np.pi, 100)
    x = -2 + np.sqrt(1/0.4444444) * np.cos(n)
    y = 3 + np.sqrt(1/2.3668639) * np.sin(n)

    plt.scatter(data_x_1_inside, data_x_2_inside, label="Inside",color= "green", marker= "o", s=15)
    plt.scatter(data_x_1_outside, data_x_2_outside, label="Outside",color= "red", marker= "o", s=15)
    plt.plot(x,y, label="Border")
    plt.xlim(-4, 2)
    plt.ylim(2, 5)
    plt.legend()
    plt.show()

def ann():
    net = None
    net = Sequential(name='ANN')
    net.add(Dense(200, input_dim=2, activation='tanh', name='input'))
    net.add(Dense(150, input_dim=2, activation='tanh', name='hidden'))
    net.add(Dense(100, input_dim=2, activation='tanh'))
    net.add(Dense(1 , activation='linear', name='output'))
    net.summary()
    net.compile(loss='mse', optimizer='sgd', metrics=['accuracy'])
    net.fit(data_unsorted, data, validation_split=0.2, batch_size=3, epochs=1000, verbose=0)

    _, accuracy = net.evaluate(data_unsorted, data)
    print('Accuracy: %.2f' % (accuracy*100))
    
    save = input(" Do you want to save this model or try it again? (Save | Again) : ")
    if save == "Save" or save == "save":
        net.save('net/'+'net'+'.h5')
    
        # Saving data
        fields = ['x_1', 'x_2', 'classification']

        # data rows of csv file
        rows = []
        for i in range(len(data)):
            rows.append([data_unsorted[i,0],data_unsorted[i,1],data[i]])     
    
        # name of csv file
        filename = "saved_data.csv"
        
        # writing to csv file
        with open(filename, 'w') as csvfile:

            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(rows)

        print("*** Model saved")

    elif save == "Again" or save == "again":
        ann()
    else: 
        print("Error: You did not choose from the above options!")

if __name__ == "__main__":
    graph_plot()
    ann()