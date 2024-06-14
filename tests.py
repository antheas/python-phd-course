import numpy as np
import pytest

from diff import euler
from lorenz import lorenz


def test_lorenz():
    # Test case 1
    x = 1.0
    y = 2.0
    z = 3.0
    sigma = 10.0
    rho = 28.0
    beta = 8 / 3
    dx, dy, dz = lorenz(x, y, z, sigma, rho, beta)
    assert dx == pytest.approx(10.0), dx
    assert dy == pytest.approx(23.0), dy
    assert dz == pytest.approx(-6.0), dz


def test_euler():
    # Test case 1
    x0 = 1.0
    y0 = 2.0
    z0 = 3.0
    sigma = 10.0
    rho = 28.0
    beta = 8 / 3
    dt = 0.01
    n = 1000

    X, Y, Z, G = euler(x0, y0, z0, sigma, rho, beta, dt, n)

    assert len(X) == n + 1
    assert len(Y) == n + 1
    assert len(Z) == n + 1
    assert len(G) == n + 1


if __name__ == "__main__":
    pytest.main([__file__])
