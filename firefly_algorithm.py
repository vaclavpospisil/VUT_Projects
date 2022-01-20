import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

def FireflyAlgorithm(function, dim, lb, ub, max_evals, pop_size=20, alpha=1.0, betamin=1.0, gamma=0.01, seed=None):
    rng = default_rng(seed)
    fireflies = rng.uniform(lb, ub, (pop_size, dim))
    intensity = np.apply_along_axis(function, 1, fireflies)
    best = np.min(intensity)

    evaluations = pop_size
    new_alpha = alpha
    search_range = ub - lb

    while evaluations <= max_evals:
        new_alpha *= 0.97
        for i in range(pop_size):
            for j in range(pop_size):
                if intensity[i] >= intensity[j]:
                    r = np.sum(np.square(fireflies[i] - fireflies[j]), axis=-1)
                    beta = betamin * np.exp(-gamma * r)
                    steps = new_alpha * (rng.random(dim) - 0.5) * search_range
                    fireflies[i] += beta * (fireflies[j] - fireflies[i]) + steps
                    fireflies[i] = np.clip(fireflies[i], lb, ub)
                    intensity[i] = function(fireflies[i])
                    evaluations += 1
                    best = min(intensity[i], best)
    return best

D = 2 # Dimensions
# [-5.12, 5.12] - Bounds of Rastrigin function
# [-500, 500] - Bounds of Schwefel function
# [-2.048, 2.048] - Bounds of Rosenbrock function

def Rastrigin(x):  
    return 10*D + (x[0]**2 - 10*np.cos(2*np.pi*x[0])) + (x[1]**2 - 10*np.cos(2*np.pi*x[1]))

def Schwefel(x):
    return 418.9829*D - ((x[0]*np.sin(np.sqrt(abs(x[0])))) + (x[1]*np.sin(np.sqrt(abs(x[1]))))) 
    
def Rosenbrock(x):
    return ((100*(x[1] - x[0]**2)**2) + ((x[0] - 1)**2))

# RASTRIGIN FUNCTION    
nRUNS_ra = 1
scores_ra = []
final_RUNS_ra = []
print("---------------------------")
print("Rastrigin function!")
while nRUNS_ra <= 10:
    final_scores_ra = []
    n_iter_ra = []
    best_ra = 20
    iter = 50
    print("---------------------------")
    print("The %d. run!" %(nRUNS_ra))
    for i in range(iter):
        actual_run_best_ra = FireflyAlgorithm(function=Rastrigin , dim=2, lb=-5.12, ub=5.12, max_evals=10000)
        if actual_run_best_ra < best_ra:
            best_ra = actual_run_best_ra
            final_scores_ra.append(actual_run_best_ra)
            n_iter_ra.append(i)
            print("%d. iteration, fitness function value = %f" % (i, actual_run_best_ra))
    scores_ra.append(best_ra)
    final_RUNS_ra.append(nRUNS_ra)
    nRUNS_ra += 1

# SCHWEFEL FUNCTION

nRUNS_s = 1
scores_s = []
final_RUNS_s = []
print("---------------------------")
print("Schwefel function!")
while nRUNS_s <= 10:
    final_scores_s = []
    n_iter_s = []
    best_s = 20
    iter = 50
    print("---------------------------")
    print("The %d. run!" %(nRUNS_s))
    for i in range(iter):
        actual_run_best_s = FireflyAlgorithm(function=Schwefel , dim=2, lb=-500, ub=500, max_evals=10000)
        if actual_run_best_s < best_s:
            best_s = actual_run_best_s
            final_scores_s.append(actual_run_best_s)
            n_iter_s.append(i)
            print("%d. iteration, fitness function value = %f" % (i, actual_run_best_s))
    scores_s.append(best_s)
    final_RUNS_s.append(nRUNS_s)
    nRUNS_s += 1

# ROSENBROCK FUNCTION
nRUNS_ro = 1
scores_ro = []
final_RUNS_ro = []
print("---------------------------")
print("Rosenbrock function!")
while nRUNS_ro <= 10:
    final_scores_ro = []
    n_iter_ro = []
    best_ro = 20
    iter = 50
    print("---------------------------")
    print("The %d. run!" %(nRUNS_ro))
    for i in range(iter):
        actual_run_best_ro = FireflyAlgorithm(function=Rosenbrock, dim=2, lb=-2.048, ub=2.048, max_evals=10000)
        if actual_run_best_ro < best_ro:
            best_ro = actual_run_best_ro
            final_scores_ro.append(actual_run_best_ro)
            n_iter_ro.append(i)
            print("%d. iteration, fitness function value = %f" % (i, actual_run_best_ro))
    scores_ro.append(best_ro)
    final_RUNS_ro.append(nRUNS_ro)
    nRUNS_ro += 1

plt.scatter(final_RUNS_ra, scores_ra, label="Rastrigin function",color= "red", marker= "o", s=15)
plt.scatter(final_RUNS_s, scores_s, label="Schwefel function",color= "green", marker= "o", s=15)
plt.scatter(final_RUNS_ro, scores_ro, label="Rosenbrock function",color= "blue", marker= "o", s=15)
plt.xlabel('nRUNS')
plt.ylabel('Fitness function value')
plt.legend()
plt.show()

# plt.plot(n_iter_ro, final_scores_ro, label="Rosenbrock function")
# plt.xlabel('n_iterations')
# plt.ylabel('Fitness function value')
# plt.legend()
# plt.show()