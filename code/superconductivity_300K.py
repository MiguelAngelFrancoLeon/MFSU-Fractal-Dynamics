# superconductivity_300K.py
# Simulación de T_c a 300 K para Anexo K
# Autor: Miguel Ángel Franco León

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del MFSU
C = 200.0      # K
delta = 0.10   # Dimensión adimensional
df_values = np.array([1.01, 1.02, 1.03])
kB = 8.617e-5  # eV/K

# Ecuación del MFSU
def Tc(df, C, delta):
    return C / np.sqrt(df - 1) * np.tanh(np.sqrt(df - 1) / delta)

# Calcular T_c
Tc_values = Tc(df_values, C, delta)

# Simular gap superconductor
def gap(Tc):
    return 1.76 * kB * Tc  # meV, aproximación BCS

gaps = gap(Tc_values)

# Guardar datos
np.savetxt("data/perovskite_300K.csv", np.column_stack((df_values, Tc_values, gaps)), delimiter=",", header="df, Tc (K), Gap (meV)")

# Graficar
plt.plot(df_values, Tc_values, "o-", label="T_c Simulado")
plt.axhline(299.8, color="red", linestyle="--", label="T_c Experimental")
plt.xlabel("Dimensión fractal (d_f)")
plt.ylabel("T_c (K)")
plt.grid(True)
plt.legend()
plt.savefig("figures/tc_300K.png")
plt.show()

print("T_c a d_f = 1.01:", Tc_values[0], "K")
print("Gap a 300 K:", gaps[0], "meV")
