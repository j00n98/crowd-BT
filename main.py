import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Initialize parameters
alg_params = {
    'L': 20,  # Number of objects
    'N': 4,   # Batch amount (each person answers N questions)
    'M': 1000,  # Iteration limit (number of people)
    'layers': [0.25, 0.7, 1.0]  # Layers used in the algorithm
}

L = alg_params['L']  # Number of objects
M = alg_params['M']  # Number of iterations
N = alg_params['N']  # Number of questions per batch

X = np.arange(1, alg_params['L'] + 1)  # Array from 1 to L
Xt = np.random.permutation(alg_params['L'])  # Random permutation of L
ixXt = np.argsort(Xt)  # Sorted indices of the permutation

Q = []  # List to store errors

# Initialize parameters
alpha_init = 10
beta_init = 1
eta_init = 1
mu_init = 1
sigma_init = 1/9
kappa = 10e-4

# Initialize the parameter dictionary
params = {
    'alpha': np.ones(L) * alpha_init,
    'beta': np.ones(L) * beta_init,
    'eta': np.ones(L) * eta_init,
    'mu': np.random.rand(L) * mu_init,
    'emu': np.exp(np.random.rand(L) * mu_init),
    'sigma': np.ones(L) * sigma_init,
    'history': np.zeros((alg_params['L'], alg_params['L']))  # History matrix of interactions
}

# Main loop for iterations
for i in range(M):
    pairs = get_pairs(alg_params['N'], params)  # Get pairs of objects
    
    for j in range(pairs.shape[0]):
        a = pairs[j, 0]  # First object in the pair
        b = pairs[j, 1]  # Second object in the pair
        pref = get_preference(Xt, a, b, alg_params)  # Get preference between a and b
        
        if pref == -1:
            a, b = b, a  # Swap if b is preferred over a
        params['history'][a, b] += 1  # Update interaction history
        new_params = get_updated_parameters(a, b, [params['history'][a, b], params['history'][b, a]], params)  # Get updated parameters
        
        # Update parameters with new values
        params['mu'][a] = new_params['mu_a']
        params['mu'][b] = new_params['mu_b']
        
        params['sigma'][a] = new_params['sigma_a']
        params['sigma'][b] = new_params['sigma_b']
        
        params['emu'][a] = np.exp(params['mu'][a])
        params['emu'][b] = np.exp(params['mu'][b])
    
    if verbose:
        plt.clf()  # Clear the current figure
        plt.imshow(params['history'], aspect='auto')  # Display the history matrix
        x = np.linspace(-1, 1, 100)  # X-axis values for plotting distributions
        for obj in range(L):
            f = norm.pdf(x, params['mu'][obj], np.sqrt(params['sigma'][obj]))  # Get the normal distribution for each object
            plt.plot(f)  # Plot the distribution
            plt.draw()  # Draw the plot
            plt.pause(0.001)  # Pause for a short duration to update the plot
        plt.show(block=False)  # Display the plot without blocking execution
    
    _, ix = np.argsort(params['mu'])  # Sort the objects based on mu values
    Q.append(np.sum(np.abs(ix - ixXt)))  # Calculate the error and append to the list
    print(f"Current Error: {Q[-1]}")  # Print the current error
