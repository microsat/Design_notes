# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 10:31:25 2016

@author: microsat
"""

import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt

def CalcTorque(TotalMass=10, RadiusDriveWheel=0.1, NumDriveMotor=2,DesiredAcceleration=0.25, TotalEfficiency=65.0):
   # torque = ((100/TotalEfficiency)*(DesiredAcceleration+9.81*(np.sin((np.pi*MaxIncline/180)))*TotalMass*RadiusDriveWheel)/NumDriveMotor
    return ((100/TotalEfficiency)*(DesiredAcceleration+9.81*(np.sin(np.pi*MaxIncline/180)))*TotalMass*RadiusDriveWheel)/NumDriveMotor


TotalMass = 11.0  # Kg
NumDriveMotor = 6  # number of drive motor
RadiusDriveWheel = 0.137  # Radius of Drive Wheel in Meter
RobotVelocity = 2.5  # m/s
MaxIncline = 32.0  # Degrees
SupplyVoltage = 12  # Volts
DesiredAcceleration = 0.25  # M/s^2
DesiredOperatingTime = 240  # Min
TotalEfficiency = 65  # %
print 'Inputs'
print 'TotalMass ', TotalMass, ' Kg'
print 'Num Drive Motor ', NumDriveMotor, '# number of drive motor'
print 'Radius Drive Wheel ', RadiusDriveWheel, ' meter'
print 'Robot Velocity ', RobotVelocity, ' m/s'
print 'Max Incline ', MaxIncline, ' deg'
print 'Desired Acceleration ', DesiredAcceleration, ' m/s^2'
print 'Desired OperatingTime ', DesiredOperatingTime, ' minutes'
print 'Total Efficiency ', TotalEfficiency, ' %'

torque = CalcTorque(TotalMass,
                    RadiusDriveWheel,
                    NumDriveMotor,
                    DesiredAcceleration,
                    TotalEfficiency)

AngularVelocity = RobotVelocity/RadiusDriveWheel
TotalPower = torque*AngularVelocity
print ''
print 'Angular Velocity ', AngularVelocity, ' rad/s ', \
                 AngularVelocity*60/(2*np.pi), ' rev/min'
print 'Motor Torque need is torque: ', torque, ' Nm ', \
                 (torque*100/9.81), ' Kgf-cm ', (torque*141.593), ' ozf-in'
print 'Total Power ', TotalPower, ' Watts'
print 'Max Current ', TotalPower/SupplyVoltage, ' A'
print 'Battery Pack', \
    (TotalPower/SupplyVoltage)*(DesiredOperatingTime/60)*NumDriveMotor, ' Ah'

totSamples = 10
speeds = (.5, 1, 1.25, 1.5, 1.75, 2, 2.1, 2.5)
speeds = np.arange(.25, RobotVelocity, .25)

print '\nSpeed info'

print 'm/s\t', 'mph'

for speed in speeds:
    print speed, '\t', (3600*speed)/1609.3

print'\nWeight info'

weights = (5, 10, 20, 25, 30, 40, 50)
print'lbs\t', 'kg\t', 'Motor ozf-in '
for lb in weights:
    print lb, '\t', lb*0.45359237, '\t', CalcTorque(lb*0.45359237,
                                                    RadiusDriveWheel,
                                                    NumDriveMotor,
                                                    DesiredAcceleration,
                                                    TotalEfficiency)*141.593

