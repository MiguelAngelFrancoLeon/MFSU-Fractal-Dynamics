# Modelo Fractal Estocástico Unificado (MFSU) –

**Autor**: Miguel Ángel Franco León, Creador del MFSU  
**ORCID**: [https://orcid.org/0009-0003-9492-385X]  
**Contacto**: [mf410360@gmail.com]

Este repositorio contiene el código, datos y documentación para el **Modelo Fractal Estocástico Unificado (MFSU)**, un marco teórico que unifica dinámicas fractales estocásticas en regímenes clásico y cuántico. El MFSU resuelve inconsistencias de modelos previos mediante un potencial fractal no singular, ruido térmico basado en la ecuación de Langevin y operadores de Lindblad dimensionalmente consistentes. Sus aplicaciones incluyen redes ópticas cuánticas, crecimiento de quasicristales y plasmones fractales.

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

El **Modelo Fractal Estocástico Unificado (MFSU)** es un avance en el modelado de sistemas complejos con dinámicas fractales y estocásticas. Sus características clave son:
- **Clásico**: Dinámica de una partícula en un potencial fractal no singular con ruido térmico descrito por la ecuación de Langevin.
- **Cuántico**: Evolución de la densidad cuántica mediante una ecuación de Lindblad con operadores de decoherencia físicamente fundamentados.
- **Conexión Clásico-Cuántica**: Correspondencia explícita a través de ecuaciones de Ehrenfest con ruido.
- **Cálculo de Dimensión Fractal**: Algoritmo de conteo de cajas para trayectorias clásicas y densidades cuánticas, con resultados $d_n \in [1.5, 1.8]$.

El modelo se valida mediante simulaciones con parámetros realistas ($V_0 = 0.1$ eV, $a = 100$ nm, $\gamma_x = 0.1$ eV) y tiene aplicaciones en:
- Redes ópticas cuánticas (implementación con hologramas digitales).
- Crecimiento de quasicristales (simulación de patrones fractales).
- Plasmones fractales (modos de localización en nanoestructuras).

Consulta el artículo asociado en `docs/MFSU_paper.pdf` para más detalles.

## Instalación

Sigue estos pasos para configurar el entorno y ejecutar las simulaciones:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/MiguelAngelFrancoLeon/MFSU-Fractal-Dynamics.git
   cd MFSU-Fractal-Dynamics

Instala las dependencias (requiere Python 3.8+):bash

pip install -r requirements.txt

Dependencias necesarias:Python 3.8 o superior
NumPy
SciPy
Matplotlib
(Opcional) Jupyter para explorar los cuadernos en notebooks/.

Verifica la instalación:
Ejecuta el script de prueba:bash

python tests/test_potential.py

UsoPara reproducir las simulaciones del artículo:Navega al directorio de scripts:bash

cd scripts

Ejecuta la simulación principal:bash

python simulate_fractal_dynamics.py

Resultados:Las figuras se guardan en figures/ (por ejemplo, trayectorias clásicas y densidades cuánticas).
Los datos de salida se guardan en data/ (por ejemplo, dimensiones fractales calculadas).

Parámetros:
Los parámetros predeterminados están en config.yaml. Ejemplo:yaml

V0: 0.1  # Amplitud del potencial (eV)
a: 100e-9  # Escala espacial (m)
T: 300  # Temperatura (K)
kappa: 1e-12  # Coeficiente de fricción (kg/s)

Exploración interactiva:
Usa el cuaderno Jupyter en notebooks/exploration.ipynb para visualizar resultados de forma interactiva.

Estructura del Repositoriosrc/: Código fuente (por ejemplo, funciones para el potencial fractal y simulaciones).
data/: Datos de entrada y salida de las simulaciones.
figures/: Figuras generadas (PNG y PDF).
docs/: Documentación, incluido el artículo en PDF (MFSU_paper.pdf).
scripts/: Scripts para reproducir resultados.
tests/: Pruebas unitarias.
notebooks/: Cuadernos Jupyter para exploración interactiva.
requirements.txt: Dependencias de Python.
config.yaml: Parámetros de simulación.
Los resultados clave incluyen:Trayectorias Clásicas: Dimensión fractal dn=1.78±0.05d_n = 1.78 \pm 0.05d_n = 1.78 \pm 0.05
 (ver figures/classical_trajectory.png).
Densidades Cuánticas: Dimensión fractal dn=1.52±0.03d_n = 1.52 \pm 0.03d_n = 1.52 \pm 0.03
 (ver figures/quantum_density.png).
Entropía de Von Neumann: Crecimiento logarítmico, SvN∝ln⁡tS_{\text{vN}} \propto \ln tS_{\text{vN}} \propto \ln t
.

Trayectoria Clásica
Densidad CuánticaCitaSi usas este código o modelo, cita el artículo:Franco-León, M. A. (2025). Modelo Fractal Estocástico Unificado: Fundamentos Matemáticos y Aplicaciones Innovadoras. [En preparación].
LicenciaEste proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.ContactoPara preguntas, sugerencias o colaboraciones, contacta a:Miguel Ángel Franco León
Correo: mf410360@gmai.com
GitHub: MiguelAngelFrancoLeon





