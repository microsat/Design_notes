# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 14:33:54 2016

@author: nielsen8
"""
import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
# Take inputs from pololu website to draw curves of the dc motor.

StallTorque = float(input('Please enter the stall torque in oz-inch : '))
StallCurrent = float(input('Please enter the stall current in mA : '))
RatedVoltage = float(input('Please enter the rated voltage in Volts : '))
FreeRunCurrent = float(input('Please enter the free run currennt in mA : '))
FreeRunSpeed = float(input('Please enter the free run speed in RPM : '))
Resistance = RatedVoltage / StallCurrent

torque1 = 0;
torque2 = StallTorque #  oz-inch *  (1/141.611932278)= N-m;


current1 = FreeRunCurrent  # / 1000; %mA to Amps
current2 = StallCurrent   #/ 1000; %mA to Amps

speed1 = FreeRunSpeed     #RPM = 1/9.5493 radians per sec
speed2 = 0


slope, intercept, r_value, p_value, std_err = stats.linregress([torque1, torque2], [current1, current2])

totSamples = 200

torque = np.arange(torque1,torque2,((torque2 - torque1)+1)/totSamples)

current = slope*torque+intercept

slope, intercept, r_value, p_value, std_err = stats.linregress([torque1, torque2], [speed1, speed2])

speed = slope*torque+intercept

print 'Resistance of motor = ', Resistance

f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
f, (ax3, ax4) = plt.subplots(2, 1, sharex=True)
ax1.plot(torque, current)
ax1.set_title('current vs torque')
ax2.plot(torque, speed)
ax2.set_title('current vs torque')
power = speed*torque
efficiency = power / (RatedVoltage * current)
#f, (ax3, ax4) = plt.subplots(2, 1, sharex=True)

ax3.plot(torque, power)
ax4.plot(torque, efficiency)
ax3.set_title('Output power')
ax4.set_title('Power Efficiency')
