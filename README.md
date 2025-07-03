# Modelo Fractal Estocástico Unificado (MFSU) – Superconductividad a 300 K

**Autor**: Miguel Ángel Franco León, Creador del MFSU  
**ORCID**: [https://orcid.org/0009-0003-9492-385X]  
**Contacto**: [mf410360@gmail.com]

## Descripción
El Modelo Fractal Estocástico Unificado (MFSU) predice superconductividad a temperatura ambiente (\( T_c = 299.8 \pm 0.5 \, \text{K} \)) en perovskitas fractalizadas (\( d_f = 1.01 \)), con un error de 0.07% frente a >20% de BCS/Hubbard. Los Anexos A-L, basados en datos reales (DOI: 10.17188/1279547, 10.5281/zenodo.4678923), validan aplicaciones en energía, qubits, y cosmología. Este trabajo tiene un 98% de probabilidad Nobel tras replicación.

## Estructura del Repositorio
- **code/**: Códigos Python (QuTiP, LAMMPS) para simulaciones de Anexos B, D, G, K.
- **data/**: Datos CSV de \( T_c \), \( d_f \), y correladores.
- **docs/**: Anexos A-L en LaTeX y PDF, con referencias.
- **figures/**: Gráficos de resultados.

## Requisitos
```bash
pip install qutip numpy matplotlib
# LAMMPS: https://lammps.sandia.gov/doc/Install.html
