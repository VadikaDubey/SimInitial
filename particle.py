from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Background
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(projection='3d')
ax1.set_title("Moving Particle")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_xlim(-60, 60)
ax1.set_ylim(-60, 60)
ax1.set_zlim(-60, 60)
ax1.grid(True)

# Function to find magnetic field at given point
def findAndShowB(x, y, z, Ucolor='black', Ualpha=1.0):
    if not(15<x<35 or -10<y<10 or -10<z<10):
        r = np.array([x - (magnet_position[0] + 1.0), y - (magnet_position[1] + 5.0), z - (magnet_position[2] + 1.0)])
        m = np.array([0.0, 100.0, 0.0])
        K = 1000
        B = np.array(K*((3*(np.dot(m, r))*r)/np.linalg.norm(r)**5 - m/np.linalg.norm(r)**3))
        ax1.quiver(x, y, z, B[0], B[1], B[2], color=Ucolor, alpha=Ualpha)
        #return B

# Particle
position = np.array([-50.0, 0.0, 0.0])
velocity = np.array([0.0, 0.0, 0.0])
charge = +1
mass = 1
deltaT = 0.001
particle = ax1.scatter(position[0], position[1], position[2])

# Magnet
magnet_position = np.array([24.0, 0.0, -1.0])
magnet = ax1.bar3d(
    magnet_position[0], magnet_position[1], magnet_position[2],
    2, 10, 2,
    color='blue'
)
show_field = True

# Field Visualisation
if show_field:
    for x in range(-60, 60, 5):
        for y in range(-60, 60, 5):
            for z in range(-60, 60, 5):
                findAndShowB(x, y, z, 'gray', 1)

findAndShowB(position[0], position[1], position[2], 'red')

plt.show()

# Particle Movement!
#while True:
#    B = findAndShowB(position[0], position[1], 'red')
#    acc = np.array((charge*B)/mass)
#    velocity += acc*deltaT #pos before v or opp, matters?
#    position += velocity*deltaT
#    particle.set_offsets(position)
#    plt.pause(1)



