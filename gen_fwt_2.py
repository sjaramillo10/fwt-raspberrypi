import spidev
import sys,time
import csv

spi = spidev.SpiDev()
spi.open(0, 1)
spi.bits_per_word=8
spi.cshigh=False

csvfile = open('fwt_2.csv','w')
fieldnames = ['value']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

print (spi.cshigh)
print (spi.max_speed_hz)
print (spi.mode)
print (spi.lsbfirst)

con = 0
try:
	while con<=1000:
		resp = spi.readbytes(2)
		resp[1] = resp[1]>>2
		resp[0] = (resp[0]&0b00111111)<<6
		valor = resp[1]|resp[0]
		#print 'valor' + str(valor) + '='+ str(valor*3.3/4095)
		writer.writerow({'value':valor*3.3/4095})
		con+=1
	print con
	
#end while
except KeyboardInterrupt:
	spi.close()
	csvfile.close()	
#end try
