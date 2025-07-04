# MFSU-Fractal-Dynamics: Modelo Fractal Estocástico Unificado
**Autor**: Miguel Ángel Franco León, Creador del MFSU  
**ORCID**: [https://orcid.org/0009-0003-9492-385X]  
**Contacto**: [mf410360@gmail.com]
MFSU-Fractal-Dynamics: Modelo Fractal Estocástico Unificado para Sistemas Cuántico-Clásicos
markdown

![Simulación Fractal](https://raw.githubusercontent.com/MiguelAngelFrancoLeon/MFSU-Fractal-Dynamics/main/images/fractal_simulation.png)

Implementación computacional del Modelo Fractal Estocástico Unificado (MFSU) para estudiar dinámicas complejas en sistemas clásicos y cuánticos, con aplicaciones en quasicristales, redes ópticas fractales y sistemas mesoscópicos.

## Características Principales

- **Modelo clásico**: Dinámica de Langevin con potenciales fractales no singulares
- **Modelo cuántico**: Ecuación de Lindblad con operadores de decoherencia consistentes
- **Herramientas de análisis**:
  - Cálculo de dimensión fractal mediante método de cajas
  - Estimación de entropía de Von Neumann
  - Visualización de patrones fractales 2D/3D
- **Optimizaciones**:
  - Implementación paralelizada con Numba
  - Algoritmos adaptativos para integración estocástica

## Instalación
# 🌀 MFSU-Fractal-Dynamics: Modelo Fractal Estocástico Unificado

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![arXiv](https://img.shields.io/badge/arXiv-2307.12345-b31b1b)](https://arxiv.org/abs/1234.5678)

Implementación computacional del Modelo Fractal Estocástico Unificado (MFSU) para sistemas complejos clásicos y cuánticos, con aplicaciones en:

- Quasicristales
- Redes ópticas fractales
- Transiciones de fase mesoscópicas

![Simulación Fractal](https://raw.githubusercontent.com/MiguelAngelFrancoLeon/MFSU-Fractal-Dynamics/main/images/fractal_sim.gif)

## 📦 Instalación

**Requisitos:**
- Python 3.9+
- Numpy/Scipy stack

```bash
# Opción 1: Instalación directa
pip install git+https://github.com/MiguelAngelFrancoLeon/MFSU-Fractal-Dynamics.git

# Opción 2: Desarrollo local
git clone https://github.com/MiguelAngelFrancoLeon/MFSU-Fractal-Dynamics.git
cd MFSU-Fractal-Dynamics
pip install -e .

```bash
# Clonar repositorio
git clone https://github.com/MiguelAngelFrancoLeon/MFSU-Fractal-Dynamics.git
cd MFSU-Fractal-Dynamics

# Instalar dependencias
pip install -r requirements.txt

# Instalar paquete en modo desarrollo (opcional)
pip install -e .
Uso Básico
Simulación clásica
python
from mfsu.classical import FractalLangevin

# Configurar simulación
sim = FractalLangevin(
    V0=0.1,      # Amplitud del potencial (eV)
    a=100,       # Escala característica (nm)
    T=300,       # Temperatura (K)
    kappa=1e-12  # Coeficiente de fricción (kg/s)
)

# Ejecutar 1000 pasos
results = sim.run(steps=1000)

# Visualizar resultados
sim.plot_trajectory()
sim.plot_fractal_dimension()
Simulación cuántica
python
from mfsu.quantum import FractalLindblad

# Inicializar sistema cuántico
quantum_sim = FractalLindblad(
    meff=0.01,   # Masa efectiva (en unidades de masa electrón)
    sigma_x=10,  # Escala de localización (nm)
    tau_x=1e-12  # Tiempo de decoherencia (s)
)

# Evolucionar el estado cuántico
quantum_sim.evolve(t_final=1e-9)  # 1 ns de evolución

# Analizar resultados

quantum_sim.plot_density_matrix()
quantum_sim.calculate_entropy()
Ejemplos incluidos
El repositorio contiene varios notebooks de Jupyter con casos de estudio:

examples/classical_fractal.ipynb - Generación de patrones fractales clásicos

examples/quantum_decoherence.ipynb - Efecto de la decoherencia en sistemas cuánticos fractales

examples/fractal_dimension_calculation.ipynb - Métodos para estimar dimensiones fractales

Documentación
La documentación completa está disponible en:
Documentación MFSU

Incluye:

Teoría matemática detrás del modelo

API de referencia

Guías de contribución

Benchmarks de rendimiento


Licencia
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

🤝 Cómo Contribuir
Las contribuciones son bienvenidas. Por favor:

Abre un issue para discutir los cambios propuestos

Haz fork del repositorio

Crea una rama con tu nueva característica (git checkout -b feature/nueva-funcionalidad)

Haz commit de tus cambios (git commit -am 'Añade nueva funcionalidad')

Haz push a la rama (git push origin feature/nueva-funcionalidad)

Abre un Pull Request

## Referencias

Breuer, H. P. (2002). The Theory of Open Quantum Systems. Oxford University Press.

Falconer, K. (2013). Fractal Geometry: Mathematical Foundations and Applications. Wiley.
📬 Contacto
✉️ mf410360@gemail.com
🐦 @MiguelAfrancoL
