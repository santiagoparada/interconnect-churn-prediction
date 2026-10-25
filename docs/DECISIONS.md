# Registro de decisiones metodológicas — Interconnect

Versión: 2026-10-25. Estados: **aplicada en notebook**, **verificada con CSV reales** (ejecución del 2026-10-25, ver `docs/VALIDACION_05.md`) o **planeada**.

| ID | Decisión | Motivo | Estado |
| --- | --- | --- | --- |
| D01 | `contract` como universo de clientes, `LEFT JOIN` 1:1 a otras fuentes | No perder clientes sin servicios opcionales; evitar multiplicar observaciones | Aplicada; verificada con CSV reales (7.043 filas preservadas, sin huérfanos) |
| D02 | Auditar cobertura conjunta internet ∪ phone, además de intersección | La suma de registros sobrecuenta usuarios con ambos servicios | Aplicada; verificada (4.835 ambos, 682 solo internet, 1.526 solo teléfono, 0 ninguno) |
| D03 | Diferenciar nulos estructurales de errores de calidad | No contratar un servicio no equivale a valor desconocido | Aplicada; verificada (0 nulos dentro de registros presentes) |
| D04 | Conservar `EndDate` solo para crear `Churn` | Prevenir fuga del target | Aplicada |
| D05 | Conservar `TotalCharges` como variable de EDA; excluirla provisionalmente de X | Total acumulado y permanencia final pueden contener información poscancelación | Aplicada; revisar disponibilidad temporal |
| D06 | Excluir `BeginDate` como predictor en esta etapa | No existe fecha de corte para calcular antigüedad sin riesgo de fuga | Aplicada; revisar en notebook 06 |
| D07 | Crear `NumServiciosInternet`, `SeguridadYSoporte`, `StreamingCompleto` | Resumir oferta contratada y coocurrencia | Aplicada |
| D08 | Hacer binarios los atributos Yes/No y siete servicios | Evita codificaciones redundantes de servicios opcionales; flags mantienen el contexto | Aplicada, con validación de etiquetas |
| D09 | Usar `OneHotEncoder(drop=None)` en `Type`, `PaymentMethod`, `InternetService` | Son categorías nominales multiclase, no números ordinales | Aplicada para EDA |
| D10 | Conservar las etiquetas legibles en `df_integrado` y exportar matriz numérica separada | Permite interpretación de negocio y experimentación independiente | Aplicada |
| D11 | No usar `clientes_codificados_eda.csv` para entrenar/evaluar ML supervisado | Su codificador se ajusta sobre toda la población; pipeline final exige ajuste solo en train | Aplicada en documentación; verificar en notebook 06 |
| D12 | Clustering comercial K-Means sin `Churn`, k=2..6 con criterio no supervisado | Evita elegir segmentos para maximizar Churn histórico de forma circular | Aplicada; ejecutada con CSV reales (k = 2, silhouette 0,242); interpretación pendiente |
| D13 | Comparar tasa, tamaño y total de cancelaciones de cada cluster | Una tasa alta en un grupo pequeño no significa gran impacto absoluto | Aplicada |
| D14 | No usar `Cluster` directamente como predictor | Etiquetas creadas con datos completos podrían inducir contaminación; valor incremental no probado | Aplicada |
| D15 | Baseline logístico sin balanceo; luego comparar pesos, sobremuestreo y otra familia de modelos | Separar desempeño original de intervenciones sobre desbalance | Planeada para notebook 06 |
| D16 | Métrica principal AUC-ROC y adicional Recall; test reservado | Priorizar discriminación y detección de abandonos con evaluación limpia | Planeada para notebook 06 |

## Riesgos y preguntas abiertas

1. ¿Cuál es la **fecha de corte** y en cuántos días/meses debe predecirse Churn? Sin esto, el target describe estado histórico pero no riesgo prospectivo bien fechado.
2. ¿`MonthlyCharges` y atributos contratados corresponden a un snapshot antes de la baja, o al estado al finalizar? Verificar procedencia temporal, porque incluso atributos sin fecha explícita pueden verse después del evento.
3. ¿Qué hacer con `TotalCharges` disponible a una fecha válida? Eventualmente podría aportar información adicional sobre pagos y permanencia, pero su correlación con tenure exige evaluación incremental.
4. ¿Los 11 blancos de TotalCharges pertenecen a clientes nuevos? Los datos reales lo apoyan (los 11 tienen `BeginDate = 2020-02-01` y siguen activos), pero falta confirmar la fecha de extracción. Sin imputación automática.
5. ¿Debe excluirse o auditarse el uso de `gender` y `SeniorCitizen` por potenciales implicaciones de equidad? Evaluar diferencias por subgrupos antes de uso operacional.
6. ¿Aporta agrupación K-Means poder predictivo fuera de muestra? No asumirlo a partir del EDA.
7. ~~¿Los tamaños y categorías reales son los del handoff?~~ Resuelta el 2026-10-25: coinciden (ver `docs/VALIDACION_05.md`).
8. La silhouette es baja para todos los k (0,19–0,24): ¿merece la pena mantener el clustering comercial en la narrativa, o basta con los cruces descriptivos?
