import numpy as np

def KLGauss(mu_0, mu_1, sigma_0, sigma_1):
    """
    Calculate the Kullback-Leibler divergence between two Gaussian distributions.

    Args:
        mu_0 (ndarray): Mean vector of the first Gaussian distribution.
        mu_1 (ndarray): Mean vector of the second Gaussian distribution.
        sigma_0 (ndarray): Covariance matrix of the first Gaussian distribution.
        sigma_1 (ndarray): Covariance matrix of the second Gaussian distribution.

    Returns:
        float: The Kullback-Leibler divergence between the two distributions.
    """
    k = len(mu_0)  # Dimension of the mean vectors
    
    # Calculate the KL divergence using the formula for Gaussian distributions
    divergence = np.trace(np.linalg.inv(sigma_1) @ sigma_0) + \
                 (mu_1 - mu_0).T @ np.linalg.inv(sigma_1) @ (mu_1 - mu_0) - \
                 k - np.log(np.linalg.det(sigma_0) / np.linalg.det(sigma_1))
    
    divergence = divergence / 2  # Divide by 2 as per the KL divergence formula
    
    return divergence

# Example usage:
mu_0 = np.array([0, 0])  # Mean vector of the first Gaussian distribution
mu_1 = np.array([1, 1])  # Mean vector of the second Gaussian distribution
sigma_0 = np.array([[1, 0], [0, 1]])  # Covariance matrix of the first Gaussian distribution
sigma_1 = np.array([[2, 0], [0, 2]])  # Covariance matrix of the second Gaussian distribution

# Calculate the KL divergence between the two Gaussian distributions
divergence = KLGauss(mu_0, mu_1, sigma_0, sigma_1)
print(f"KL Divergence: {divergence}")  # Output the result
