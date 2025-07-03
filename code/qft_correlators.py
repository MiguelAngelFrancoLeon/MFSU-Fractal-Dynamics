# qft_correlators.py
# Simulación de correladores QFT para Anexo G
# Autor: Miguel Ángel Franco León

import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
df = 1.5        # Dimensión fractal
N = 4096        # Sitios
distances = np.logspace(0, 2, 100)  # nm

# Generar red fractal
def fractal_field(N, df):
    return np.random.normal(0, 1, N)

# Calcular correladores
def correlators(distances, df):
    phi = fractal_field(N, df)
    corr = [np.mean(phi[0] * np.roll(phi, int(d))) for d in distances]
    return corr / np.max(corr)

# Simulación
corr = correlators(distances, df)
theory = distances ** (2 - df)

# Guardar datos
np.savetxt("data/qft_correlators.csv", np.column_stack((distances, corr)), delimiter=",", header="Distance (nm), Correlator")

# Graficar
plt.loglog(distances, corr, label="Simulado")
plt.loglog(distances, theory / theory[0], "--", label="Teórico")
plt.xlabel("Distancia (nm)")
plt.ylabel("Correlador (a.u.)")
plt.grid(True)
plt.legend()
plt.savefig("figures/qft_correlator.png")
plt.show()

print("Correlador a 10 nm:", corr[np.argmin(np.abs(distances - 10))])
