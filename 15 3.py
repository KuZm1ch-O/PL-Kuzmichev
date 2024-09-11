#-------1--------
for a in range(1000):
    if all((x+2*y<a) or (y>x) or (x>60) for x in range(1000) for y in range(1000)):
        print(a)
        break
#---------2-------
for a in range(1000,-1,-1):
    if all((x+2*y>a) or (y<x) or (x<30) for x in range(1000) for y in range(1000)):
        print(a)
        break
#-------3--------
for a in range(1000):
    if all((x*y<a) or (x<y) or (9<x) for x in range(1000) for y in range(1000)):
        print(a)
        break
#-------4------
for a in range(1000):
    if all((x<a) or (y<a) or (x+2*y>50) for x in range(1000) for y in range(1000)):
        print(a)
        break
#-----5------
for a in range(1000):
    if all((x>=27) or (2*x<3*y) or ((x+2)*(y-3)<a)for x in range(1000) for y in range(1000)):
        print(a)
        break
#---------6------
for a in range(1000):
    if all((x>=9) or (2*x<y) or (x*y<a) for x in range(1000) for y in range(100)):
        print(a)
        break