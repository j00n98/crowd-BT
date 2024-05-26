import numpy as np

def KLGauss(mu_0, mu_1, sigma_0, sigma_1):
    k = len(mu_0)
    
    divergence = np.trace(np.linalg.inv(sigma_1) @ sigma_0) + \
                 (mu_1 - mu_0).T @ np.linalg.inv(sigma_1) @ (mu_1 - mu_0) - \
                 k - np.log(np.linalg.det(sigma_0) / np.linalg.det(sigma_1))
    
    divergence = divergence / 2
    
    return divergence

# Example usage:
mu_0 = np.array([0, 0])
mu_1 = np.array([1, 1])
sigma_0 = np.array([[1, 0], [0, 1]])
sigma_1 = np.array([[2, 0], [0, 2]])

divergence = KLGauss(mu_0, mu_1, sigma_0, sigma_1)
print(f"KL Divergence: {divergence}")
