import numpy as np

def get_pairs(N, params):
    from heapq import heappush, heappop

    # Define the heap as a list
    heap = []

    count = 0
    L = len(params['emu'])  # number of objects

    for a in range(L):
        for b in range(L):
            if a != b:
                new_params = get_updated_parameters(a, b, [params['history'][a][b], params['history'][b][a]], params)
                
                div_a_ab = 0 + KLGauss(new_params['mu_a'], params['mu'][a], new_params['sigma_a'], params['sigma'][a])
                div_b_ab = KLGauss(new_params['mu_b'], params['mu'][b], new_params['sigma_b'], params['sigma'][b])
                div_k_ab = 0
                pr_ab = new_params['pr']
                
                new_params = get_updated_parameters(b, a, [params['history'][b][a], params['history'][a][b]], params)
                
                div_a_ba = 0 + KLGauss(new_params['mu_a'], params['mu'][b], new_params['sigma_a'], params['sigma'][b])
                div_b_ba = KLGauss(new_params['mu_b'], params['mu'][a], new_params['sigma_b'], params['sigma'][a])
                div_k_ba = 0
                pr_ba = new_params['pr']
                
                div = pr_ab * (div_a_ab + div_b_ab + div_k_ab) + pr_ba * (div_a_ba + div_b_ba + div_k_ba)
                
                if -div < (heap[0][0] if heap else float('inf')) or count < N:
                    el = (-div, a, b)
                    
                    if count == N:
                        heappop(heap)
                    else:
                        count += 1
                    heappush(heap, el)
    
    pairs = np.zeros((N, 2), dtype=int)
    for i in range(N):
        max_el = heappop(heap)
        pairs[i, 0] = max_el[1]
        pairs[i, 2] = max_el[2]
    
    return pairs

# Example usage:
# params should be a dictionary with keys: 'emu', 'history', 'mu', 'sigma'
# params = {
#     'emu': [...],
#     'history': [...],
#     'mu': [...],
#     'sigma': [...]
# }
# N = 10
# pairs = get_pairs(N, params)
# print(pairs)
