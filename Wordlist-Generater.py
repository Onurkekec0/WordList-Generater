import itertools
from itertools import repeat

giris=input("Usage : <characters> <min> <max> <output> ")
uniqechars=[]
hersey=giris.split(" ")
karakterler=hersey[0]
karakterler=list(karakterler)
for i in range(len(karakterler)):
    if(karakterler[i]==" "):
        pass
    elif(karakterler[i] in uniqechars):
        pass
    else:
        uniqechars.append(karakterler[i])
try:
    output=str(hersey[3])
except:
    output="wordlist"
long=0
with open(output,"w") as f:
    for k in range(int(hersey[1]),int(hersey[2])+1):
        for i in itertools.product(uniqechars,repeat=k):
            long+=1
            f.write("".join(i)+"\n")
print(long)