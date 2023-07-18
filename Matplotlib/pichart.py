import matplotlib.pyplot as plt
import numpy as np

x = np.array([35,25,25,15])
labels = {"a","b","c","d"}

plt.pie(x,labels=labels)

plt.show()