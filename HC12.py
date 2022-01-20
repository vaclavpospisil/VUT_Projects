import numpy as np
import matplotlib.pyplot as plt

def Rastrigin(x, D=2):   
    return 10*D + (x[0]**2 - 10*np.cos(2*np.pi*x[0])) + (x[1]**2 - 10*np.cos(2*np.pi*x[1]))

def Schwefel(x, D=2):
    return 418.9829*D - ((x[0]*np.sin(np.sqrt(abs(x[0])))) + (x[1]*np.sin(np.sqrt(abs(x[1]))))) 

def Rosenbrock(x):
    return ((100*(x[1] - x[0]**2)**2) + ((x[0] - 1)**2))

class HC12:
    def __init__(self, n_param, n_bit_param, dod_param = None, float_type = np.float64):
        self.n_param = n_param
        self.n_bit_param = np.array([n_bit_param for _ in range(n_param)], dtype = np.uint32)
        self.dod_param = dod_param
        self.uint_type = np.uint16
        self.float_type = float_type
        self.total_bits = int(np.sum(self.n_bit_param))
        self._M0_rows = 1
        self._M1_rows = self.total_bits
        self._M2_rows = self.total_bits*(self.total_bits-1)//2
        self.rows = self._M0_rows + self._M1_rows + self._M2_rows
        self.K = np.zeros((1, self.n_param), dtype=self.uint_type) # kernel
        self.M = np.zeros((self.rows, self.n_param), dtype=self.uint_type) # gray code
        self.B = np.zeros((self.rows, self.n_param), dtype=self.uint_type) # binary
        self.I = np.zeros((self.rows, self.n_param), dtype=self.uint_type) # integer
        self.R = np.zeros((self.rows, self.n_param), dtype=self.float_type) # real number
        self.F = np.zeros((self.rows, self.n_param), dtype=self.float_type) # fitness
        self._init_M()

    @property
    def dod_param(self):
        return self._dod_param

    @dod_param.setter
    def dod_param(self, dod_param):
        if len(dod_param) == self.n_param:
            self._dod_param = np.array(dod_param)
        else:
            self._dod_param = np.array([dod_param for _ in range(self.n_param)])

    def run(self, func, times, kernel=None, max_iter=1000):
        for run_i in range(times):
            
            if run_i == max_iter:
                break

            if kernel is None:
                kernel = np.random.randint(0, 2, self.n_param)

        self.K = kernel
        # K xor M - vysledek B
        self.B = np.array(np.logical_xor(self.K, self.M))
        # dekodovat Graye z B do I
        self.I = self.graytobin(self.B)
        self.I = self.bintoint(self.I)
        # prevod I do realnych cisel
        self.R = self.inttoreal(self.I)
        # vypocet hodnoty ucelove funkce F
        self.F = func(self.R)
        # vybrat nejlepsi a pak bud ukoncit nebo ho prohlasit za nove K
        min_index = np.argmin(self.F)
        min_value = self.F[min_index]
        min_pos = self.R[min_index]
        kernel = self.B[min_index,:]
        return (min_value, min_pos)

    def _init_M(self):
        bit_lookup = []
        for p in range(self.n_param):
            for b in range(self.n_bit_param[p]):
                bit_lookup.append((p, b))

        for j in range(1, 1+self._M1_rows):
            p, bit = bit_lookup[j-1]
            self.M[j, p] |= 1 << bit

        j = self._M0_rows + self._M1_rows
        for bit in range(self.total_bits-1):
            for bit2 in range(bit+1, self.total_bits):
                self.M[j, bit_lookup[bit][0]] |= 1 << bit_lookup[bit][1]
                self.M[j, bit_lookup[bit2][0]] |= 1 << bit_lookup[bit2][1]
                j += 1

    def graytobin(self, gray: np.array):
        B = np.zeros(gray.shape, dtype=np.uint32)
        for i, j in enumerate(gray):
            for k, l in enumerate(j):
                if k == 0:
                    B[i,k] = 1 if l else 0
                elif k == 1:
                    B[i,k] = int(np.logical_xor(j[k-1], l))
                else:
                    prev_B = int(B[i, k-1])
                    B[i,k] = int(np.logical_xor(prev_B, l))
        return B

    def bintoint(self, B: np.array):
        I = np.zeros((B.shape[0], 1), dtype=np.uint32)
        for i, j in enumerate(B):
            I[i] = sum([k*(2**l) for k,l in list(enumerate(reversed(j)))])
        return I

    def inttoreal(self, I: np.array):
        (min_I, max_I) = self.bintoint(np.array([np.zeros((self.n_param, 1)), np.ones((self.n_param, 1))]))
        max_F = max(self.dod_param[1])
        min_F = min(self.dod_param[1])
        R = np.zeros(I.shape)
        for i, j in enumerate(I):
            R[i] = max_F + (min_F - max_F)/(max_I - min_I) * (max_I - j)
        return R

if __name__ == '__main__':
    nRUNS = 20
    runs = list(range(1,nRUNS+1)) 
    values_RA = []
    values_S = []
    values_RO = []
    # RASTRIGIN FUNCTION
    print('-------------------------------------')
    print('Rastrigin function')
    nRUNS_RA = 1
    best_RA = 10000
    while nRUNS_RA <= nRUNS:
        hc12_instance = HC12(n_param=8, n_bit_param = 15, dod_param=[-5.12, 5.12])
        x, fx = hc12_instance.run(func=Rastrigin, times=2)
        if x < best_RA:
            best_RA = x
            values_RA.append(best_RA)
            print("%s. iteration, new best is : %s" % (nRUNS_RA, x))
        else:
            values_RA.append(best_RA)
            print("%s. iteration, best is : %f" % (nRUNS_RA, best_RA))

        nRUNS_RA += 1

    # SCHWEFEL FUNCTION
    print('-------------------------------------')
    print('Schwefel function')
    nRUNS_S = 1
    best_S = 10000
    while nRUNS_S <= nRUNS:
        hc12_instance = HC12(n_param=8, n_bit_param = 15, dod_param=[-500, 500])
        x, fx = hc12_instance.run(func=Schwefel, times=2)
        if x < best_S:
            best_S = x
            values_S.append(best_S)
            print("%s. iteration, new best is : %f" % (nRUNS_S, x))
        else:
            values_S.append(best_S)
            print("%s. iteration, best is : %f" % (nRUNS_S, best_S))

        nRUNS_S += 1

    # ROSENBROCK FUNCTION
    print('-------------------------------------')
    print('Rosenbrock function')
    nRUNS_RO = 1
    best_RO = 10000
    while nRUNS_RO <= nRUNS:
        hc12_instance = HC12(n_param=8, n_bit_param = 15, dod_param=[-2.048, 2.048])
        x, fx = hc12_instance.run(func=Rosenbrock, times=2)
        if x < best_RO:
            best_RO = x
            values_RO.append(best_RO)
            print("%s. iteration, new best is : %s" % (nRUNS_RO, x))
        else:
            values_RO.append(best_RO)
            print("%s. iteration, best is : %s" % (nRUNS_RO, best_RO))
        nRUNS_RO += 1

    plt.plot(runs, values_RA, label='Rastrigin function')
    plt.plot(runs, values_S, label='Schwefel function')
    plt.plot(runs, values_RO, label='Rosenbrock function')
    plt.xlabel('Number of iterations')
    plt.ylabel('Fitness function')
    plt.legend()
    plt.show()