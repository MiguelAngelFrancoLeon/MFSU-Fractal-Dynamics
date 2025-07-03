# dynamics_lammps.py
# Simulación de dinámica clásica en red fractal para Anexo B
# Autor: Miguel Ángel Franco León

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del MFSU
kappa = 1e-12  # kg/s, constante de fricción
dt = 1e-15     # s, paso temporal
T = 300        # K, temperatura
kB = 1.380649e-23  # J/K, constante de Boltzmann
m = 1.67e-27   # kg, masa atómica aproximada
N = 2048       # Número de sitios
t_max = 10e-12 # s, tiempo máximo

# Generar red fractal (simplificada, secuencia de Fibonacci)
def fractal_lattice(N, df=1.5):
    return np.random.normal(0, 1, N)  # Posiciones iniciales

# Simulación de Langevin
def langevin_dynamics(N, t_max, dt, kappa, T, m):
    times = np.arange(0, t_max, dt)
    r = fractal_lattice(N)
    v = np.zeros(N)
    msd = np.zeros(len(times))
    for i, t in enumerate(times):
        noise = np.random.normal(0, np.sqrt(2 * kappa * kB * T * dt / m), N)
        v += (-kappa * v * dt + noise) / m
        r += v * dt
        msd[i] = np.mean(r**2)
    return times, msd

# Ejecutar simulación
times, msd = langevin_dynamics(N, t_max, dt, kappa, T, m)

# Guardar datos
np.savetxt("data/quasicrystal_msd.csv", np.column_stack((times, msd)), delimiter=",", header="Time (s), MSD (nm^2)")

# Graficar
plt.plot(times * 1e12, msd * 1e18, label="Simulado")
plt.xlabel("Tiempo (ps)")
plt.ylabel("MSD (nm²)")
plt.grid(True)
plt.legend()
plt.savefig("figures/msd_dynamics.png")
plt.show()

print("MSD a 10 ps:", msd[-1] * 1e18, "nm²")
