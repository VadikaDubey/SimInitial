from matplotlib import pyplot as plt

# Background
fig, ax1 = plt.subplots(1, figsize=(10, 6))
ax1.set_title("Moving Particle")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_xlim(-60, 60)
ax1.set_ylim(-1, 1)
ax1.grid(True)
#ax1.axis("equal")

# Particle
position = [-50, 0]
velocity = [10, 0]
deltaT = 0.001
particle = ax1.scatter(position[0], position[1])

# Making it move
while position[0] < 50:
    position[0] += velocity[0]*deltaT
    particle.set_offsets([position[0], position[1]])
    plt.pause(0.001)
