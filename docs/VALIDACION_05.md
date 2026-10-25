# Validación disponible del notebook 05

Fecha: 2026-10-25.

## Qué se verificó

- Validez estructural `.ipynb` mediante `nbformat.validate`.
- Ejecución top-to-bottom usando `nbclient` con tablas **sintéticas** creadas en `tempfile.TemporaryDirectory`.
- Universo sintético de 7.043 clientes y `Churn` simulado en 1.869 registros.
- 5.517 clientes con registro de internet, 6.361 con teléfono, unión completa (4.835 ambos, 682 solo internet, 1.526 solo teléfono) solo en el **test artificial**.
- Persistencia de `customerID` único y conservación del número de clientes.
- Identificación de no-internet y no-phone, conversiones numéricas y verificación de 11 `TotalCharges` blancos sintéticos.
- `OneHotEncoder` sobre tres columnas nominales del test (3+4+3 categorías), 16 binarias, 2 numéricas; **28 columnas numéricas y una columna objetivo**, con `NaN` prohibidos y Churn excluido de X.
- Exportación de `clientes_integrados.csv`, `clientes_modelado_base.csv`, `clientes_codificados_eda.csv`, `diccionario_features_05.csv` a carpeta temporal.
- Se generaron nueve figuras en salidas del notebook de prueba.

## Ejecución en el repositorio real (2026-10-25)

Integración realizada con Claude Code en el repositorio local, con Python 3.14, pandas 3.0.1, scikit-learn 1.8.0, nbformat 5.10.4, nbclient 0.10.4 e ipykernel 7.2.0.

1. `nbformat.validate`: válido para los notebooks 01–05.
2. `python tests/test_notebook05_sintetico.py`: **PASS** — `encoded: (7043, 29)`, integrada 7.043 × 26, modelado 7.043 × 22, 9 figuras.
3. **Ejecución con los cuatro CSV reales** (`nbclient`, de arriba a abajo, salidas guardadas en el notebook): 0 errores, 9 figuras.

### Cifras observadas con datos reales

| Control | Esperado (handoff) | Observado |
| --- | --- | --- |
| Filas `contract` / `personal` / `internet` / `phone` | 7.043 / por verificar / 5.517 / 6.361 | 7.043 / 7.043 / 5.517 / 6.361; IDs únicos, sin huérfanos ni nulos |
| Internet ∩ teléfono / solo internet / solo teléfono / ninguno | — | 4.835 / 682 / 1.526 / 0 |
| Cancelaciones | 1.869 (≈ 26,5 %) | 1.869 (26,54 %) |
| `TotalCharges` en blanco | 11 | 11, todos con `BeginDate = 2020-02-01` y `EndDate = No` |
| Columnas candidatas originales | 21 | 21 (16 binarias + 3 multiclase + 2 numéricas) |
| Categorías OHE | 3 + 4 + 3 | `Type` 3, `PaymentMethod` 4, `InternetService` 3 (`DSL`, `Fiber optic`, `No`) |
| Matriz numérica EDA | 28 + `Churn` | 7.043 × 28 + `Churn`; sin `NaN`, todo numérico; `Churn` fuera de X |
| Variables de clustering | sin `Churn` | 19 comerciales, sin `Churn` ni atributos personales |
| k elegido (silhouette, sin `Churn`) | — | k = 2; silhouette 0,242 (k = 3: 0,238; k = 6: 0,192); todos los k superan el mínimo de 212 clientes |
| Cluster de menor / mayor tasa | — | 2.931 clientes, 16,58 %, 486 bajas / 4.112 clientes, 33,63 %, 1.383 bajas (74 % del total) |

Exportados en `data/processed/` (ignorado por Git): `clientes_integrados.csv` (7.043 × 26), `clientes_modelado_base.csv` (7.043 × 22), `clientes_codificados_eda.csv` (7.043 × 29) y `diccionario_features_05.csv` (28 × 4).

**Lectura metodológica:** la silhouette es baja en todos los k, por lo que la estructura de clusters es débil. Esta tabla registra observaciones; la interpretación de negocio corresponde a las secciones 8.6 y 10 del notebook, pendientes de redacción por el responsable.

## No verificado

- Valor predictivo fuera de muestra de cualquier variable o cluster (requiere notebook 06).
- Estabilidad de los clusters ante remuestreo o con otras semillas.
- Disponibilidad temporal de `MonthlyCharges` y de los servicios antes de la baja.

## Ejecutar localmente

```bash
python tests/test_notebook05_sintetico.py
```

Para cifras reales: abrir `notebooks/05_integracion_clientes.ipynb` en VS Code con el entorno local que contiene `data/raw/`, seleccionar kernel e iniciar `Run All`. Inspeccionar resultados e incluir conclusiones reales verificadas en README/contexto solo tras completar el experimento.
