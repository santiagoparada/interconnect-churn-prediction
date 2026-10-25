# Interconnect · Churn Prediction

**Proyecto final de Data Science · TripleTen · Sprint 19**  
**Última actualización:** 2026-10-25  
**Estado:** EDA individual de las cuatro fuentes realizado (notebooks 01–04) e integración multifuente ejecutada con los CSV reales (notebook 05): codificación numérica para EDA y clustering exploratorio sin `Churn`. **Sin modelos supervisados.** Las conclusiones interpretativas del notebook 05 están pendientes de redacción por el responsable.  
**Enfoque:** comprender primero a los clientes; formular hipótesis, contrastarlas y solo después modelar.  
**Metodología:** CRISP-DM, iterativa, organizada en sprints con criterios de cierre.

## Problema

Interconnect busca identificar clientes con riesgo de cancelar el servicio, para apoyar decisiones de retención. El entregable académico requiere clasificación binaria, comparación de al menos dos modelos base sin balanceo, tratamiento de desbalance/ajuste, evaluación con **AUC-ROC como métrica principal y Recall como adicional**, y un informe orientado a negocio. **Aún no hay resultados de modelado.**

**Pregunta de negocio:** ¿qué características de los contratos, los servicios contratados, los importes mensuales, las formas de pago y los perfiles personales se relacionan con el abandono? ¿Puede un modelo supervisado ordenar correctamente a los clientes según su riesgo para priorizar retención? La exploración describe **asociaciones**, no causas. La fecha de predicción y el horizonte de abandono deben quedar definidos antes del entrenamiento.

## Principios del trabajo

- **Tutoría, no solución automática.** El estudiante plantea hipótesis, escribe código y justifica decisiones. El asistente cuestiona, enseña y revisa; Claude Code mantiene estructura y ayuda con Git bajo autorización.
- **Una observación no es una explicación causal.** Distinguir dato observado, hipótesis y conclusión sustentada.
- **Perfil no es historia temporal.** No afirmar evolución del cliente sin registros longitudinales.
- **Sin fuga de información.** Separar información usada para definir Churn de las características disponibles para la predicción.
- **Datos crudos inmutables.** No publicar los CSV sin confirmar derechos de redistribución. No incorporar datos al control de versiones.
- **Simplicidad profesional.** Código claro, modular cuando se necesite, verificable, reproducible y legible.

## Datos y población

Origen en TripleTen: `/datasets/final_provider/`. Copia local en `data/raw/` (los cuatro CSV, **excluidos de Git**; no se modifican).

| Fuente | Filas (observadas, notebook 05) | Grano | Principales dimensiones |
|---|---:|---|---|
| `data/raw/contract.csv` | 7.043 | `customerID` único | Fechas, tipo de contrato, importe mensual y acumulado, facturación, método de pago |
| `data/raw/personal.csv` | 7.043 | `customerID` único | Género, adulto mayor, pareja, dependientes |
| `data/raw/internet.csv` | 5.517 | `customerID` único | DSL / fibra óptica y seis complementos |
| `data/raw/phone.csv` | 6.361 | `customerID` único | Múltiples líneas |

Ninguna fuente tiene IDs fuera de `contract` ni celdas nulas. **Cancelaciones:** 1.869 de 7.043 (**26,54 %**), recalculadas en el notebook 05 y coincidentes con el notebook 01.

## Ruta de investigación: del EDA independiente a la integración

| Paso | Notebook | Pregunta investigada | Hallazgo o decisión (evidencia guardada en el notebook) | Estado |
|---|---|---|---|---|
| 01 | `01_contract_eda_clustering.ipynb` | ¿Cómo se relacionan contratos, pagos y cargos con la cancelación? | Churn por contrato: mes a mes 42,7 %, anual 11,3 %, dos años 2,8 %. `TotalCharges` y permanencia final: Pearson 0,954, Spearman 0,971. `PaymentMethod` χ² = 648,14 (V = 0,303); `PaperlessBilling` χ² = 258,28 (V = 0,191). **Clustering A** (solo 1.869 desertores; duración final + `MonthlyCharges`): k = 3, silhouette 0,513, ARI 1,000. **Clustering B** (7.043 clientes; contrato, pago, facturación y cargo): k = 6, tasas de churn por cluster entre 4,18 % y 53,42 %. Ambos son descriptivos, sin ganancia predictiva demostrada. | Cerrado |
| 02 | `02_eda_internet.ipynb` | ¿Qué cambia entre tecnologías y complementos? | 5.517 clientes: fibra 3.096, DSL 2.421. DSL relativamente más seguridad/soporte; fibra más streaming. Mediana de 3 complementos en ambas: la **composición** distingue más que la cantidad. | Completado |
| 03 | `03_eda_phone.ipynb` | ¿Cómo se contratan las líneas múltiples? | 6.361 registros: `No` 3.390 (53,29 %) y `Yes` 2.971 (46,71 %). | Completado |
| 04 | `04_eda_personal.ipynb` | ¿Cómo se distribuyen atributos personales y `Partner` × `Dependents`? | Revisado y verificado por el responsable; su sección de conclusiones aún no está redactada, por lo que aquí no se transcriben cifras. | Revisado por responsable |
| 05 | `05_integracion_clientes.ipynb` | ¿Qué revelan conjuntamente servicios, precio, contrato, pago, atributos personales y Churn? | Integra las cuatro fuentes; audita cobertura y nulos; construye `Churn`; analiza cruces; codifica 21 características (28 columnas numéricas); clustering sin target; perfiles de baja/alta tasa; exporta cuatro tablas. | **Ejecutado con CSV reales (2026-10-25)**; conclusiones interpretativas pendientes |
| 06 | — | ¿Puede un modelo ordenar a los clientes según su riesgo? | Ver «Próxima fase». | Pendiente |

### Preguntas cruzadas del notebook 05

1. ¿Internet ∪ telefonía cubre los 7.043 clientes? ¿Cuántos están en ambos, solo uno o ninguno?
2. ¿Los cargos mensuales y las tasas de abandono cambian entre solo internet, solo teléfono y ambos?
3. ¿Cómo varían contrato, tecnología, método de pago y facturación electrónica conjuntamente?
4. ¿Qué ocurre con los seis complementos dentro de DSL y fibra óptica?
5. ¿K-Means descubre grupos comerciales con distintas tasas de abandono? ¿Cómo se caracterizan los extremos en tasa **y número absoluto** de bajas?

### Resultados observados con los CSV reales (notebook 05, 2026-10-25)

Cifras leídas de las salidas guardadas. Son asociaciones descriptivas, no efectos causales.

- **Cobertura:** internet ∪ teléfono = 7.043; ambos 4.835 (68,65 %), solo teléfono 1.526 (21,67 %), solo internet 682 (9,68 %), ninguno 0. `personal` cubre a los 7.043.
- **Calidad:** 11 `TotalCharges` en blanco, todos con `BeginDate = 2020-02-01` y sin baja; se conservan como `NaN` sin imputar.
- **Contrato:** 42,71 % / 11,27 % / 2,83 % (confirma el notebook 01).
- **Tecnología:** fibra 41,89 %, DSL 18,96 %, sin internet 7,40 %. Mes a mes × fibra: 54,61 % (n = 2.128).
- **Perfil de servicios:** internet + teléfono 32,80 % (cargo medio 81,76); solo internet 24,93 % (42,03); solo teléfono 7,40 % (21,08).
- **Pago:** Electronic check 45,29 %; mes a mes + Electronic check + PaperlessBilling = 57,70 % (n = 1.397).
- **Complementos:** dentro de cada tecnología, la tasa desciende al aumentar `NumServiciosInternet` (fibra: 60,40 % con 0 a 9,22 % con 6; DSL: 41,16 % a 1,40 %). `SeguridadYSoporte` = 9,01 % frente a 29,78 %.
- **Atributos personales:** `SeniorCitizen` 41,68 % frente a 23,61 %; sin pareja 32,96 % frente a 19,66 %; sin dependientes 31,28 % frente a 15,45 %; género 26,92 % frente a 26,16 %.
- **Clustering K-Means (19 variables comerciales, sin `Churn`):** silhouette máxima 0,242 con k = 2 (estructura débil). Cluster de menor tasa: 2.931 clientes, 16,58 %, 486 bajas, con sobrerrepresentación de clientes sin internet. Cluster de mayor tasa: 4.112 clientes, 33,63 %, 1.383 bajas (**74 % de todas**), con predominio de fibra y streaming. PCA 2D: 49,9 % de varianza.

## Arquitectura de datos y reglas de integridad

`contract` es la tabla base y se une mediante `LEFT JOIN` por `customerID`, primero con `personal`, después con `internet` y `phone`, usando `validate='one_to_one'`, sin pérdida de clientes. Las columnas `_merge_personal`, `_merge_internet` y `_merge_phone` son trazas temporales de auditoría, no características.

La ausencia de una fila de internet o telefonía se trata como **nulo estructural**, no como error: `InternetService = "No"`, `No internet service` en los complementos y `No phone service` en `MultipleLines`, con las banderas `TieneInternet` y `TieneTelefono`. Un nulo dentro de un registro presente detiene la ejecución. Si existieran clientes sin ningún servicio, el notebook interrumpe el relleno.

## Preparación de características (notebook 05)

- **Target** `Churn`: `EndDate = "No"` → `0`; fecha válida de cancelación → `1`.
- **Excluidas del conjunto candidato:** `customerID`, `EndDate`, `BeginDate`, `TotalCharges`. `BeginDate` se reserva para una posible antigüedad válida al corte; `TotalCharges` se conserva solo para EDA hasta validar su disponibilidad temporal.
- **21 características originales**, verificadas con los datos reales:
  - **16 binarias (0/1):** `PaperlessBilling`, `Partner`, `Dependents`, `gender` (Female = 0, Male = 1, sin orden), siete servicios (`OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `MultipleLines`), `SeniorCitizen`, `TieneInternet`, `TieneTelefono`, `SeguridadYSoporte`, `StreamingCompleto`.
  - **3 multiclase con `OneHotEncoder(drop=None)`:** `Type` (3), `PaymentMethod` (4), `InternetService` (3) → 10 columnas.
  - **2 numéricas:** `MonthlyCharges` y `NumServiciosInternet`.
  - Resultado: **28 columnas numéricas + `Churn`**. `Churn` no forma parte de X ni del espacio de clustering.
- Un `0` en un complemento puede significar «no contratado» o «sin servicio principal»; se distingue con `TieneInternet`/`TieneTelefono` e `InternetService_No`.
- La matriz numérica para **EDA** se ajusta sobre todas las filas y **no** debe usarse para entrenar o evaluar modelos. En ML supervisado: split primero y `OneHotEncoder`, escalado e imputación ajustados solo en `train` dentro de un `Pipeline`.

### Archivos generados al ejecutar el notebook 05 (ignorados por Git)

| Archivo | Forma | Uso |
|---|---|---|
| `data/processed/clientes_integrados.csv` | 7.043 × 26 | Tabla analítica completa; no apta directamente para entrenamiento |
| `data/processed/clientes_modelado_base.csv` | 7.043 × 22 | 21 atributos originales + `Churn`; insumo para un pipeline supervisado **train-only** |
| `data/processed/clientes_codificados_eda.csv` | 7.043 × 29 | 28 atributos numéricos + `Churn`; **solo EDA/clustering** |
| `data/processed/diccionario_features_05.csv` | 28 × 4 | Linaje y semántica de las variables codificadas |

## Clustering exploratorio

K-Means compara `k = 2..6` y elige por silhouette y tamaño mínimo **sin usar `Churn`**. Solo después se calcula la tasa de churn por segmento, informando tanto el **riesgo relativo** (tasa) como el **impacto total** (cancelaciones). PCA ayuda a visualizar, pero no demuestra separabilidad supervisada. Los clusters de los notebooks 01 y 05 usan poblaciones y variables distintas: **sus números de cluster no se corresponden**. `Cluster` no se exporta como predictor.

## Próxima fase: aprendizaje supervisado (notebook 06)

1. Definir fecha de corte, horizonte de predicción y disponibilidad temporal de las variables.
2. Separar train/validation/test (estratificación y semilla reproducible; no usar test para selección).
3. `Pipeline` con transformaciones ajustadas en **train**: `OneHotEncoder`, escalado cuando corresponda, imputación solo si es necesaria.
4. Regresión logística sin balanceo como baseline; comparar `class_weight='balanced'` y sobremuestreo solo dentro de train; añadir una segunda familia de modelos.
5. Evaluar **AUC-ROC** (principal) y **Recall** (adicional), junto con precisión, matriz de confusión y umbrales según el negocio.
6. Seleccionar en validación; evaluar en test una sola vez y documentar límites y recomendaciones de retención.

## Ruta de trabajo y entregables

| Sprint | Fase CRISP-DM | Trabajo | Milestone / criterio de cierre |
|---|---|---|---|
| **0. Base reproducible** | Comprensión del negocio | Git, documentación, reglas, estructura, ingesta | **M0:** repo local inicializado, README, contexto y bitácora; sin CSV en Git |
| **1. Radiografía de tablas** | Comprensión de datos | EDA individual: granularidad, esquema, nulos, categorías, tamaños, claves | **M1:** fichas de 4 tablas y preguntas documentadas; ninguna limpieza arbitraria |
| **2. Población y relaciones** | Comprensión de datos | Intersecciones de IDs, cobertura, servicios exclusivos/combinados, auditoría de llaves | **M2:** estrategia de unión argumentada y universo de clientes definido |
| **3. Comportamientos e hipótesis** | Comprensión de datos | Contratos, permanencia, cargos, pagos, número de servicios, cruces demográficos, atípicos | **M3:** evidencia descriptiva con gráficos/tablas y límites interpretativos |
| **4. Dataset analítico** | Preparación | Objetivo Churn, manejo de ausencias, fechas, ingeniería de características, codificación, split sin leakage | **M4:** dataset y pipeline reproducibles, validaciones básicas |
| **5. Modelos base** | Modelado | ≥2 modelos sin balanceo, evaluación en validación AUC-ROC y Recall | **M5:** comparación baseline honesta y reproducible |
| **6. Experimentos controlados** | Modelado | Desbalance, hiperparámetros, análisis de errores; clustering opcional si aporta | **M6:** registro de experimentos y modelo candidato justificado |
| **7. Evaluación e informe** | Evaluación | Test final reservado, AUC-ROC/Recall, límites y recomendaciones de negocio | **M7:** informe y notebook final auditables |
| **8. Transferencia opcional** | Despliegue | Prototipo o propuesta operativa de uso; no sustituye entregable | **M8:** alcance y restricciones documentadas si se realiza |

**Situación actual:** M2 y la parte descriptiva de M3 tienen evidencia ejecutada en el notebook 05; su cierre formal requiere las conclusiones del responsable. M4 está parcialmente preparado (tabla base y decisiones de exclusión), pero el split y el pipeline pertenecen al notebook 06.

**Regla:** la secuencia se revisa al descubrir nueva evidencia. Nunca optimizar con el conjunto de prueba. El clustering no es requisito ni implica automáticamente un mejor clasificador.

## Estructura

```text
interconnect-churn-prediction/
├── README.md
├── PROJECT_CONTEXT.md             # contexto histórico y resultados de contract.csv
├── ROADMAP.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── raw/                       # CSV originales, ignorados por Git
│   └── processed/                 # salidas del notebook 05, ignoradas por Git
├── notebooks/
│   ├── 01_contract_eda_clustering.ipynb
│   ├── 02_eda_internet.ipynb
│   ├── 03_eda_phone.ipynb
│   ├── 04_eda_personal.ipynb
│   └── 05_integracion_clientes.ipynb
├── tests/
│   └── test_notebook05_sintetico.py
├── src/
├── reports/
│   └── figures/
└── docs/
    ├── PROJECT_CONTEXT.md         # contrato operativo vigente (2026-10-25)
    ├── DECISIONS.md               # decisiones metodológicas D01–D16
    ├── HANDOFF_2026-10-25.md      # punto de continuación
    ├── VALIDACION_05.md           # pruebas sintéticas y ejecución real
    ├── decision_log.md
    ├── hypotheses.md
    └── data_dictionary.md
```

## Reproducibilidad

**VS Code:** abrir la carpeta `interconnect-churn-prediction/`, abrir el notebook, seleccionar un kernel de Python con `pandas`, `numpy`, `matplotlib`, `scipy`, `scikit-learn`, `ipykernel` e `IPython`, y ejecutar **Restart Kernel → Run All**. Los notebooks buscan los CSV en `data/raw/` tanto desde la raíz como desde `notebooks/`.

**Test sintético del notebook 05** (no usa datos reales; requiere además `nbformat` y `nbclient`):

```bash
python tests/test_notebook05_sintetico.py
```

El test valida la lógica de integración, codificación y exportación; **no sustituye** la ejecución con las fuentes originales.

## Flujo de trabajo

1. Elegir una pregunta y registrar hipótesis/criterio de contraste.
2. Ejecutar una inspección o experimento pequeño, sin modificar datos originales.
3. Escribir evidencia, interpretación, incertidumbres y siguiente decisión.
4. Revisar cambios (`git status`, `git diff`), hacer commits temáticos y **push solo con aprobación**.
5. Actualizar README, bitácora e hitos al cerrar cada sprint.

## Documentos de continuidad

- `docs/PROJECT_CONTEXT.md`: objetivo, contratos de datos y estado de validación.
- `docs/DECISIONS.md`: registro explícito de decisiones metodológicas, riesgos y preguntas abiertas.
- `docs/HANDOFF_2026-10-25.md`: punto exacto de continuación.
- `docs/VALIDACION_05.md`: alcance de la prueba sintética y resultados de la ejecución real.

**Siguiente acción:** redactar las conclusiones del notebook 05 (secciones 8.6 y 10) a partir de las salidas reales; después, abrir el notebook 06 con la definición temporal y el split.
