class CRCcoder:
    def __init__(self, data, genpol):
        self.data = data
        self.genpol = genpol
        self.CRCdata = ""

    def __call__(self):
        return self.CRCdata
    
    def checkgenpol(self):
        x = ""
        for i in self.data:
            self.CRCdata += i
        for i in range(len(self.genpol)-1):
            self.CRCdata += "0"
        s = divpol1(self.CRCdata, self.genpol)
        while True:
            if len(s) < len(self.genpol)-1:
                s = "0" + s
            else:
                break
        self.CRCdata = self.data
        for i in range(len(s)):
            self.CRCdata += s[i]
        print("Odeslaná sekvence je: ", format(self.CRCdata))
           
class CRCdecoder:
    def __init__(self, genpol, newdata):
        self.genpol = genpol
        self.newdata = newdata
    def checkmessage(self):
        s = divpol1(self.newdata, self.genpol)

        if s == "":
            print("Přenos je správný!")
        else:
            print("Přenos je chybný a musíme najít chybu!")
            Pozice = 0
            for j in range(len(self.newdata)):
                data = ""
                for i in range(len(self.newdata)-j):
                    if i == 0:
                        data += "1"
                    else:
                        data += "0"
                CRCdecoder = divpol1(data, genpol)
                if s == CRCdecoder:
                    Pozice = len(self.newdata)-j
                    print("Chyba je na pozici číslo: ", format(Pozice))
                    w = newdata[:j]
                    if newdata[j] == "1":
                        w += "0"
                    else:
                        w += "1"
                    w += newdata[j+1:]
                    print("Opravená sekvence je tvaru: ", format(w))
                    return w
                               
def divpol1(a, b):
    s = ""
    i = 0
    while True:
        if i < len(b):
            if a[i] == b[i]:
                s += "0"
            else:
                s += "1"
            i += 1
        elif i < len(a):
            s += a[i]
            i += 1
        else:
            i = 0
            a = zkraceni(s)
            s = ""
        if len(a) < len(b):
            break
    return a

def split(word): 
    return [char=="1" for char in word]

def zkraceni(s):
    i = 0
    while True:
        if i < len(s):
            if s[i] == "1":
                break
            else:
                i += 1
        else:
            s = ""
            break
    if len(s) > 0:
        s = s[i:]
    return s

if __name__ == '__main__':
    data = input("Zadej vstupní sekvenci bitů informace m(x): ")
    genpol = input("Zadej generující polynom g(x): ")
    P = CRCcoder(data, genpol)
    P.checkgenpol()
    CRCdata = P.CRCdata
    newdata = input("Pro kontrolu CRC zadejte přijatou sekvenci: ")
    if len(CRCdata) != len(newdata):
        newdata = input("Zadej přijatou sekvenci o správné délce: ")
    D = CRCdecoder(genpol, newdata)
    D.checkmessage()