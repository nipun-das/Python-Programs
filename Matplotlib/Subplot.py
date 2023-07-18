import matplotlib.pyplot as plt
import numpy as np

#plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1) # rows, cols, current index
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([30,18,11,12])

plt.subplot(1,2,2) # rows, cols, current index
plt.plot(x,y)

plt.show()