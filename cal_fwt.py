import spidev
import sys,time

txtfile = open('fwt_2.txt','rb')
signal = list(txtfile.readlines())

print signal[0]
