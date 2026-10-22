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

## Plantilla para nuevas entradas

### AAAA-MM-DD · Sprint N · [título]
- **Pregunta:**
- **Evidencia:**
- **Opciones consideradas:**
- **Decisión y justificación:**
- **Riesgos / supuestos:**
- **Siguiente comprobación:**
