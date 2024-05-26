import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Initialize parameters
alg_params = {
    'L': 20,  # obj num
    'N': 4,   # batch amount (every guy answers N questions)
    'M': 1000,  # iteration limit (how many people do we have)
    'layers': [0.25, 0.7, 1.0]
}

L = alg_params['L']
M = alg_params['M']
N = alg_params['N']

X = np.arange(1, alg_params['L'] + 1)
Xt = np.random.permutation(alg_params['L'])
ixXt = np.argsort(Xt)

Q = []

alpha_init = 10
beta_init = 1
eta_init = 1
mu_init = 1
sigma_init = 1/9
kappa = 10e-4

params = {
    'alpha': np.ones(L) * alpha_init,
    'beta': np.ones(L) * beta_init,
    'eta': np.ones(L) * eta_init,
    'mu': np.random.rand(L) * mu_init,
    'emu': np.exp(np.random.rand(L) * mu_init),
    'sigma': np.ones(L) * sigma_init,
    'history': np.zeros((alg_params['L'], alg_params['L']))
}

for i in range(M):
    pairs = get_pairs(alg_params['N'], params)
    
    for j in range(pairs.shape[0]):
        a = pairs[j, 0]
        b = pairs[j, 1]
        pref = get_preference(Xt, a, b, alg_params)
        
        if pref == -1:
            a, b = b, a  # swap
        params['history'][a, b] += 1
        new_params = get_updated_parameters(a, b, [params['history'][a, b], params['history'][b, a]], params)
        
        # Update parameters
        params['mu'][a] = new_params['mu_a']
        params['mu'][b] = new_params['mu_b']
        
        params['sigma'][a] = new_params['sigma_a']
        params['sigma'][b] = new_params['sigma_b']
        
        params['emu'][a] = np.exp(params['mu'][a])
        params['emu'][b] = np.exp(params['mu'][b])
    
    if verbose:
        plt.clf()
        plt.imshow(params['history'], aspect='auto')
        x = np.linspace(-1, 1, 100)
        for obj in range(L):
            f = norm.pdf(x, params['mu'][obj], np.sqrt(params['sigma'][obj]))
            plt.plot(f)
            plt.draw()
            plt.pause(0.001)
        plt.show(block=False)
    
    _, ix = np.argsort(params['mu'])
    Q.append(np.sum(np.abs(ix - ixXt)))
    print(f"Current Error: {Q[-1]}")
