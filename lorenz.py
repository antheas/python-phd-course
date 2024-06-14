def lorenz(x: float, y: float, z: float, sigma: float, rho: float, beta: float):
    """
    Calculate the derivatives of the Lorenz system.

    Args:
        x (float): The x-coordinate.
        y (float): The y-coordinate.
        z (float): The z-coordinate.
        sigma (float): The sigma parameter.
        rho (float): The rho parameter.
        beta (float): The beta parameter.

    Returns:
        Tuple[float, float, float]: The derivatives dx, dy, dz.
    """
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    return dx, dy, dz

