# Contexto operativo — Interconnect Customer Churn Prediction

Actualizado: 2026-10-25 · TripleTen Sprint 19

## Propósito y contrato de calidad

Problema: clasificación binaria de cancelación de servicio. Métrica principal AUC-ROC; métrica secundaria Recall. El objetivo de negocio es priorizar acciones de retención, no diagnosticar causalidad a partir de correlaciones.

## Fuentes

- `contract.csv` (7.043 registros, observado), clave única `customerID`, base de población.
- `personal.csv` (7.043, observado), atributos demográficos/convivencia.
- `internet.csv` (5.517, observado), tecnología y seis extras.
- `phone.csv` (6.361, observado), `MultipleLines`.

Los cuatro CSV viven en `data/raw/` y no se modifican. `data/processed/` recibe versiones derivadas por un notebook reproducible.

## Ubicación de trabajo

- `notebooks/01_contract_eda_clustering.ipynb`: EDA y segmentación contractual.
- `notebooks/02_eda_internet.ipynb`: tecnología y complementos.
- `notebooks/03_eda_phone.ipynb`: múltiples líneas.
- `notebooks/04_eda_personal.ipynb`: revisado y verificado por responsable, sin resultados numéricos suministrados en este handoff.
- `notebooks/05_integracion_clientes.ipynb`: integración, EDA cruzado, codificación numérica para EDA, clustering, exportaciones.
- Notebook 06 aún no creado: preparación ML con split y pipelines train-only.

## Definición y análisis de target

`Churn = 1` si `EndDate` contiene una fecha válida; `Churn = 0` si `EndDate` es `No`. 1.869 cancelaciones / 7.043 clientes (26,54 %), recalculadas con los CSV reales en el notebook 05 (2026-10-25). **Nunca introducir EndDate como predictor**.

## Contrato de integración y categorías

- `LEFT JOIN` desde `contract`, `validate='one_to_one'` para `personal`, `internet` y `phone`.
- Auditar `customerID` nulos, duplicados, huérfanos, intersección/unión de fuentes de servicio y preservación del orden/filas.
- `_merge_*` son marcadores efímeros de auditoría; no features.
- Nulo estructural de servicio: `InternetService='No'`, extras = `No internet service`; `MultipleLines='No phone service'`; mantener flags `TieneInternet` y `TieneTelefono`.
- Nulo dentro de registro presente es anomalía; no rellenar automáticamente.
- `TotalCharges` contiene 11 blancos según EDA 01: convertir a numérico con `NaN` controlado; no imputar sin justificación. No usarlo como feature hasta establecer su disponibilidad temporal.

## Diseño de características

21 originales, excluyendo ID, BeginDate, EndDate y TotalCharges. De ellas: 16 binarias (incluye `gender` nominal binaria codificada sin jerarquía), 3 multiclase nominales (`Type`, `PaymentMethod`, `InternetService`) y 2 numéricas (`MonthlyCharges`, `NumServiciosInternet`). El OneHotEncoder de notebook 05 genera variables numéricas descriptivas sobre el conjunto completo, nunca directamente para test supervisado. Refit del encoder solo en train dentro de pipeline futuro. Para ML conservar variable `Churn` fuera de `X`.

El clustering usa un subconjunto comercial de la matriz numérica con `StandardScaler` solo para precio; excluye `Churn`, atributos personales y variables redundantes como banderas del espacio de distancia. Aún no hay evidencia de valor predictivo adicional del clustering.

## Insights previamente documentados

- EDA contractual: Churn 42,7 % mes a mes; 11,3 % anual; 2,8 % dos años.
- `TotalCharges` y permanencia final: Pearson 0,954; Spearman 0,971. No equivale a capacidad predictiva incremental.
- Internet: DSL favorece relativamente OnlineSecurity y TechSupport; fibra StreamingTV/Movies; medias 2,66 (DSL) vs 2,55 (fibra) extras.
- Phone: 3.390 sin múltiples líneas y 2.971 con ellas.
- Notebook 01 contiene dos clustering distintos: (A) solo los 1.869 desertores, k = 3, silhouette 0,513, ARI 1,000; (B) los 7.043 clientes con contrato, pago, facturación y cargo, k = 6, tasas de churn por cluster entre 4,18 % y 53,42 %. Ninguno demuestra ganancia predictiva adicional.

## Estado de validación

Notebook 05 probado con datos sintéticos (`tests/test_notebook05_sintetico.py`: PASS) y **ejecutado de arriba a abajo con los cuatro CSV reales el 2026-10-25**, sin errores. La codificación real confirma 21 columnas originales → 28 numéricas + `Churn`. Las cifras observadas están en `docs/VALIDACION_05.md`. Las conclusiones interpretativas siguen pendientes de redacción por el responsable; no registrar conclusiones sintéticas como hechos empresariales.

## Principios de trabajo

Cada celda responde a una pregunta; entradas/salidas claras, estadísticas interpretadas con denominador y número de clientes, sin establecer causalidad ni crear targets basados en el futuro, separación train/validation/test, semilla y reproducibilidad. No requiere SQLite ni PostgreSQL para este proyecto.
