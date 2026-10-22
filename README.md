# Interconnect · Churn Prediction

**Proyecto final de Data Science · TripleTen**  
**Estado:** Sprint 0 — infraestructura y documentación, sin análisis ejecutado.  
**Enfoque:** comprender primero a los clientes; formular hipótesis, contrastarlas y solo después modelar.  
**Metodología:** CRISP-DM, iterativa, organizada en sprints con criterios de cierre.

## Problema

Interconnect busca identificar clientes con riesgo de cancelar el servicio, para apoyar decisiones de retención. El entregable académico requiere clasificación binaria, comparación de al menos dos modelos base sin balanceo, tratamiento de desbalance/ajuste, evaluación con **AUC-ROC como métrica principal y Recall como adicional**, y un informe orientado a negocio. **No hay resultados aún.**

## Principios del trabajo

- **Tutoría, no solución automática.** El estudiante plantea hipótesis, escribe código y justifica decisiones. El asistente cuestiona, enseña y revisa; Claude Code mantiene estructura y ayuda con Git bajo autorización.
- **Una observación no es una explicación causal.** Distinguir dato observado, hipótesis y conclusión sustentada.
- **Perfil no es historia temporal.** No afirmar evolución del cliente sin registros longitudinales.
- **Sin fuga de información.** Separar información usada para definir Churn de las características disponibles para la predicción.
- **Datos crudos inmutables.** No publicar los CSV sin confirmar derechos de redistribución. No incorporar datos al control de versiones.
- **Simplicidad profesional.** Código claro, modular cuando se necesite, verificable, reproducible y legible.

## Datos por auditar

| Fuente | Pregunta estructural |
|---|---|
| `contract.csv` | ¿Qué representa cada fila? ¿Qué campos reflejan contrato, pago y salida? |
| `internet.csv` | ¿Solo registra clientes con internet? ¿Qué complementos aparecen? |
| `personal.csv` | ¿Una fila por cliente? ¿Qué atributos personales contiene? |
| `phone.csv` | ¿Solo clientes con telefonía? ¿Cómo se superpone con internet? |

Origen en TripleTen: `/datasets/final_provider/`. Las tablas **no han sido inspeccionadas localmente**. El distinto número de filas puede deberse a cobertura de servicios, pero debe verificarse con la clave de cliente.

## Preguntas de investigación

- Combinaciones de teléfono/internet, servicios opcionales y **cantidad de servicios**: ¿cómo se relacionan con permanencia y Churn?
- Tipo de contrato, método de pago, facturación sin papel y cargos: ¿qué asociaciones aparecen?
- Interacciones entre pareja, dependientes, género y servicios de protección/soporte: ¿qué patrones son estadísticamente observables sin atribuir motivaciones personales?
- ¿Qué caracteriza a clientes atípicos y agrupaciones no evidentes? ¿Aporta valor exploratorio el clustering?
- ¿Qué información temporal existe realmente? ¿Podemos analizar duración sin confundirla con trayectorias de consumo?

## Ruta de trabajo y entregables

| Sprint | Fase CRISP-DM | Trabajo | Milestone / criterio de cierre |
|---|---|---|---|
| **0. Base reproducible** | Comprensión del negocio | Git, documentación, reglas, estructura, ingesta pendiente | **M0:** repo local inicializado, README, contexto y bitácora; sin CSV en Git |
| **1. Radiografía de tablas** | Comprensión de datos | EDA individual: granularidad, esquema, nulos, categorías, tamaños, claves | **M1:** fichas de 4 tablas y preguntas documentadas; ninguna limpieza arbitraria |
| **2. Población y relaciones** | Comprensión de datos | Intersecciones de IDs, cobertura, servicios exclusivos/combinados, auditoría de llaves | **M2:** estrategia de unión argumentada y universo de clientes definido |
| **3. Comportamientos e hipótesis** | Comprensión de datos | Contratos, permanencia, cargos, pagos, número de servicios, cruces demográficos, atípicos | **M3:** evidencia descriptiva con gráficos/tablas y límites interpretativos |
| **4. Dataset analítico** | Preparación | Objetivo Churn, manejo de ausencias, fechas, ingeniería de características, codificación, split sin leakage | **M4:** dataset y pipeline reproducibles, validaciones básicas |
| **5. Modelos base** | Modelado | ≥2 modelos sin balanceo, evaluación en validación AUC-ROC y Recall | **M5:** comparación baseline honesta y reproducible |
| **6. Experimentos controlados** | Modelado | Desbalance, hiperparámetros, análisis de errores; clustering opcional si aporta | **M6:** registro de experimentos y modelo candidato justificado |
| **7. Evaluación e informe** | Evaluación | Test final reservado, AUC-ROC/Recall, límites y recomendaciones negocio | **M7:** informe y notebook final auditables |
| **8. Transferencia opcional** | Despliegue | Prototipo o propuesta operativa de uso; no sustituye entregable | **M8:** alcance y restricciones documentadas si se realiza |

**Regla:** la secuencia se revisa al descubrir nueva evidencia. Nunca optimizar con el conjunto de prueba. El clustering no es requisito ni implica automáticamente un mejor clasificador.

## Estructura

```text
interconnect-churn-prediction/
├── README.md
├── PROJECT_CONTEXT.md
├── ROADMAP.md
├── .gitignore
├── requirements.txt              # se completa cuando conozcamos dependencias
├── data/
│   └── raw/                      # CSV originales, ignorados por Git
├── notebooks/                     # experimentos pedagógicos, uno por objetivo
├── src/                           # utilidades reutilizables cuando hagan falta
├── reports/
│   └── figures/
└── docs/
    ├── decision_log.md
    ├── hypotheses.md
    └── data_dictionary.md
```

## Flujo de trabajo

1. Elegir una pregunta y registrar hipótesis/criterio de contraste.
2. Ejecutar una inspección o experimento pequeño, sin modificar datos originales.
3. Escribir evidencia, interpretación, incertidumbres y siguiente decisión.
4. Revisar cambios (`git status`, `git diff`), hacer commits temáticos y **push solo con aprobación**.
5. Actualizar README, bitácora e hitos al cerrar cada sprint.

**Siguiente acción:** Sprint 0, repositorio local inicializado en `interconnect-churn-prediction/` (ver `PROJECT_CONTEXT.md`), revisar `.gitignore` y preparar la importación manual de CSV sin publicarlos.
