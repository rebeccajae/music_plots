from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

input_data = read("res.wav")
audio = input_data[1]
yvals = [r[0] for r in audio[0:4800]]
yvals -= min(yvals)
xvals = np.linspace(0, 1, num=len(yvals))
plt.plot(xvals, yvals)

plt.xlim(0, 1)
plt.xlabel("Time")
plt.savefig('gensample.eps', format='eps', dpi=1000)
