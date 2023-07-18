import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([1,2,3,4,5])
y2 = np.array([1,4,9,16,25])

plt.plot(y1)
plt.plot(y2)

plt.legend(['blue','green'],loc="lower right")
plt.show()