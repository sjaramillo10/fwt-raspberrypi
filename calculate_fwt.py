import spidev
import sys,time

signalfile = open('signal_bank.txt','rb')
Signal = list(signalfile.readlines())

filterfile = open('filter_bank.txt','rb')
Filter = list(filterlfile.readlines())

print Signal[0]
print Filter[0]
