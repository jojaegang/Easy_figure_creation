import matplotlib.pyplot as plt
import numpy as np

params = {
    'axes.labelsize':9, # Font size for axis labels
    'axes.titlesize':9, # Font size for the title
    'xtick.labelsize':9, # Font size for x-axis tick labels
    'ytick.labelsize':9, # Font size for y-axis tick labels
    'xtick.direction': 'in', # Direction of tick marks (in, out, inout)
    'ytick.direction': 'in', # Direction of tick marks (in, out, inout)
    'lines.markersize': 3, # Marker size
    'axes.titlepad': 6, # Padding between title and graph
    'axes.labelpad': 4, # Padding between axis label and graph
    'font.size': 9, # Font size
    'font.sans-serif': 'Arial', # Font setting
    'figure.dpi': 300, # Resolution, vector graphics remain sharp regardless of dpi
    'figure.autolayout': True, # Ensures all elements fit inside the figure
    'xtick.top': True, # Show tick marks on the top of the x-axis
    'ytick.right': True, # Show tick marks on the right side of the y-axis
    'xtick.major.size': 2, # Length of major tick marks on the x-axis
    'ytick.major.size': 2, # Length of major tick marks on the y-axis
}
plt.rcParams.update(params)

fig, ax = plt.subplots(figsize=(6.0 / 2.54, 6.0 / 2.54)) # 6cm x 6cm (1 inch = 2.54 cm)
# Data for plotting
x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)
plt.plot(x, y)
plt.xlim(0, 2)
plt.ylim(0, 2)
plt.xlabel('x')
plt.ylabel('y')

# If you use plt.show() to view the figure, the image size might not be correct when saving
fig.savefig('temp.svg', transparent=True)
