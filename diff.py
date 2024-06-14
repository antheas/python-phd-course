import numpy as np

from lorenz import lorenz


def euler(
    x0: float,
    y0: float,
    z0: float,
    sigma: float,
    rho: float,
    beta: float,
    dt: float,
    n: int,
):
    """
    Approximates the solution to the Lorenz system of differential equations using the Euler method.

    Parameters:
    - x0 (float): The initial value of x.
    - y0 (float): The initial value of y.
    - z0 (float): The initial value of z.
    - sigma (float): The sigma parameter of the Lorenz system.
    - rho (float): The rho parameter of the Lorenz system.
    - beta (float): The beta parameter of the Lorenz system.
    - dt (float): The time step size.
    - n (int): The number of iterations.

    Returns:
    - X (ndarray): An array containing the x values at each iteration.
    - Y (ndarray): An array containing the y values at each iteration.
    - Z (ndarray): An array containing the z values at each iteration.
    - G (ndarray): An array containing the magnitude of the velocity vector at each iteration.
    """
    X, Y, Z, G = np.zeros(n + 1), np.zeros(n + 1), np.zeros(n + 1), np.zeros(n + 1)
    X[0], Y[0], Z[0] = x0, y0, z0

    for i in range(n):
        dx, dy, dz = lorenz(X[i], Y[i], Z[i], sigma, rho, beta)
        X[i + 1] = X[i] + dx * dt
        Y[i + 1] = Y[i] + dy * dt
        Z[i + 1] = Z[i] + dz * dt
        G[i] = np.sqrt(dx**2 + dy**2 + dz**2)

    G[-1] = G[-2] # type: ignore
    return X, Y, Z, G

