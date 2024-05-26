def get_updated_parameters(a, b, history, params):
    def get_C():
        # Eq 19
        C1 = np.exp(history[0]) / (np.exp(history[0]) + np.exp(history[1]))
        C2 = 1 - C1
        C = (C1 * params['alpha'][0] + C2 * params['beta'][0]) / (params['alpha'][0] + params['beta'][0])
        return C1, C2, C
    
    kappa = 10e-4
    
    term = 1 - params['emu'][a] / (params['emu'][a] + params['emu'][b])
    
    # Eq 12
    new_params = {}
    new_params['mu_a'] = params['mu'][a] + params['sigma'][a] * term
    
    # Eq 13
    new_params['mu_b'] = params['mu'][b] - params['sigma'][b] * term
    
    term = -params['emu'][a] * params['emu'][b] / (params['emu'][a] + params['emu'][b]) ** 2
    
    # Eq 14
    new_params['sigma_a'] = params['sigma'][a] * max(1 + params['sigma'][a] * term, kappa)
    # Eq 15
    new_params['sigma_b'] = params['sigma'][b] * max(1 + params['sigma'][b] * term, kappa)
    
    C1, C2, C = get_C()
    new_params['pr'] = C1
    
    return new_params

# Example usage:
# params should be a dictionary with keys: 'alpha', 'beta', 'emu', 'mu', 'sigma'
# history should be a list or array with two elements
# params = {
#     'alpha': [...],
#     'beta': [...],
#     'emu': [...],
#     'mu': [...],
#     'sigma': [...]
# }
# a = ...
# b = ...
# history = [...]
# new_params = get_updated_parameters(a, b, history, params)
# print(new_params)
