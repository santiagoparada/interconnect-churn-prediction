# Diccionario de datos — pendiente de auditoría

**Importante:** no completar definiciones basándose únicamente en el nombre de una columna. Validar contenido y unidad de cada variable.

| Tabla | Variable | Tipo observado | Significado confirmado | Valores/categorías | Nulos | Notas |
|---|---|---|---|---|---|---|
| contract | `customerID` | object | Identificador de cliente; único en la tabla | 7.043 distintos | 0 | Clave candidata para uniones; cobertura entre tablas por verificar |
| contract | `EndDate` | object | Fecha de baja, o `"No"` si no hay baja registrada | `"No"` (5.174) o fecha (1.869) | 0 | Define la etiqueta; no usar como predictor |
| contract | `MonthlyCharges` | float64 | Cargo mensual | 18,25 – 118,75 | 0 | |
| contract | `TotalCharges` | object | Cargo acumulado; ≈ `MonthlyCharges × meses` (error mediano 1,77 % en desertores) | numérico en texto | 11 espacios | Los 11 casos tienen `BeginDate = 2020-02-01`; sin imputar. Acumulado a la baja: riesgo de leakage |
| contract | `BeginDate`, `Type`, `PaperlessBilling`, `PaymentMethod` | object | Ver notebook 01 | | 0 | Pendiente de ficha detallada |
| internet | Por inspeccionar | | | | | |
| personal | Por inspeccionar | | | | | |
| phone | Por inspeccionar | | | | | |

Para cada tabla, registrar: forma, granularidad, unicidad de la clave, cobertura de IDs, categorías y anomalías. Evitar pegar datos personales identificables en documentación pública.
