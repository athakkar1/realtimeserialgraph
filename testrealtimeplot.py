import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import serial

# Initialize a deque with maxlen 300
data_buffer = deque(maxlen=300)

# Open the serial port
serial_port = serial.Serial('COM3', 115200, timeout=.1)

fig, ax = plt.subplots()

def update(num):
    data = ''
    while serial_port.in_waiting > 0:
      data = serial_port.readline().decode('utf-8', errors='ignore').strip()
    try:
        if data:
          value = float(data)
          data_buffer.append(value)
          ax.clear()
          ax.plot(data_buffer, label='Received Data')
    except ValueError:
        pass

ani = FuncAnimation(fig, update, interval=100)
plt.show()