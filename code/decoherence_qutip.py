# decoherence_qutip.py
# Simulación de decoherencia cuántica para Anexo D
# Autor: Miguel Ángel Franco León

import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
gamma0 = 0.1e-3  # eV, tasa de decoherencia
t_max = 5e-12    # s, tiempo máximo
dt = 0.01e-12    # s, paso temporal
df = 1.65        # Dimensión fractal
N = 1000         # Iteraciones

# Operadores
sigma_z = qt.sigmaz()
sigma_x = qt.sigmax()
H = sigma_z  # Hamiltoniano simplificado
c_op = [np.sqrt(gamma0 * (df - 1)) * sigma_x]  # Operador de Lindblad fractal

# Estado inicial
psi0 = (qt.basis(2, 0) + qt.basis(2, 1)).unit()

# Resolver ecuación maestra
times = np.arange(0, t_max, dt)
result = qt.mesolve(H, psi0, times, c_op, [qt.sigmaz()])

# Calcular entropía
rho = [qt.ket2dm(psi) for psi in result.states]
entropy = np.array([qt.entropy_vn(r) for r in rho])

# Guardar datos
np.savetxt("data/entropy_qubits.csv", np.column_stack((times, entropy)), delimiter=",", header="Time (s), Entropy (kB)")

# Graficar
plt.plot(times * 1e12, entropy, label="Simulado")
plt.xlabel("Tiempo (ps)")
plt.ylabel("Entropía (k_B)")
plt.grid(True)
plt.legend()
plt.savefig("figures/entropy_dynamics.png")
plt.show()

print("Entropía a 5 ps:", entropy[-1])
