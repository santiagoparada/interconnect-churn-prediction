# Interconnect — Predicción de fuga de clientes (Churn)

**Proyecto final de Data Science · TripleTen**  
**Estado:** Sprint 1 en curso — `contract.csv` investigado y cerrado en `notebooks/01_contract_eda_clustering.ipynb`; tablas de servicios y datos personales pendientes  
**Ruta de trabajo local (Windows):** `E:\data tree\data science\tripleten bootcamp\sprint 19 proyecto final`  
**Raíz del repositorio Git:** `interconnect-churn-prediction/` dentro de la ruta de trabajo (remoto: `interconnect-churn-prediction`)  
**Responsable de guía técnica:** Senior Data Scientist con criterio de ingeniería de software y buenas prácticas de reproducibilidad.  
**Modalidad:** Investigación guiada: el estudiante propone, implementa y justifica; el tutor formula preguntas, revisa decisiones y ayuda a depurar.  
**Metodología:** CRISP-DM (iterativa).

## 1. Contexto y objetivo

Interconnect quiere identificar clientes con riesgo de cancelar sus servicios para diseñar acciones de retención. El problema académico consiste en desarrollar y comparar modelos de clasificación binaria. Las métricas indicadas en el enunciado son **AUC-ROC (principal)** y **Recall (adicional)**.

Este proyecto no comienza por la selección de algoritmos. Primero debemos comprender qué información registró la empresa, a quién representa cada fila y qué patrones merecen estudiarse.

## 2. Fuentes disponibles

La plataforma de TripleTen contiene cuatro archivos en `/datasets/final_provider/`:

| Archivo | Área a investigar | Pregunta inicial |
|---|---|---|
| `contract.csv` | Contratación y cobros | ¿Cuál es la unidad de registro y cómo se documenta la cancelación? |
| `internet.csv` | Servicios de internet | ¿Incluye únicamente clientes con internet? |
| `personal.csv` | Datos del cliente | ¿Hay una fila por cliente? |
| `phone.csv` | Servicios telefónicos | ¿Incluye únicamente clientes con telefonía? |

Copia local en `data/raw/` (ignorada por Git). Hasta ahora solo `contract.csv` se ha investigado en profundidad (ver sección 11); `internet.csv`, `phone.csv` y `personal.csv` tienen únicamente la auditoría estructural inicial. No interpretar una tabla ausente como un dato faltante antes de comprobar su significado.

## 3. Preguntas de investigación — propuestas del estudiante

### 3.1 Combinaciones de servicios
- ¿Cuántos clientes contrataron solo telefonía, solo internet o ambos?
- ¿Cuántos servicios o complementos tiene cada cliente? ¿Qué significa realmente tener “todos” los servicios?
- ¿Cómo se distribuyen permanencia, cargos mensuales y abandono según el número y la combinación de servicios?
- ¿Existen asociaciones distintas según tipo de contrato o método de pago?

### 3.2 Perfiles y características personales
- ¿Qué asociaciones aparecen al combinar género, pareja y dependientes con servicios como protección de dispositivos, soporte técnico y copias de seguridad?
- ¿Se observan diferencias por perfiles en las tasas de abandono o duración contractual?
- Evitar inferir motivos psicológicos individuales a partir de atributos: describir asociaciones y contrastar hipótesis, no afirmar causalidad.

### 3.3 Contratos, pagos y facturación
- ¿Qué valores y frecuencias aparecen realmente en `Contract` y `PaymentMethod`?
- ¿Qué relación existe entre `PaperlessBilling`, condiciones del contrato y permanencia?
- ¿Cómo se relacionan `MonthlyCharges` y `TotalCharges` con abandono y duración? ¿Qué mide exactamente cada variable?
- ¿La permanencia difiere entre grupos comparables?

### 3.4 Patrones no evidentes y observaciones atípicas
- ¿Una segmentación descriptiva es suficiente o un método de clustering descubre agrupaciones adicionales?
- ¿Qué observaciones atípicas aparecen? ¿Son errores, casos legítimos o segmentos poco frecuentes?
- Investigar agrupaciones **solo si** el EDA justifica su utilidad y se puede escoger una medida de similitud adecuada.

## 4. Distinciones metodológicas que debemos preservar

- **Asociación ≠ causalidad.** Una característica puede correlacionarse con abandono sin provocarlo.
- **Perfil ≠ trayectoria.** Las fechas de inicio y fin no garantizan un historial del comportamiento del mismo cliente. No modelar una serie temporal individual sin observaciones repetidas.
- **Objetivo ≠ característica predictiva.** Una fecha de cancelación puede servir para construir la etiqueta, pero no debe filtrar la respuesta al modelo.
- **Ausencia de fila ≠ NaN.** Puede significar que el servicio no fue contratado; requiere verificación antes de rellenar valores.
- **Outlier ≠ error.** Primero investigar; después decidir cómo tratarlo.
- **No modificar datos originales.** Mantener los CSV en `data/raw/` sin alteraciones.

## 5. Plan de investigación con CRISP-DM

### Fase 1 — Comprensión del negocio
- Reformular el problema y las decisiones de retención.
- Definir a quién se busca identificar, en qué momento y qué información estaría disponible.
- Identificar métricas exigidas: AUC-ROC y Recall.

### Fase 2 — Comprensión de datos
- Inspeccionar **cada CSV por separado**: filas, columnas, tipos, ejemplos, valores ausentes, duplicados y cardinalidades.
- Comprobar unicidad y correspondencia del identificador de cliente en las cuatro tablas.
- Entender por qué difieren las dimensiones y qué clientes aparecen en más de una tabla.
- Formular hipótesis contrastables y realizar EDA por servicios, cobros, contratos, duración y atributos personales.
- Documentar tablas y gráficos con interpretación, no solo imágenes.

### Fase 3 — Preparación de datos
- Justificar la estrategia de unión por identificador tras auditar claves y cobertura.
- Definir cómo generar la etiqueta de Churn usando exclusivamente la información pertinente.
- Identificar variables con riesgo de fuga de información.
- Decidir imputación, codificación y transformaciones solo después del EDA.
- Probar características derivadas, por ejemplo el recuento de servicios, si las definiciones lo permiten.
- Diseñar un esquema de particiones que evite contaminación entre entrenamiento, validación y prueba.

### Fase 4 — Modelado
- Comparar al menos dos modelos base sin balanceo de clases.
- Explorar una técnica de manejo del desbalance y optimización de hiperparámetros.
- Considerar clustering como experimento exploratorio opcional, no como requisito previo al clasificador.

### Fase 5 — Evaluación
- Comparar modelos con AUC-ROC y Recall.
- Seleccionar el modelo a partir de la validación; reservar el conjunto de prueba para evaluación final.
- Interpretar errores, limitaciones y utilidad en lenguaje de negocio.

### Fase 6 — Despliegue / transferencia
- Entregar notebook, conclusiones y código reproducibles.
- Documentar cómo podrían utilizarse las predicciones en retención.
- Evaluar un prototipo de despliegue **solo como extensión posterior**, sin desplazar los requisitos académicos.

**CRISP-DM no es una línea rígida:** los descubrimientos pueden llevarnos a revisar preguntas, variables o procesamiento.

## 6. Estructura inicial sugerida del repositorio

```text
interconnect-churn-prediction/
├── README.md
├── PROJECT_CONTEXT.md
├── .gitignore
├── requirements.txt                 # definir tras revisar el entorno
├── data/
│   └── raw/                         # CSV originales, fuera de Git si corresponde
├── notebooks/
│   └── 01_contract_eda_clustering.ipynb   # hito cerrado: EDA contractual + clustering de desertores
├── src/                              # utilidades reutilizables cuando sean necesarias
├── reports/
│   └── figures/                     # gráficos seleccionados
└── docs/
    └── decision_log.md              # decisiones, evidencia y pendientes
```

No crear carpetas ni módulos vacíos innecesarios. La estructura crecerá con las necesidades del proyecto.

## 7. Flujo de Git / Claude Code

1. Trabajar localmente en VS Code y Jupyter.
2. Usar ramas o commits pequeños y descriptivos por avance verificable.
3. Revisar `git status` y `git diff` antes de permitir commits o push.
4. **Nunca** subir datos reales, credenciales, outputs sensibles o archivos pesados sin revisar permisos y condiciones de uso.
5. Claude Code ayuda con organización, documentación, pruebas y Git; no toma decisiones metodológicas automáticamente.
6. Mantener notebooks ejecutables desde el comienzo y conclusiones explicables por el estudiante.

## 8. Bitácora inicial de decisiones

| Estado | Decisión o cuestión | Criterio |
|---|---|---|
| Acordado | EDA por tabla antes del merge | Comprender granularidad y cobertura |
| Acordado | Explorar interacciones entre servicios y datos personales | Hipótesis contrastables, sin inferir causalidad |
| Acordado | Evaluar número de servicios como característica candidata | Validar definición y señal predictiva |
| Pendiente | Tipo de unión | Auditar claves y presencia/ausencia por tabla |
| Pendiente | Construcción final de la variable objetivo | Verificar formato real de las fechas |
| Pendiente | Series temporales o análisis de duración | Comprobar si existen registros históricos |
| Realizado (exploratorio) | Clustering retrospectivo de desertores | K-Means k = 3, Silhouette 0,513, ARI 1,000; perfiles descriptivos, no probabilidades (sección 11.4) |
| Pendiente | Fecha de corte / extracción | `2020-02-01` es candidata, no confirmada |
| Pendiente | Política de publicación de CSV | Verificar licencia y condiciones de TripleTen |

## 9. Próximo paso — sin adelantar soluciones

**Estudiar individualmente `internet.csv` y `phone.csv` en `notebooks/02_eda_servicios.ipynb`, y después `personal.csv`, antes de cualquier unión.**

Para cada tabla registrar:
- Unidad de observación (qué representa una fila).
- Dimensiones y nombres de variables.
- Tipos de datos y muestras pequeñas.
- Ausencias y duplicados.
- Cardinalidad del identificador.
- Preguntas que surgen de la inspección.

Solo después contrastar los conjuntos de IDs entre tablas y estudiar relaciones posibles.

## 10. Gobierno de sprints y milestones

Consultar `README.md` para el mapa de M0 a M8, y `ROADMAP.md` para checklists y criterios de cierre. Cada cambio metodológico se registra en `docs/decision_log.md`; cada hipótesis en `docs/hypotheses.md`.

## 11. Resultados consolidados — `contract.csv`

Fuente: `notebooks/01_contract_eda_clustering.ipynb` (hito cerrado el 2026-10-24; código, orden de ejecución y salidas congelados). Cifras tomadas de las salidas guardadas.

### 11.1 Población (hechos observados)
- 7.043 clientes contractuales.
- 1.869 cancelaciones registradas (`EndDate` distinto de `"No"`).
- Prevalencia histórica de abandono: **26,5 %**.

### 11.2 Calidad de datos (hechos observados)
- `customerID` es único en `contract.csv`: 7.043 valores distintos, sin nulos ni repetidos.
- `TotalCharges` presenta 11 valores representados mediante espacios; todos con `BeginDate = 2020-02-01` y sin baja. Permanecen sin imputar.
- **Supuesto no confirmado:** `2020-02-01` es una posible referencia temporal, pero no ha sido confirmada como fecha oficial de extracción.

### 11.3 Análisis económico de los desertores (hechos observados)
- `TotalCharges` acumulado entre desertores: **2.862.926,90**.
- Correlación entre permanencia final y `TotalCharges`: Pearson **0,954**; Spearman **0,971**.
- Error porcentual absoluto mediano de `MonthlyCharges × meses` frente a `TotalCharges`: **1,77 %**.
- El **94,17 %** de los desertores tiene un error absoluto igual o inferior al 10 %.

### 11.4 Clustering retrospectivo (experimento exploratorio)
- Algoritmo: K-Means.
- Características: duración final hasta la baja y `MonthlyCharges`.
- Estandarización: `StandardScaler`.
- Clusters seleccionados: **3**.
- Silhouette Score: **0,513**.
- ARI: **1,000** en cinco inicializaciones (semillas 0, 21, 42, 99, 123).

**Interpretación obligatoria:** los clusters son **perfiles retrospectivos de clientes que ya abandonaron**, no probabilidades de abandono. No se entrenaron con clientes activos, por lo que no discriminan entre quien se va y quien se queda.

### 11.5 Limitaciones
- El clustering incluye exclusivamente desertores.
- La fecha de corte no está confirmada.
- La duración final y el gasto acumulado a la fecha de baja **no son predictores válidos**: usarlos en el modelo supervisado introduciría fuga de información. Las características predictivas deberán definirse respecto a un corte temporal.
- El ARI mide estabilidad frente a la inicialización, no robustez entre muestras ni espacios de características.
- Las asociaciones con contrato o pago no implican causalidad.
