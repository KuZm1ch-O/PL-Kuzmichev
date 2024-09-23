#-----------1----------
s=' ''ехал грека через ехал реку. Видит ежик грека в реке рак'
#s=input('введите строку')
#s=' '+s
c=0
for i in range(len(s)):
    if s[i]==' ' and s[i+1]=='е':
        c+=1
print(c)
#-----------15-----------
s='ттт тпт вфоит оатфытаойт'
c=0
for i in range(len(s)):
    if s[i]=='т':
        c+=1
print(c)
#----------------2----------
s='gtegmrgmwr:,orgowfwofw:mwofwoqkfw:fowkf%50'
c=0
for i in range(len(s)):
    if s[i]==':':
        s=s.replace(':','%',1)
        c+=1
print(c)
