# Registro de hipótesis

Cada hipótesis debe separar una relación que **podemos observar** de una explicación que **no podemos afirmar causalmente**.

| ID | Hipótesis por contrastar | Variables candidatas (confirmar nombres) | Estado |
|---|---|---|---|
| H01 | Cantidad/combinación de servicios se asocia con abandono y duración | internet, phone, servicios extra, contrato | Sin probar |
| H02 | Tipo de contrato se asocia con permanencia y abandono | `Type`, `BeginDate`, `EndDate` | Apoyada descriptivamente: abandono 42,7 % mes a mes, 11,3 % un año, 2,8 % dos años (notebook 01). Asociación, no causalidad; sin contraste estadístico formal |
| H03 | Método de pago y facturación sin papel se asocian con abandono | `PaymentMethod`, `PaperlessBilling`, `EndDate` | Apoyada (asociación): `PaymentMethod` χ² = 648,14, gl = 3, V de Cramér = 0,303 (Electronic check 45,3 %); `PaperlessBilling` χ² = 258,28, gl = 1, V = 0,191 (33,6 % vs 16,3 %). La diferencia persiste dentro de cada tipo de contrato. No implica causalidad (notebook 01) |
| H04 | Cargos y permanencia se distribuyen de manera diferente entre grupos | monthly/total charges, duración | Sin probar |
| H05 | Combinaciones de pareja/dependientes/género y servicios de soporte se asocian con patrones diferentes | atributos personales, tech support, backup, device protection | Sin probar |
| H06 | Agrupaciones exploratorias revelan subgrupos no evidentes en EDA | variables transformadas; similitud | Parcial: entre desertores, K-Means (duración final, `MonthlyCharges`) separa 3 perfiles, Silhouette 0,513, ARI 1,000. No probado frente a clientes activos ni como señal predictiva |
| H07 | Algunos clientes atípicos representan comportamientos legítimos | distribuciones, reglas de negocio | Sin probar |

## Plantilla por hipótesis

### Hxx — Título
- Pregunta en lenguaje de negocio:
- Unidad de análisis:
- Variables observadas:
- Comparación/estadística prevista:
- Factores de confusión o límites:
- Evidencia obtenida:
- Interpretación (asociación, no causalidad):
- Estado: sin probar / apoyada / no apoyada / inconclusa
