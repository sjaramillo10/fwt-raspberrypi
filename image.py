import Image

s1 = range(256)
s2 = range(0,256,2)
s3 = range(0,256,4)
s4 = range(0,256,8)
s5 = range(0,256,16)
s6 = range(0,256,32)
s7 = range(0,256,64)

scale1 = []
for s in s1:
    scale1 += [s]*4

scale2 = []
for s in s2:
    scale2 += [s]*8

scale3 = []
for s in s3:
    scale3 += [s]*16

scale4 = []
for s in s4:
    scale4 += [s]*32

scale5 = []
for s in s5:
    scale5 += [s]*64

scale6 = []
for s in s6:
    scale6 += [s]*128

scale7 = []
for s in s7:
    scale7 += [s]*256

lst = []
lst += scale7*90
lst += scale6*90
lst += scale5*90
lst += scale4*90
lst += scale3*90
lst += scale2*90
lst += scale1*90

#print img

img = Image.new("L", (1024, 630), "white")
img.putdata(lst)
img.show()
