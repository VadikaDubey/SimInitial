# region Imports
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
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

# region Magnet
file = open('data/magnet_properties.csv', 'r')
reader = csv.reader(file)
next(reader)
for row in reader:
    magnet_position = [float(row[0]), float(row[1]), float(row[2])]
    magnet_size = [float(row[3]), float(row[4]), float(row[5])]

magnet = ax1.bar3d(
    magnet_position[0] - magnet_size[0]/2, 
    magnet_position[1] - magnet_size[1]/2,  #directly connected to magnet, not data folder
    magnet_position[2] - magnet_size[2]/2,
    magnet_size[0], magnet_size[1], magnet_size[2],
    color='blue'
)
file.close()
# endregion

# region Particles
file = open('data/particle_properties.csv', 'r')
reader = csv.reader(file)
particles=[]
next(reader)
for row in reader:
    position = [float(row[0]), float(row[1]), float(row[2])]
    particles.append(ax1.scatter([position[0]], [position[1]], [position[2]], color='green'))
file.close()

# endregion

# region Animation
file = open('data/animation.csv', 'r')

frame = 0
def draw_frame(frame):
    i=0
    file.seek(0)
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[0])==frame:
            particles[i].set_offsets([[float(row[1]), float(row[2]), float(row[3])]])
            i+=1
            #ax1.scatter(float(row[1]), float(row[2]), float(row[3]), color='green')
            ax1.quiver(float(row[1]), float(row[2]), float(row[3]), 
                       1, 1, 1, 
                       color='red'
            )

#plt.show()
file.seek(0)
reader = csv.reader(file)
rows = list(csv.reader(file))
last_frame = int(float(rows[-1][0]))

while frame<=last_frame:
    draw_frame(frame)
    plt.pause(0.01)
    frame+=100

file.close()
# endregion

plt.show()




'''
# region Field Visualisation
show_field = False

if show_field:
    for x in range(-60, 60, 5):
        for y in range(-60, 60, 5):
            for z in range(-60, 60, 5):
                findAndShowB(x, y, z, 'gray', 1)
ax1.quiver(
    x, y, z, 
    B[0], B[1], B[2], 
    color=Ucolor, alpha=Ualpha
)
# endregion
'''
