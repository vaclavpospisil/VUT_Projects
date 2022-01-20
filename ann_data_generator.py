import random
import numpy as np
import pandas as pd
import array as arr
import csv

# 1 -  data randomly generated

'''data_unsorted = np.array([[random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)],
                          [random.uniform(-4, 2),random.uniform(2, 5)]])'''
#______________________________________________________________________
#### 2 - Data written by hand

'''number_of_inputs = int(input("How many numbers do you want to generate? "))
print("Enter the values one by one for x_1 and x_2.")

x_1 = []
x_2 = []
k = []
l = []

for i in range(number_of_inputs):
    k = float(input("Value x_1 in range <-4;2> : "))
    if -4 <= k <= 2:
        x_1.append(k)
    else:
        print("Wrong interval! Try it again!") 
        break
    
    l = float(input("Value x_2 in range <2;5> : "))
    if 2 <= l <= 5:
        x_2.append(l)
    else:
        print("Wrong interval! Try it again!")
        break

x_1_array = np.array(x_1)
x_2_array = np.array(x_2)

data_unsorted_lst = []
for i in range(number_of_inputs):
    data_unsorted_lst.append([x_1_array[i],x_2_array[i]])

data_unsorted = np.array(data_unsorted_lst)'''
## ______________________________________________________________________
##### 3 - Import from CSV file


filename = "ann_data.csv"

fields = ['x_1','x_2']
rows = []
  
# reading csv file
with open(filename, 'r') as csvfile:

    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

data_unsorted_str = (np.array(rows))
data_unsorted_x1 = (data_unsorted_str[:,0])
data_unsorted_x2 = (data_unsorted_str[:,1])
data_unsorted1_x1 = []
data_unsorted1_x2 = []

for i in range(len(data_unsorted_x1)):
    data_unsorted1_x1.append(float(data_unsorted_x1[i]))
    data_unsorted1_x2.append(float(data_unsorted_x2[i]))

data_unsorted_lst = []

for i in range(len(data_unsorted1_x1)):
    data_unsorted_lst.append([data_unsorted1_x1[i],data_unsorted1_x2[i]])
data_unsorted = np.array(data_unsorted_lst)