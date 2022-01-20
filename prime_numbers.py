import matplotlib.pyplot as plt
import numpy as np

class prvocisla:
    def __init__(self, val):
        self.prlist = []
        self.primenumbers = val

    def AtkinsSieve(self):
        cisla = 2
        stin = 15
        self.prlist.append(cisla)
        print("cislo {}: {}".format(len(self.prlist), cisla))
        
        while len(self.prlist) < self.primenumbers:
            if cisla == 2:
                cisla += 1
                self.prlist.append(cisla)
                print("cislo {}: {}".format(len(self.prlist), cisla))
            elif cisla == 5:
                self.prlist.append(cisla)
                print("cislo {}: {}".format(len(self.prlist), cisla))
            else:
                n = cisla % 12
                if n == 1 or n == 5 or n == 7 or n == 11:
                    prvocisla.Prtest(self, cisla)
        
        
            cisla += 2
            if cisla > stin:
                stin +=10
            if stin == cisla:
                cisla +=2
        
        vel = 0.0
        if cisla <= 1000:
            vel = 3
        elif 10000 >= cisla > 1000:
            vel = 1.5
        else:
            vel = 0.5 
        arr = np.array(self.prlist)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
        c = ax.scatter(arr, arr, c=arr, s=vel, cmap='hsv', alpha=1)   
        plt.show()
                             
    def Prtest(self, cislo):
        pocitadlo = 0
        pc2 = 0
        for i in self.prlist:
            if i < cislo/2:
                if cislo % i == 0:
                    pc2 += 1
                    break
                else:
                    pocitadlo += 1
            else:
                break
        if pc2 == 0:
            self.prlist.append(cislo)
            print("cislo {}: {}".format(len(self.prlist), cislo))
            
if __name__ == "__main__":
    val = int(input("Zadej počet prvočíšel:"))
    Vysledek = prvocisla(val)
    Vysledek.AtkinsSieve()
