import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np

# Fixing random state for reproducibility
# np.random.seed(19680801)

# create random data


A=np.load('fornp.npy')
xdata = A[:, 0]
ydata1 = A[:, 1]
ydata2 = A[:, 2]



# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata, ydata1, color='tab:blue')
ax.plot(xdata, ydata2, color='tab:orange')

# create the events marking the x data points
# xevents1 = EventCollection(xdata, color='tab:blue', linelength=0.05)
# xevents2 = EventCollection(xdata, color='tab:orange', linelength=0.05)
#
# # create the events marking the y data points
# yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05,
#                            orientation='vertical')
# yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05,
#                            orientation='vertical')

# add the events to the axis
# ax.add_collection(xevents1)
# ax.add_collection(xevents2)
# ax.add_collection(yevents1)
# ax.add_collection(yevents2)

# set the limits
ax.set_xlim([0, 200])
ax.set_ylim([0, 1])

ax.set_title('line plot with data points')

# display the plot
plt.show()