import psutil
import matplotlib.pyplot as plt
from collections import deque
import numpy as np
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter
from gpuinfo import GPUInfo

    


def init():
    line1.set_ydata([np.nan] * len(x))
    line2.set_ydata([np.nan] * len(x))
    line3.set_ydata([np.nan] * len(x))
    return line1,line2,line3,

def animate(i):
    # Add next value
    # data.append(np.random.randint(0, max_val))
    val = psutil.cpu_percent()
    val2 = psutil.virtual_memory()[2]
    val3 = GPUInfo.gpu_usage()[0][0]
    data.append(val)
    data2.append(val2)
    data3.append(val3)
    line1.set_ydata(data)
    line2.set_ydata(data2)
    line3.set_ydata(data3)
    return line1,line2,line3,

max_x = 60
max_val = 100
arr = [0 for i in range(max_x)]

data = deque(np.zeros(max_x), maxlen=max_x)  # hold the last 10 values
data2 = deque(np.zeros(max_x), maxlen=max_x)
data3 = deque(np.zeros(max_x), maxlen=max_x)
x = np.arange(0, max_x)

fig, ax = plt.subplots()
ax.set_ylim(0, max_val)
ax.set_xlim(0, max_x-1)
line1, = ax.plot(x, np.random.randint(0, max_val, max_x))

line2, = ax.plot(x, np.random.randint(0, max_val, max_x))

line3, = ax.plot(x, np.random.randint(0, max_val, max_x))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:.0f}s'.format(max_x - x - 1)))
plt.xlabel('Seconds ago')
plt.ylabel('Usage %')
plt.legend(['CPU Usage %', 'Memory Usage %', 'GPU Usage %'], loc='upper left')

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1000, blit=True, save_count=10)

plt.show()


    
