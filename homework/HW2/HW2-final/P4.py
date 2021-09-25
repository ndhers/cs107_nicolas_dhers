import numpy as np
import matplotlib.pyplot as plt
import datetime

# Closure defined below
def make_coor(r):
	def coor(theta):
		x = r*np.cos(np.pi*theta/180.0)
		y = r*np.sin(np.pi*theta/180.0)
		return [x,y]
	return coor

# Current time:
currentDT = datetime.datetime.now()
hour = currentDT.hour
minute = currentDT.minute
second = currentDT.second

# Calculate theta in degrees for each hand
theta_hour = 90 - 30*hour-minute/2
theta_minute = 90 - 6*minute
theta_second = 90-6*second

# Specify the length of hour, minute and second hands
r_hour = 6
r_minute = 10
r_second = 9

# create instances of closure and compute coordinates
hour_hand = make_coor(r_hour)
x_hour, y_hour = hour_hand(theta_hour)

minute_hand = make_coor(r_minute)
x_min, y_min = minute_hand(theta_minute)

second_hand = make_coor(r_second)
x_sec, y_sec = second_hand(theta_second)

# Plot the clock
plt.plot([0, x_hour], [0, y_hour], linewidth=5, color = 'r')
plt.plot([0, x_min], [0, y_min], linewidth=4, color = 'b')
plt.plot([0, x_sec], [0, y_sec], linewidth=2, color = 'g')
plt.xticks([])  
plt.yticks([])  
plt.title('Clock showing current time (red is hour, blue minute, green second)')
plt.show()


