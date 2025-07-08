# Calc AB Final Project
# Objective of the project is to calculate the initial velocity of the throw based on the angle of throw and the time it took to hit the target
# Measurements of our classroom were taken to help with calculating the initial velocity
# Using a combination of the equations learned in class and using the math library, we solve for the initial velocity

import math

print("\nInput Time")
yv = float(input())
print("Input Angle")
theta = float(input())
print('Initial Vertical Velocity = ' + str((5 + 16*((yv)**2))/(yv*math.sin(((math.pi)/180)*theta))))
print('Initial Horizontal Velocity = ' + str((35)/(yv*math.cos(((math.pi)/180)*theta))))
