import math

class Háromszög():
    def __init__(self):
        self.a = 0    
        self.b = 0
        self.c = 0
    
    def ker(self):
        return self.a + self.b + self.c
    
    def ter(self):
        s= (self.a + self.b +self.c) / 2
        sa = s - self.a
        sb = s - self.b
        sc = s - self.c
        számolás = s * sa * sb * sc
        return math.sqrt(számolás)
    
    def kör(self):
    
        if (self.a**2 + self.b**2) == self.c **2:
            return "Nincs belső köre mivel ez egy derékszögű háromszög és azoknál csak köré lehet irni"
    
        elif (self.a**2 + self.b**2) != self.c **2:
            r = 2*Háromszög.ter(self) / (self.a + self.b + self.c)
            return round(r,2),"cm"
    
    def szerk(self):
        if self.a + self.b > self.c and self.a +self.c > self.b and self.c + self.b > self.a :
            return "Szerkeszthető!", Háromszög.ker(self), Háromszög.ter(self), Háromszög.kör(self)
        else:
            return "Nem szerkeszthető igy nincs semmije."                                                        
f = open("eredmény.txt","w",encoding="UTF-8")   

háromszög = Háromszög()

print("A maga által megadott paraméterek cenitméterben értendő. A kör sugara két tizedes jegyre van kerekitve. ")

háromszög.a = (int(input("A oldal:")))
háromszög.b = (int(input("B oldal:")))
háromszög.c = (int(input("C oldal:")))

f = open("eredmény.txt","w", encoding="UTF-8")

Lista = []
for i in range(1):
    iratás = háromszög.szerk()
    Lista.append(iratás)

új = []
for i in Lista[0]:
    új.append((i))

print(új)
kerület = új[1]


if kerület > 0:
    f.write("Szerkeszthető" +"\n"+ str(új[1]) + "\n" + str(új[2]) + "\n" + str(új[3]))
else:
    f.write("Nem szerkeszthető")
