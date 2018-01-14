import serial
import numpy as np
from matplotlib import pyplot as plt
from drawnow import *

arduinoData = serial.Serial('/dev/ttyACM0', 9600)

sensor = []
output = []

plt.ion()
cnt = 0

def makeFig():                            #Create a function that makes our desired plot
    s = sensor
    t = output

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='sensor reading (mV)',
       title='Sample data')
    ax.grid()

    fig.savefig("test.png")
    plt.show() 

def get_serial_port():
    ser_devs = [dev for dev in os.listdir('/dev') if dev.startswith('ttyAC')]
    if len(ser_devs) > 0:
        return '/dev/'+ser_devs[0]
    return None

while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoString = arduinoData.readline()  #read the line of text from the serial port
    string = arduinoString.decode()
    dataArray = string.split(',')   #Split it into an array called dataArray
    data1 = float( dataArray[0])            #Convert first element to floating number and put in temp
    data2 = float( dataArray[1])            #Convert second element to floating number and put in P
    sensor.append(data1)                     #Build our tempF array by appending temp readings
    output.append(data2)                     #Building our pressure array by appending P readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>500):                            #If you have 50 or more points, delete the first one from the array
        sensor.pop(0)                       #This allows us to just see the last 50 data points
        output.pop(0)
