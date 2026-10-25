# Bitácora de decisiones

Formato: fecha | sprint | pregunta | evidencia disponible | decisión provisional/final | impacto | próximo examen.

| Fecha | Sprint | Tema | Evidencia | Decisión / estado | Próximo paso |
|---|---|---|---|---|---|
| 2026-10-21 | 0 | Enfoque | Enunciado del proyecto y conversación inicial | Acordado: tutoría paso a paso, no respuestas anticipadas | Estructurar repo |
| 2026-10-21 | 0 | Método | Plan propuesto por el estudiante | Acordado: CRISP-DM iterativo y sprints verificables | EDA individual |
| 2026-10-21 | 0 | Clustering | Intuición de agrupaciones y outliers | Pendiente: experimento opcional tras EDA | Revisar variables y distancias |
| 2026-10-21 | 0 | Temporalidad | No se ha demostrado historial longitudinal | No asumir series temporales | Auditar columnas de fechas |
| 2026-10-21 | 0 | Publicación | Datasets provistos en plataforma educativa | No versionar ni publicar CSV sin confirmar permisos | Revisar condiciones |
| 2026-10-21 | 0 | Raíz del repositorio | Archivos del proyecto en una subcarpeta; notas personales y `.zip` en la carpeta padre | Acordado: Git en `interconnect-churn-prediction/` (rama `main`), mismo nombre que el remoto; notas y `.zip` fuera del control de versiones | Primer commit documental |
| 2026-10-21 | 0 | `.gitignore` | Solo `data/` excluía datos; un CSV en otra carpeta se habría publicado | Se ignoran `*.csv`, `*.xlsx`, `*.zip`, etc. en todo el repo, y archivos de credenciales | Verificar `git status` tras copiar CSV a `data/raw/` |
| 2026-10-21 | 0 | Licencia | Proyecto educativo; datos propiedad de TripleTen | Pendiente: decidir antes de hacer público el repositorio | Elegir licencia de código/documentación |
| 2026-10-24 | 1 | Cierre notebook 01 | 1.869 desertores; K-Means k = 3; Silhouette 0,513; ARI 1,000 | Final: conservar `01_contract_eda_clustering.ipynb` como investigación independiente congelada | `02_eda_servicios.ipynb` |
| 2026-10-25 | 1 | Ampliación notebook 01 | Clustering de los 7.043 clientes (contrato, pago, facturación, cargo): k = 6, churn por cluster 4,18 %–53,42 % | Añadido como experimento B; el clustering A de desertores se conserva sin cambios | Contrastar con la integración |
| 2026-10-25 | 1 | EDA individual de servicios y datos personales | `02_eda_internet`, `03_eda_phone`, `04_eda_personal` | Se usa un notebook por tabla en lugar del `02_eda_servicios.ipynb` previsto | Integración |
| 2026-10-25 | 2–3 | Integración y EDA multifuente | Notebook 05 ejecutado con CSV reales: 7.043 clientes, cobertura completa internet ∪ teléfono, 28 columnas numéricas + `Churn`, K-Means k = 2 (silhouette 0,242) | Decisiones D01–D16 en `docs/DECISIONS.md`; resultados en `docs/VALIDACION_05.md` | Conclusiones del notebook 05; notebook 06 |

## Entradas detalladas

### 2026-10-24 · Sprint 1 · Cierre del EDA contractual y del primer clustering
- **Pregunta:** ¿cómo conservar el análisis de `contract.csv` y el clustering retrospectivo sin mezclarlo con la preparación del modelo predictivo?
- **Evidencia:** 1.869 desertores de 7.043 clientes (26,5 %); K-Means sobre duración final y `MonthlyCharges` estandarizadas, tres clusters, Silhouette 0,513 y estabilidad ARI 1,000 en cinco inicializaciones. Salidas guardadas en `notebooks/01_contract_eda_clustering.ipynb`.
- **Opciones consideradas:** continuar en el mismo notebook con las demás tablas; congelarlo y abrir notebooks nuevos por investigación.
- **Decisión y justificación:** conservar el análisis contractual y el primer clustering como investigación independiente, sin modificar código, orden ni salidas. Mantiene la trazabilidad, evita mezclar la investigación retrospectiva con la preparación del modelo predictivo y facilita comparaciones futuras. El archivo `01_contract_eda_clustering_cierre.ipynb` se renombró a su nombre definitivo sin alterar su contenido (SHA-256 idéntico).
- **Riesgos / supuestos (limitaciones):**
  - Clustering exclusivo de desertores: describe perfiles retrospectivos, no estima probabilidades de abandono.
  - Fecha de corte no confirmada (`2020-02-01` es solo candidata).
  - Riesgo de fuga de información si la duración final o el gasto acumulado a la fecha de baja se usan como predictores.
  - El ARI mide estabilidad frente a la inicialización, no frente a otras muestras o características.
- **Siguiente comprobación:** estudiar individualmente los servicios de internet y telefonía (`02_eda_servicios.ipynb`) antes de las uniones.

## Plantilla para nuevas entradas

### AAAA-MM-DD · Sprint N · [título]
- **Pregunta:**
- **Evidencia:**
- **Opciones consideradas:**
- **Decisión y justificación:**
- **Riesgos / supuestos:**
- **Siguiente comprobación:**
