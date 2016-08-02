import spidev
import sys,time
import numpy as np

detail=7

signalfile = open('signal_bank.txt','rb')
Signal = list(signalfile.readlines())
Signal = map(lambda s:s.strip(), Signal)
Signal = list(map(float, Signal))

filterfile = open('filter_bank.txt','rb')
Filter = list(filterfile.readlines())
Filter = map(lambda s:s.strip(), Filter)
Filter = list(map(float, Filter))

LP_filter = Filter[:len(Filter)/2]
HP_filter = Filter[len(Filter)/2:]

out = []

for i in range(detail):
	out.append([])
	out.append([])
	aux1 = np.convolve(Signal,HP_filter, 'full') #same len of the bigger 
	aux2 = np.convolve(Signal,LP_filter, 'full') #same len of the bigger 
	out[2*i] = list(aux1[::2])
	out[2*i+1] = list(aux2[::2])
	Signal = list(aux2[::2])

for value in out:
	print len(value)
	
#FUCK
