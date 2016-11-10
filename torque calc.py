# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 10:31:25 2016

@author: microsat
"""

import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt

def CalcTorque(TotalMass=10, RadiusDriveWheel=0.1, NumDriveMotor=2,DesiredAcceleration=0.25, TotalEfficiency=65.0,MaxIncline=10):
   # torque = ((100/TotalEfficiency)*(DesiredAcceleration+9.81*(np.sin((np.pi*MaxIncline/180)))*TotalMass*RadiusDriveWheel)/NumDriveMotor
    return ((100/TotalEfficiency)*(DesiredAcceleration+9.81*(np.sin(np.pi*MaxIncline/180)))*TotalMass*RadiusDriveWheel)/NumDriveMotor


TotalMass = 11.0  # Kg
NumDriveMotor = 6  # number of drive motor
RadiusDriveWheel = 0.137  # Radius of Drive Wheel in Meter
RobotVelocity = 2.5  # m/s
MaxIncline = 32.0  # Degrees
SupplyVoltage = 12  # Volts
DesiredAcceleration = 0.25  # M/s^2
DesiredOperatingTime = 120  # Min
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
                    TotalEfficiency,MaxIncline)

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
                                                    TotalEfficiency,
                                                    MaxIncline)*141.593

print'\nIncline info'

Incline = (0, 5, 10, 20, 25, 30, 32, 40, 45, 50)
print'Incline\t', 'Motor ozf-in\t', 'Current','Current + 500ma','Ah'
for Incl in Incline:
    torq = CalcTorque(TotalMass,
                      RadiusDriveWheel,
                      NumDriveMotor,
                      DesiredAcceleration,
                      TotalEfficiency,
                      Incl)
    TP = torq*AngularVelocity
    print Incl, '\t', torq*141.593, '\t', TP/12,TP/12+0.5,(TP/12+0.5)*(DesiredOperatingTime/60)*NumDriveMotor


print'\nMotor info'


StallTorque = 416.6
StallCurrent = 20000
RatedVoltage = 12
FreeRunCurrent = 510
FreeRunSpeed = 313.0

print '\nStall torque in oz-inch : ', StallTorque
print 'Stall current in mA : ', StallCurrent
print 'Rated voltage in Volts : ', RatedVoltage
print 'Free run currennt in mA : ', FreeRunCurrent
print 'Free run speed in RPM : ', FreeRunSpeed



Resistance = RatedVoltage / StallCurrent

torque1 = 0;
torque2 = StallTorque #  oz-inch *  (1/141.611932278)= N-m;


current1 = FreeRunCurrent  # / 1000; %mA to Amps
current2 = StallCurrent   #/ 1000; %mA to Amps

speed1 = FreeRunSpeed     #RPM = 1/9.5493 radians per sec
speed2 = 0
totSamples = 10

slope, intercept, r_value, p_value, std_err = stats.linregress([torque1, torque2], [current1, current2])

torque = np.arange(torque1,torque2,((torque2 - torque1)+1)/totSamples)

current = slope*torque+intercept

plt.plot(torque, current)


print'\nIncline info'

Incline = (0, 5, 10, 20, 25, 30, 32, 40, 45, 50)
print'Incline\t', 'Motor ozf-in\t', 'Current','current_motor','Ah current_motor'
for Incl in Incline:
    torq = CalcTorque(TotalMass,
                      RadiusDriveWheel,
                      NumDriveMotor,
                      DesiredAcceleration,
                      TotalEfficiency,
                      Incl)
    TP = torq*AngularVelocity
    current_motor = slope*(torq*141.593)+intercept
    print Incl, '\t', torq*141.593, '\t', TP/12, current_motor/1000, \
        (current_motor/1000)*(DesiredOperatingTime/60)*NumDriveMotor, \
        TP,  current_motor/1000*12


