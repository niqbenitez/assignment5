import math
from datetime import datetime, timezone


def mean_anomaly(e: float, t: datetime, tau: datetime, T_days: float) -> float: #days
    if t.tzinfo is None:
        t = t.replace(tzinfo=timezone.utc)
    if tau.tzinfo is None:
        tau = tau.replace(tzinfo=timezone.utc)

    delta_days = (t - tau).total_seconds() / 86400.0
    frac = (delta_days % T_days) / T_days
    M = 2.0 * math.pi * frac
    return M


def solve_kepler(M: float, e: float, tol: float = 1e-12, max_iter: int = 100) -> float:
    M = M % (2.0 * math.pi)

    E = M if e < 0.8 else math.pi

    for _ in range(max_iter):
        f = E - e * math.sin(E) - M
        fp = 1.0 - e * math.cos(E)
        dE = f / fp
        E -= dE
        if abs(dE) < tol:
            break

    return E % (2.0 * math.pi)


def true_anomaly(E: float, e: float) -> float:
    num = math.sqrt(1.0 + e) * math.sin(E / 2.0)
    den = math.sqrt(1.0 - e) * math.cos(E / 2.0)
    v = 2.0 * math.atan2(num, den)
    return v % (2.0 * math.pi)

def print_result(e: float, t: datetime, tau: datetime, T_days: float):
    M = mean_anomaly(e, t, tau, T_days)
    E = solve_kepler(M, e)
    v = true_anomaly(E, e)

    print(e, T_days, t, tau, M, E, v)

e_mars = 0.0934
T_mars = 686.92971  # days

tau_mars = datetime(2007, 6, 1, 7, 20, 0, tzinfo=timezone.utc)
t_mars = datetime(1672, 8, 6, 0, 0, 0, tzinfo=timezone.utc)

print_result(e_mars,t_mars,tau_mars,T_mars)

e_donald = 0.1876
T_donald = 1343.0  # days

tau_donald = datetime(2024, 12, 3, 0, 0, 0, tzinfo=timezone.utc)
t_donald = datetime(2025, 4, 20, 0, 0, 0, tzinfo=timezone.utc)

print_result(e_donald,t_donald,tau_donald,T_donald)
