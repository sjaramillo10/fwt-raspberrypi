import spidev
import sys,time

spi = spidev.SpiDev()
spi.open(0, 1)
spi.bits_per_word=8
spi.cshigh=False

txtfile = open('fwt_2.txt','w')

print (spi.cshigh)
print (spi.max_speed_hz)
print (spi.mode)
print (spi.lsbfirst)

con = 0
try:
	while con<=1024:
		resp = spi.readbytes(2)
		resp[1] = resp[1]>>2
		resp[0] = (resp[0]&0b00111111)<<6
		valor = resp[1]|resp[0]
		#print 'valor' + str(valor) + '='+ str(valor*3.3/4095)
		txtfile.writelines(str(valor*3.3/4095)+'\n')
		con+=1
	print con
	
#end while
except KeyboardInterrupt:
	spi.close()
	txtfile.close()	
#end try
