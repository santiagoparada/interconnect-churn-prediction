# Roadmap de sprints y gates

El README contiene la vista ejecutiva. Este documento sirve para la operación diaria. Ningún sprint se marca completo sin su evidencia.

## Sprint 0 — Infraestructura
- [ ] Crear estructura local sin sobrescribir archivos existentes.
- [ ] `git init` (solo si no existe repositorio) y revisar rama activa.
- [ ] Revisar `.gitignore` **antes** de copiar datasets.
- [ ] Comprobar que `git status` no incluye CSV ni secretos.
- [ ] Decidir con el estudiante si crear repositorio remoto en GitHub; no hacer push sin autorización.
- [ ] Registrar decisión y primer commit documental autorizado.

**Gate M0:** estructura reproducible y documentos visibles; no se han procesado datos.

## Sprint 1 — EDA individual  *(en curso)*
- [x] Auditoría inicial de estructura de las cuatro fuentes (dimensiones, columnas, tipos, nulos, duplicados).
- [x] Análisis individual profundizado de `contract.csv` (unicidad de `customerID`, `TotalCharges` con espacios, fechas, contrato, pago).
- [x] Investigación económica de clientes que abandonaron.
- [x] Primer clustering exploratorio de desertores, validado por silueta y ARI.
- [x] Cierre documental de `notebooks/01_contract_eda_clustering.ipynb` (2026-10-24).
- [x] Exploración detallada de `internet.csv` (`02_eda_internet.ipynb`) y `phone.csv` (`03_eda_phone.ipynb`).
- [x] Exploración detallada de `personal.csv` (`04_eda_personal.ipynb`; sección de conclusiones pendiente).
- [ ] Inspeccionar categorías reales y registrar supuestos sin resolver en las tablas restantes (`docs/data_dictionary.md`).

**Gate M1:** cuatro fichas completadas, código reproducible y primeros hallazgos separados de hipótesis. *Pendiente: conclusiones del notebook 04 y diccionario de datos.*

## Sprint 2 — Universo de clientes y joins
- [x] Comprobar relaciones y cobertura de `customerID` entre tablas (notebook 05).
- [x] Determinar qué significa que un cliente falte en una tabla de servicio (nulo estructural).
- [x] Verificar cardinalidades antes de decidir cómo unir (`validate='one_to_one'`).
- [x] Documentar posibles nulos introducidos por join.
- [x] Construir la unión customer-level de las fuentes.

**Gate M2:** universo de análisis y estrategia de join justificados. *Evidencia ejecutada con datos reales; falta la conclusión escrita del responsable.*

## Sprint 3 — EDA de comportamientos
- [x] Servicios individuales, combinaciones y recuentos (notebook 05, evidencia descriptiva).
- [x] Cargos, contratos, formas de pago, paperless billing (notebook 05, evidencia descriptiva).
- [ ] Interacciones con atributos personales y duración.
- [ ] Detección y revisión de atípicos, sin eliminarlos automáticamente.
- [ ] Comparar los perfiles de desertores con clientes activos, con denominadores válidos.
- [ ] Evaluar si clustering merece un experimento posterior. *(Primer experimento retrospectivo ya realizado en Sprint 1: describe desertores, no estima riesgo.)*

**Gate M3:** hipótesis contrastadas mediante evidencia descriptiva y límites claros.

## Sprint 4 — Preparación
- [ ] Definir Churn y fecha de referencia sin filtrar información futura.
- [ ] Auditar nulos, categorías y variables de fechas.
- [ ] Planear ingeniería de características; registrar definiciones.
- [ ] Preparar características predictivas sin data leakage (excluir duración final y gasto acumulado a la fecha de baja).
- [ ] Diseñar división train/validation/test y procesamiento sin leakage.

**Gate M4:** preparación auditable y reproducible.

## Sprint 5 — Baselines
- [ ] Definir métrica y baseline de referencia.
- [ ] Entrenar ≥2 modelos sin balanceo.
- [ ] Comparar AUC-ROC y Recall en validación.

**Gate M5:** comparación documentada sin usar test para decisiones.

## Sprint 6 — Optimización
- [ ] Elegir al menos una estrategia de desbalance.
- [ ] Ajustar hiperparámetros usando solo datos apropiados.
- [ ] Explorar clustering solo si se justifica y no compromete validación.
- [ ] Registrar configuración y resultados comparables.

**Gate M6:** candidato seleccionado y razones documentadas.

## Sprint 7 — Evaluación y reporte
- [ ] Medir en test reservado una sola vez después de la selección (AUC-ROC principal, Recall adicional).
- [ ] Interpretar AUC-ROC, Recall y errores operativos.
- [ ] Discutir límites y recomendaciones para retención.
- [ ] Verificar ejecución y consistencia del notebook completo.

**Gate M7:** entrega final verificable.

## Sprint 8 — Opcional
- [ ] Definir propuesta o prototipo de uso, con riesgos y condiciones de operación.

**Gate M8:** transferencia opcional documentada.
