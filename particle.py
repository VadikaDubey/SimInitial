from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

# Background
fig, ax1 = plt.subplots(1, figsize=(10, 6))
ax1.set_title("Moving Particle")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_xlim(-60, 60)
ax1.set_ylim(-60, 60)
ax1.grid(True)

# Function to find magnetic field at given point
def findAndShowB(x, y, Ucolor='black', Ualpha=1.0):
    r = np.array([x - (magnet.get_x() + 1), y - (magnet.get_y() + 5)])
    m = np.array([0, 100])
    K = 1
    B = np.array(K*((3*(np.dot(m, r))*r)/np.linalg.norm(r)**5 - m/np.linalg.norm(r)**3))
    ax1.quiver(x, y, B[0], B[1], color=Ucolor, alpha=Ualpha)

# Particle
position = np.array([-50, 0])
charge = 1
deltaT = 0.001
particle = ax1.scatter(position[0], position[1])

# Magnet
magnet = Rectangle((24, -5), 2, 10)
ax1.add_patch(magnet)
show_field = True


# Field Visualisation
if show_field:
    for x in range(-60, 60, 5):
        for y in range(-60, 60, 5):
            findAndShowB(x, y, 'gray', 0.5)

# Particle Magnetic Field
findAndShowB(position[0], position[1], 'red')

plt.show()