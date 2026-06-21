'''
This module stores different kinds of numerical integrators, for experimentation
and use in magnet_background.
'''
import numpy as np

def semi_implicit_euler(self, field, deltaT):
    acc = np.array(self.charge*(np.cross(self.velocity, field))/self.mass)
    self.velocity += acc*deltaT
    self.position += self.velocity*deltaT #using new velocity

def forward_euler(self, field, deltaT):
    acc = np.array(self.charge*(np.cross(self.velocity, field))/self.mass)
    self.position += self.velocity*deltaT #using old velocity
    self.velocity += acc*deltaT

def verlet_integration(self, field, deltaT):
    pass

def RK4(self, field, deltaT):
    pass

def Boris_Pusher(self, field, deltaT):
    pass
