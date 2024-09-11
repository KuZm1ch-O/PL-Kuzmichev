for a in range(1000):
    if all( ((x&103==0) and (x&94!=0))<=(x&a!=0) for x in range(1,1000) ):
        print(a)
        break

#-------2---------
for b in range(1000):
    if all(((x&500!=0) and (x&200==0))<=(x&b!=0) for x in range(1000)):
        print(b)
        break
#-------3-------
for a in range(1000):
    if all(((x&52!=0) and (x&36==0)) <=(x&a!=0) for x in range(1000)):
        print(a)
        break
#---------4-------
for a in range(1000):
    if all((x&29) and ((x&11==0)<=(x&a!=0)) for x in range(15,31)):
        print(a)
        break

#--------5--------