# Modelo Fractal Estocástico Unificado (MFSU) –

**Autor**: Miguel Ángel Franco León, Creador del MFSU  
**ORCID**: [https://orcid.org/0009-0003-9492-385X]  
**Contacto**: [mf410360@gmail.com]

# Modelo Fractal Estocástico Unificado (MFSU)

Este repositorio contiene el código, datos y documentación para el **Modelo Fractal Estocástico Unificado (MFSU)**, un marco teórico innovador que unifica dinámicas fractales y estocásticas en regímenes clásico y cuántico. El MFSU aborda limitaciones de modelos previos mediante:
- Un potencial fractal no singular con fases angulares.
- Ruido térmico basado en la ecuación de Langevin.
- Operadores de Lindblad dimensionalmente consistentes para modelar decoherencia cuántica.
- Una conexión explícita entre dinámicas clásicas y cuánticas vía ecuaciones de Ehrenfest con ruido.

Sus aplicaciones incluyen redes ópticas cuánticas, crecimiento de quasicristales y plasmones fractales, con dimensiones fractales calculadas $d_n \in [1.5, 1.8]$ consistentes con sistemas físicos reales.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Resultados](#resultados)
- [Cita](#cita)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción

El **Modelo Fractal Estocástico Unificado (MFSU)** es un avance en el modelado de sistemas complejos con dinámicas fractales y estocásticas. Sus características principales son:
- **Dinámica Clásica**: Modela el movimiento de una partícula en un potencial fractal no singular con ruido térmico, descrito por la ecuación de Langevin:
  \[
  \vec{r}_{n+1} = \vec{r}_n - \frac{\Delta t}{\kappa} \nabla V_{\text{fractal}}(\vec{r}_n) + \sqrt{\frac{2k_B T \Delta t}{\kappa}} \vec{\xi}_n
  \]
- **Dinámica Cuántica**: Describe la evolución de la densidad cuántica mediante una ecuación de Lindblad con operadores de decoherencia físicamente fundamentados.
- **Conexión Clásico-Cuántica**: Establece una correspondencia explícita mediante ecuaciones de Ehrenfest con ruido.
- **Cálculo de Dimensión Fractal**: Utiliza un algoritmo de conteo de cajas para calcular dimensiones fractales de trayectorias clásicas y densidades cuánticas.

El modelo se valida con simulaciones numéricas usando parámetros realistas ($V_0 = 0.1$ eV, $a = 100$ nm, $\gamma_x = 0.1$ eV), mostrando dimensiones fractales consistentes con quasicristales y redes ópticas fractales. Para detalles teóricos, consulta el artículo en `docs/MFSU_paper.pdf`.

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/MiguelAngelFrancoLeon/MFSU-Fractal-Dynamics.git
   cd MFSU-Fractal-Dynamics
Instala las dependencias (requiere Python 3.8+):bash

pip install -r requirements.txt

Dependencias necesarias:Python 3.8 o superior
NumPy>=1.21.0
SciPy>=1.7.0
Matplotlib>=3.4.0
Jupyter>=1.0.0 (opcional, para exploración interactiva)

Verifica la instalación:
Ejecuta la prueba unitaria:bash

python tests/test_potential.py

UsoPara reproducir las simulaciones del artículo:Navega al directorio de scripts:bash

cd scripts

Ejecuta la simulación principal:bash

python simulate_fractal_dynamics.py

Resultados:Las figuras se guardan en figures/ (por ejemplo, classical_trajectory.png, quantum_density.png).
Los datos de salida (por ejemplo, dimensiones fractales) se guardan en data/.

Configuración de parámetros:
Los parámetros están definidos en config.yaml. Ejemplo:yaml

V0: 0.1        # Amplitud del potencial (eV)
a: 100e-9      # Escala espacial (m)
T: 300         # Temperatura (K)
kappa: 1e-12   # Coeficiente de fricción (kg/s)
tau_x: 1e-12   # Tiempo de decoherencia (s)
sigma_x: 10e-9 # Escala de localización (m)

Exploración interactiva:
Usa el cuaderno Jupyter en notebooks/exploration.ipynb para visualizar resultados interactivamente.

Estructura del Repositoriosrc/: Código fuente (funciones para potencial fractal, simulaciones clásicas y cuánticas).
data/: Datos de entrada y salida de las simulaciones.
figures/: Figuras generadas en formatos PNG y PDF.
docs/: Documentación, incluido el artículo en PDF (MFSU_paper.pdf).
scripts/: Scripts para reproducir resultados.
tests/: Pruebas unitarias para verificar el código.
notebooks/: Cuadernos Jupyter para exploración interactiva.
requirements.txt: Dependencias de Python.
config.yaml: Parámetros de simulación.
LICENSE: Licencia MIT.

ResultadosLos resultados clave del MFSU incluyen:Trayectorias Clásicas: Dimensión fractal dn=1.78±0.05d_n = 1.78 \pm 0.05d_n = 1.78 \pm 0.05
, calculada mediante疗

System: * Today's date and time is 09:08 AM -03 on Friday, July 04, 2025.

detalles sobre simulaciones
modelos de redes neuronales
más claro y conciso

