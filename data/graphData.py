# http://www.learningaboutelectronics.com/Articles/How-to-plot-a-graph-with-matplotlib-from-data-from-a-CSV-file-using-the-CSV-module-in-Python.php

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("C://Users//black//CS499//learned_index//Learned-Index-Structures//data//exponential.csv", 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x, y, marker='o')

plt.title('Data')

plt.xlabel('x')
plt.ylabel('y')

plt.show()
