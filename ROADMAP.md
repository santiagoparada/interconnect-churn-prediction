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

## Sprint 1 — EDA individual
- [ ] Examinar `contract.csv`, `internet.csv`, `personal.csv` y `phone.csv` por separado.
- [ ] Documentar dimensiones, columnas, tipos, valores ausentes y duplicados.
- [ ] Determinar unidad de registro y unicidad de `customerID` (nombre sujeto a inspección).
- [ ] Inspeccionar categorías reales y registrar supuestos sin resolver.

**Gate M1:** cuatro fichas completadas, código reproducible y primeros hallazgos separados de hipótesis.

## Sprint 2 — Universo de clientes y joins
- [ ] Comparar claves y superposición entre tablas.
- [ ] Determinar qué significa que un cliente falte en una tabla de servicio.
- [ ] Verificar cardinalidades antes de decidir cómo unir.
- [ ] Documentar posibles nulos introducidos por join.

**Gate M2:** universo de análisis y estrategia de join justificados.

## Sprint 3 — EDA de comportamientos
- [ ] Servicios individuales, combinaciones y recuentos.
- [ ] Cargos, contratos, formas de pago, paperless billing.
- [ ] Interacciones con atributos personales y duración.
- [ ] Detección y revisión de atípicos, sin eliminarlos automáticamente.
- [ ] Evaluar si clustering merece un experimento posterior.

**Gate M3:** hipótesis contrastadas mediante evidencia descriptiva y límites claros.

## Sprint 4 — Preparación
- [ ] Definir Churn y fecha de referencia sin filtrar información futura.
- [ ] Auditar nulos, categorías y variables de fechas.
- [ ] Planear ingeniería de características; registrar definiciones.
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
- [ ] Medir en test reservado una sola vez después de la selección.
- [ ] Interpretar AUC-ROC, Recall y errores operativos.
- [ ] Discutir límites y recomendaciones para retención.
- [ ] Verificar ejecución y consistencia del notebook completo.

**Gate M7:** entrega final verificable.

## Sprint 8 — Opcional
- [ ] Definir propuesta o prototipo de uso, con riesgos y condiciones de operación.

**Gate M8:** transferencia opcional documentada.
