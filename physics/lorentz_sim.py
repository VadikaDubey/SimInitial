# region Imports
import numpy as np
import csv
import integrators
import time
# endregion

# region Objects

class Particle:

    def __init__(self, position, velocity, charge, mass):
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.charge = float(charge)
        self.mass = float(mass)

    def update_particle_position(self, field, integrator_type):
        integrator_type(self, field, deltaT)

    def save_particle_position(self, frame, writer):
        writer.writerow([frame, self.position[0], self.position[1], self.position[2]])

    def save_particle_totalenergy(self, frame, writer):
        energy = (self.mass*((np.linalg.norm(self.velocity))**2))/2.0
        writer.writerow([frame, energy])
            
class Magnet():

    def __init__(self, position=np.array([-10.0, 5.0, 0.0]), size=[2, 10, 2], m=np.array([0.0, 100.0, 0.0])):
        self.magnet_position = position
        self.magnet_size = size
        self.m = m

# endregion

# region Particle

print("Particle Creation Start")
file = open('data/particle_properties.csv', 'w')
writer = csv.writer(file)
addParticle=True
writer.writerow(["x", "y", "z", "Ux", "Uy", "Uz", 'charge', 'mass'])

while addParticle==True:
    writer.writerow(
        [float(input("Particle position x: ")),
        float(input("Particle position y: ")),
        float(input("Particle position z: ")),
        float(input("Particle initial velocity Ux: ")),
        float(input("Particle initial velocity Uy: ")),
        float(input("Particle initial velocity Uz: ")),
        float(input('Particle charge: ')),
        float(input('Particle mass: '))]
    )
    addParticle = input("Continue? (y/n): ").lower() == 'y'

file.close()

file = open('data/particle_properties.csv', 'r')
reader = csv.reader(file)
next(reader)


particles = []
for row in reader:
    row = [float(x) for x in row]
    particles.append(Particle(
        [row[0], row[1], row[2]],
        [row[3], row[4], row[5]],
        row[6], row[7]
    ))
file.close()
print("Particle Creation Done!")

# endregion

# region Magnet

print("Magnet Creation Start")
print("i'll make the input questions later, for now use default")
magnet = Magnet()
with open('data/magnet_properties.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['posX', 'posY', 'posZ', 'sizeX', 'sizeY', 'sizeZ', 'm'])
    writer.writerow([magnet.magnet_position[0], magnet.magnet_position[1], magnet.magnet_position[2], 
                     magnet.magnet_size[0], magnet.magnet_size[1], magnet.magnet_size[2], 
                     magnet.m])
print("Magnet Creation Done!")

# endregion

# region Functions

def findB(x, y, z):
    r = np.array(
        [x - magnet.magnet_position[0], 
        y - magnet.magnet_position[1], 
        z - magnet.magnet_position[2]]
    )
    K = 1000
    B = np.array(K*((3*(np.dot(magnet.m, r))*r)/np.linalg.norm(r)**5 - magnet.m/np.linalg.norm(r)**3))
    return B

# endregion


# region Particle Movement!

deltaT = 0.001
frame = 0

file1 = open("data/animation.csv", "w", newline="")
writer1 = csv.writer(file1)
writer1.writerow(["frame", "x", "y", "z"])

file2 = open("data/energy.csv", "w", newline="")
writer2 = csv.writer(file2)
writer2.writerow(["frame", "Ux", "Uy", "Uz"])

start = time.time()
while (time.time()-start <= 20):
    for p in particles:
        B = findB(p.position[0], p.position[1], p.position[2])
        p.update_particle_position(B, integrators.forward_euler) # IMPORTANT INPUT: INTEGRATOR
        p.save_particle_position(frame, writer1)
        p.save_particle_totalenergy(frame, writer2)
    frame +=1
    time.sleep(deltaT)

print("Lorentz simulation done!")
file1.close()
file2.close()
# endregion



