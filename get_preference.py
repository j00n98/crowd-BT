import numpy as np

def get_preference(Xt, a, b, alg_params):
    val_at_a = Xt[a]
    val_at_b = Xt[b]
    
    layers = alg_params['layers'] * alg_params['L']
    a_layer = np.argmax(layers > val_at_a)
    b_layer = np.argmax(layers > val_at_b)
    
    pref = (val_at_a > val_at_b)
    if a_layer == b_layer:
        p = np.exp(-(val_at_a + val_at_b))  # probability of wrong answer
        r = np.random.rand()
        if r < p:
            pref = not pref
    
    if not pref:
        pref = -1
    
    return pref

# Example usage:
# Xt = np.array([...])
# alg_params = {
#     'layers': ...,
#     'L': ...
# }
# a = ...
# b = ...
# pref = get_preference(Xt, a, b, alg_params)
# print(pref)
