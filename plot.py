import matplotlib.pyplot as plt
x=(1,2,3,4,5,6,7,8,9)
plt.plot(x,x[::-1])
plt.ylabel('scale')
plt.xlabel('time')
#plt.axis([0,m,0,t])
plt.show()
