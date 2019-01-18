import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

l=131.e-02
counter=0
wlength=55.e-08
const=1.e-07
I_naught=426.5
c=3.e8
epsilon_naught=8854.e-15
tab=PrettyTable()
tab.field_names=["slit width/m","Photoelectric current/x10^-3 A"]
p=[]
i=[]
j=[]
a=1
b=a*const
while((b**2)<(l*wlength)):
    intensity=(2*I_naught/(c*epsilon_naught))/(4*((np.pi)**2))*(b**2)
    current=(0.0166*intensity)+0.0504
    tab.add_row([b,current])
    i.insert(counter,b)
    j.insert(counter,intensity)
    
    p.insert(counter,current)
    a=a+1
    if a%10==0:
        a=1
        const=const*10
    
    b=a*const
    counter=counter+1

print(tab)
plt.plot(i,p)
plt.show()



