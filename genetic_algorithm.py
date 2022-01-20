import numpy as np
from numpy.random import rand
from numpy.random import randint
import matplotlib.pyplot as plt

D = 2 # dimenze
final_scores_RA = []
iter_RA = []
final_scores_S = []
iter_S = []
final_scores_RO = []
iter_RO = []

N_RUNS = 10
N_ITER = 100 # počet iterací
N_BITS = 16 # počet bitů na parametr
N_POP = 40 # velikost populace - NP
R_CROSS = 0.9 # pravděpodobnost křížení - pC
R_MUT = 1.0/float(N_BITS) # pravděpodobnost mutace - pM

RA_BOUNDS = [[-5.12, 5.12],[-5.12, 5.12]] # Meze funkce Rastrigin
S_BOUNDS = [[-500, 500],[-500, 500]] # Meze funkce Schwefel
RO_BOUNDS = [[-2.048, 2.048],[-2.048, 2.048]] # Meze funkce Rosenbrock

def Rastrigin(x):   
    return 10*D + (x[0]**2 - 10*np.cos(2*np.pi*x[0])) + (x[1]**2 - 10*np.cos(2*np.pi*x[1]))

def Schwefel(x):
    return 418.9829*D - ((x[0]*np.sin(np.sqrt(abs(x[0])))) + (x[1]*np.sin(np.sqrt(abs(x[1]))))) 

def Rosenbrock(x):
    return ((100*(x[1] - x[0]**2)**2) + ((x[0] - 1)**2))

def tournament_selection(pop, scores, k=3): 
    selection_ix = randint(len(pop)) # první index je náhodný, dále to projdeme a jakmile najdeme lepší index, tak ho uložíme, jestli ne, tak ho zanecháme
    for ix in randint(0, len(pop), k-1):
        if scores [ix] < scores[selection_ix]: #zkontrolujeme, jestli nenajdeme lepší
            selection_ix = ix
    return pop[selection_ix]

def crossover(p1, p2, r_cross):
    c1, c2 = p1.copy(), p2.copy() # potomci jsou kopie svých rodičů
    # check for recombination
    if rand() < r_cross:
        pt = randint(1, len(p1)-2) # vybereme náhodný bod křížení (nesmí být na konci stringu)
        c1 = p1[:pt] + p2[pt:] # provedení křížení
        c2 = p2[:pt] + p1[pt:] # provedení křížení
    return [c1, c2]

def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        if rand() < r_mut:
            bitstring[i] = 1 - bitstring[i] # přehození bitu

def decode(bounds, n_bits, bitstring):
	decoded = list()
	largest = 2**n_bits
	for i in range(len(bounds)):
		# extrahování podřetězce
		start, end = i * n_bits, (i * n_bits)+n_bits 
		substring = bitstring[start:end]
		# převedení na řetězec znaků
		chars = ''.join([str(s) for s in substring])
		# převedení na integer
		integer = int(chars, 2)
		# škálování integeru na požadovaný rozsah
		value = bounds[i][0] + (integer/largest) * (bounds[i][1] - bounds[i][0])
		decoded.append(value)
	return decoded

def genetic_algorithm_RA(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut):
	pop = [randint(0, 2, n_bits*len(bounds)).tolist() for _ in range(n_pop)] # počáteční populace
	best, best_eval = 0, objective(decode(bounds, n_bits, pop[0])) # sledování nejlepšího řešení
	for gen in range(n_iter):
		decoded = [decode(bounds, n_bits, p) for p in pop] # dekódování populace
		scores = [objective(d) for d in decoded] # ohodnocení všech kandidátů v populaci
		for i in range(n_pop):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				if scores[i] < 20:
					final_scores_RA.append(scores[i])
					iter_RA.append(gen)
				print("> %d. iteration, new best f(%s) = %f" % (gen,  decoded[i], scores[i]))
			else:
				final_scores_RA.append(best_eval)
				iter_RA.append(gen)
				print("> %d. iteration, best f(%s) = %f" % (gen,  decoded[i], best_eval))

		
		selected = [tournament_selection(pop, scores) for _ in range(n_pop)] # výběr rodičů
		children = list() # vytvoření nové generace
		for i in range(0, n_pop, 2):
			p1, p2 = selected[i], selected[i+1] # vytvoření páru vybraných rodičů 
			for c in crossover(p1, p2, r_cross): # provedení křížení a mutace
				mutation(c, r_mut)
				children.append(c)
		pop = children # nahrazení staré populace
	return [best, best_eval]

def genetic_algorithm_S(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut):
	pop = [randint(0, 2, n_bits*len(bounds)).tolist() for _ in range(n_pop)] # počáteční populace
	best, best_eval = 0, objective(decode(bounds, n_bits, pop[0])) # sledování nejlepšího řešení
	for gen in range(n_iter):
		decoded = [decode(bounds, n_bits, p) for p in pop] # dekódování populace
		scores = [objective(d) for d in decoded] # ohodnocení všech kandidátů v populaci
		for i in range(n_pop):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				if scores[i] < 20:
					final_scores_S.append(scores[i])
					iter_S.append(gen)
				print("> %d. iteration, new best f(%s) = %f" % (gen,  decoded[i], scores[i]))
			else:
				final_scores_S.append(best_eval)
				iter_S.append(gen)
				print("> %d. iteration, best f(%s) = %f" % (gen,  decoded[i], best_eval))
		
		selected = [tournament_selection(pop, scores) for _ in range(n_pop)] # výběr rodičů
		children = list() # vytvoření nové generace
		for i in range(0, n_pop, 2):
			p1, p2 = selected[i], selected[i+1] # vytvoření páru vybraných rodičů 
			for c in crossover(p1, p2, r_cross): # provedení křížení a mutace
				mutation(c, r_mut)
				children.append(c)
		pop = children # nahrazení staré populace
	return [best, best_eval]

def genetic_algorithm_RO(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut):
	pop = [randint(0, 2, n_bits*len(bounds)).tolist() for _ in range(n_pop)] # počáteční populace
	best, best_eval = 0, objective(decode(bounds, n_bits, pop[0])) # sledování nejlepšího řešení
	for gen in range(n_iter):
		decoded = [decode(bounds, n_bits, p) for p in pop] # dekódování populace
		scores = [objective(d) for d in decoded] # ohodnocení všech kandidátů v populaci
		for i in range(n_pop):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				if scores[i] < 20:
					final_scores_RO.append(scores[i])
					iter_RO.append(gen)
				print("> %d. iteration, new best f(%s) = %f" % (gen,  decoded[i], scores[i]))
			else:
				final_scores_RO.append(best_eval)
				iter_RO.append(gen)
				print("> %d. iteration, best f(%s) = %f" % (gen,  decoded[i], best_eval))
		
		selected = [tournament_selection(pop, scores) for _ in range(n_pop)] # výběr rodičů
		children = list() # vytvoření nové generace
		for i in range(0, n_pop, 2):
			p1, p2 = selected[i], selected[i+1] # vytvoření páru vybraných rodičů 
			for c in crossover(p1, p2, r_cross): # provedení křížení a mutace
				mutation(c, r_mut)
				children.append(c)
		pop = children # nahrazení staré populace
	return [best, best_eval]

nRUNS_RA = 1
scores_RA = []
final_RUNS_RA = []
while nRUNS_RA <= N_RUNS:
	best_RA, score_RA = genetic_algorithm_RA(Rastrigin, RA_BOUNDS, N_BITS, N_ITER, N_POP, R_CROSS, R_MUT)
	decoded = decode(RA_BOUNDS, N_BITS, best_RA)
	print("f(%s) = %f" % (best_RA, score_RA))
	scores_RA.append(score_RA)
	final_RUNS_RA.append(nRUNS_RA)
	nRUNS_RA += 1

nRUNS_S = 1
scores_S = []
final_RUNS_S = []
while nRUNS_S <= N_RUNS:
	best_S, score_S = genetic_algorithm_S(Schwefel, S_BOUNDS, N_BITS, N_ITER, N_POP, R_CROSS, R_MUT)
	decoded = decode(S_BOUNDS, N_BITS, best_S)
	print("f(%s) = %f" % (best_S, score_S))
	scores_S.append(score_S)
	final_RUNS_S.append(nRUNS_S)
	nRUNS_S += 1

nRUNS_RO = 1
scores_RO = []
final_RUNS_RO = []
while nRUNS_RO <= N_RUNS:
	best_RO, score_RO = genetic_algorithm_RO(Rosenbrock, RO_BOUNDS, N_BITS, N_ITER, N_POP, R_CROSS, R_MUT)
	decoded = decode(RO_BOUNDS, N_BITS, best_RO)
	print("f(%s) = %f" % (best_RO, score_RO))
	scores_RO.append(score_RO)
	final_RUNS_RO.append(nRUNS_RO)
	nRUNS_RO += 1

plt.plot(iter_RA, final_scores_RA, label='Rastrigin function')
plt.plot(iter_S, final_scores_S, label='Schwefel function')
plt.plot(iter_RO, final_scores_RO, label='Rosenbrock function')
plt.xlabel('Number of iterations')
plt.ylabel('Fitness function')
plt.legend()
plt.show()

# plt.scatter(final_RUNS_RA, scores_RA, label="Rastrigin function",color= "red", marker= "o", s=15)
# plt.scatter(final_RUNS_S, scores_S, label="Schwefel function",color= "green", marker= "o", s=15)
# plt.scatter(final_RUNS_RO, scores_RO, label="Rosenbrock function",color= "blue", marker= "o", s=15)
# plt.xlabel('nRUNS')
# plt.ylabel('Fitness function value')
# plt.legend()
# plt.title('2D')
# plt.show()