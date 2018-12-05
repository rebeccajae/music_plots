#Compare single-square to square+saw.
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal



def datgen(r):
    squareComponent = signal.square(2 * np.pi * 8 * r)+1
    sawComponent = signal.sawtooth(2 * np.pi * 2 * r)+1
    return 0.5*(squareComponent+sawComponent)

t = np.linspace(0, 1, 500, endpoint=False)
plt.plot(t, 0.5*(signal.square(2 * np.pi * 8 * t)+1))
plt.xlim(0, 1)
plt.xlabel("Time")
#plt.show()
plt.savefig('plot1.eps', format='eps', dpi=1000)
plt.clf()
t = np.linspace(0, 1, 500, endpoint=False)
data = datgen(t)

plt.plot(t, data/max(data))
plt.xlim(0, 1)
plt.xlabel("Time")
plt.savefig('plot2.eps', format='eps', dpi=1000)
