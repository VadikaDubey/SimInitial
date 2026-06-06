# region Imports
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# endregion

# region Background
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(projection='3d')
ax1.set_title("A Particle in a Magnetic Field")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")
ax1.set_xlim(-60, 60)
ax1.set_ylim(-60, 60)
ax1.set_zlim(-60, 60)
ax1.grid(True)
# endregion

# region Functions

def dist_from_magnet(x, y, z):
    r = np.array([x - magnet_position[0], y - magnet_position[1], z - magnet_position[2]])
    return r

def findB(x, y, z):
    r = dist_from_magnet(x, y, z)
    K = 1000
    B = np.array(K*((3*(np.dot(m, r))*r)/np.linalg.norm(r)**5 - m/np.linalg.norm(r)**3))
    return B

def findAndShowB(x, y, z, Ucolor='black', Ualpha=1.0):
    B = findB(x, y, z)
    ax1.quiver(
        x, y, z, 
        B[0], B[1], B[2], 
        color=Ucolor, alpha=Ualpha
    )
    return B

# endregion

# region Particle Object

class Particle:

    def __init__(self, position, velocity, charge, mass):
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.charge = charge
        self.mass = mass
        self.sphere = ax1.scatter(self.position[0], self.position[1], self.position[2])
    


    def update_particle_position(self, field):
        acc = np.array(self.charge*(np.cross(self.velocity, field))/self.mass)
        self.velocity += acc*deltaT #pos before v or opp, matters?
        self.position += self.velocity*deltaT



# endregion

# region Particle

p1 = Particle(
    [-10.0, 0.0, 0.0], 
    [0.0, 20.0, 0.0], 
    +1.0, 1.0
)

deltaT = 0.001

# endregion

# region Magnet
magnet_position = np.array([25.0, 5.0, 0.0])
magnet_size = [2, 10, 2]
m = np.array([0.0, 100.0, 0.0])

magnet = ax1.bar3d(
    magnet_position[0] - magnet_size[0]/2, magnet_position[1] - magnet_size[1]/2, magnet_position[2] - magnet_size[2]/2,
    magnet_size[0], magnet_size[1], magnet_size[2],
    color='blue'
)
# endregion

# region Field Visualisation
show_field = False

if show_field:
    for x in range(-60, 60, 5):
        for y in range(-60, 60, 5):
            for z in range(-60, 60, 5):
                findAndShowB(x, y, z, 'gray', 1)

# endregion


# region Particle Movement!
c = 0
#p1.position[0]<60 and p1.position[1]<60 and p1.position[2]<60
while True:
    B = findB(p1.position[0], p1.position[1], p1.position[2])
    p1.update_particle_position(B)
    c +=1
    if (c % 100 == 0):
        #print(velocity)
        p1.sphere._offsets3d = ([p1.position[0]], [p1.position[1]], [p1.position[2]])
        B = findB(p1.position[0], p1.position[1], p1.position[2])
        ax1.quiver(p1.position[0], p1.position[1], p1.position[2], B[0], B[1], B[2], color='red')
    plt.pause(0.00001)

# endregion



