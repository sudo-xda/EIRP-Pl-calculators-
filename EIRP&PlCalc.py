import math
print("EIRP & Pl calculator by sudo_xda")

Pt = float(input("Enter value of Pt in W/dBd:"))
Gt = float(input("Enter value of Gt in dBd:"))
Gr = float(input("Enter value of Gr in dBd:"))
Pr = float(input("Enter value of Pr in dBm:"))
Lt = float(input("Enter value of Lt in dB:"))
Lr = float(input("Enter value of Lr in dB:"))

Gt = (Gt+2.15 )
Gr = (Gr+2.15)
Pr = (Pr-31)

Eirp = float(Pt+Gt-Lt)
print('EIRP in dBw:',Eirp)
s = (Eirp/10.0)
print("EIRP in watt:",10**s)



Pl = float(Pt+Gt+Gr-Pr-Lt-Lr)
print("PL in dB:" ,Pl)





