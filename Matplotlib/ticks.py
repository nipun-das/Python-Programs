import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6])
y = np.array([0,250])

fig = plt.figure()
ax = plt.axes()

plt.plot(x,y)

ax.set_xticks([0,2,4,6])
ax.set_xticklabels(["zero","two","four","six"])
ax.set_yticks([0,100,250])
ax.set_yticklabels(["zero","hundred","twofifty"])

plt.show()