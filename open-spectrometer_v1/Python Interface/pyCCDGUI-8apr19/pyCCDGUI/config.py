import numpy as np


#serial definitions
port = '/dev/ttyACM0'
baudrate = 115200

#Data as the program handles
SHperiod = np.uint32(200)
ICGperiod = np.uint32(100000)
AVGn = np.uint8([0,1])
MCLK = 2000000
SHsent = np.uint32(200)
ICGsent = np.uint32(100000)
stopsignal = 0

#Data arrays for received bytes
rxData8 = np.zeros(7388, np.uint8)
rxData16 = np.zeros(3694, np.uint16)
pltData16 = np.zeros(3694, np.uint16)

#Arrays for data to transmit
txsh = np.uint8([0,0,0,0]) 
txicg = np.uint8([0,0,0,0])
txfull = np.uint8([0,0,0,0,0,0,0,0,0,0,0,0])

#Invert data
datainvert = 1
offset = 0
balanced = 0
