# DataProtect — Cybersecurity Risk Assessment & Mitigation Plan
# DataProtect — Evaluación de riesgos de ciberseguridad y plan de mitigación

**Type / Tipo:** Academic simulation / Simulación académica  
**Organization / Organización:** DataProtect de Guatemala, S. A. (**fictional / ficticia**)  
**Deliverables / Entregables:** 3-sheet Excel risk matrix and action plan; browser-readable bilingual risk-register summary / Matriz en Excel de 3 hojas y plan de acción; resumen bilingüe navegable del registro  
**Skills / Competencias:** Risk assessment · Asset identification · Threat/vulnerability analysis · Excel modeling · Control selection · Remediation tracking

[← Portfolio / Portafolio](../README.md) · [Risk register / Registro de riesgos (CSV)](risk-register-bilingual.csv) · [Visual summary / Resumen visual (SVG)](risk-distribution.svg)

## English

### Business problem
A fictional cybersecurity consulting company identified weak or reused passwords affecting 30% of employees, no remote-access MFA, monitoring software without updates for eight months, unsupported database software, unregistered visitors in sensitive areas, increased phishing attempts and no formal incident-response plan or training.

### My academic approach
I identified critical assets, paired threats with documented vulnerabilities, rated nine scenarios on a **custom qualitative 3×3 likelihood × impact** scale, and prepared proposed mitigations, owners, deadlines and methods of verification. The original spreadsheet contains three tabs: **Matriz**, **Justificación y plan**, and **Criterios y fuentes**. Editable rating fields and formulas support the classification and totals.

### Findings from the case exercise
| Metric | Result |
|---|---:|
| Scenarios evaluated | **9** |
| High priority | **8** |
| Medium priority | **1** |
| Low priority | **0** |

**Key scenarios:** weak/reused passwords (R01), remote access without MFA (R02), phishing-enabled account compromise (R03), unpatched monitoring software (R04), unsupported databases (R05), physical access gaps (R06), unauthorized external access attempts (R07), missing incident-response plan (R08), and lack of incident training (R09).

**Prioritized proposals:** enforce stronger credentials and MFA, patch or migrate obsolete software, regulate visitor access, review external exposure and security logs, and formalize incident-response roles and drills. Planned deadlines and verification evidence are **recommendations, not completed remediation**.

### What a recruiter can inspect
- [Bilingual risk register (CSV)](risk-register-bilingual.csv): a **condensed, readable representation** of the nine scenarios, not a replacement for the original Excel.
- [Risk distribution (SVG)](risk-distribution.svg): distribution of risk classifications, based on the academic scores.
- The original Excel workbook was reviewed for this description but **has not been uploaded into this GitHub folder**. Therefore no downloadable .xlsx is claimed here.

### Limits
The fictional case does not identify exact CVEs, exposure paths or confirmed successful attacks. The 30% figure describes employees using weak/reused passwords, **not the probability of a breach**. The analysis was qualitative; I did not perform a vulnerability scan or deploy the proposed controls.

## Español

### Problema empresarial
Una consultora ficticia de ciberseguridad identificó contraseñas débiles o repetidas en el 30 % del personal, ausencia de MFA remoto, ocho meses sin actualizar software de monitoreo, bases de datos fuera de soporte, visitantes sin registro, aumento de phishing y falta de un plan formal de respuesta y capacitación.

### Mi enfoque académico
Identifiqué activos críticos, asocié amenazas con vulnerabilidades documentadas, valoré nueve escenarios mediante una **escala cualitativa propia de 3×3 (probabilidad × impacto)** y propuse medidas de mitigación, responsables, plazos y formas de verificación. El Excel original tiene tres hojas: **Matriz**, **Justificación y plan** y **Criterios y fuentes**. Las calificaciones editables y las fórmulas actualizan los niveles y conteos.

### Resultados del ejercicio
| Indicador | Resultado |
|---|---:|
| Escenarios evaluados | **9** |
| Riesgo alto | **8** |
| Riesgo medio | **1** |
| Riesgo bajo | **0** |

**Escenarios principales:** contraseñas (R01), MFA remoto (R02), phishing (R03), monitoreo desactualizado (R04), bases de datos sin soporte (R05), acceso físico (R06), intentos externos (R07), falta de plan de respuesta (R08) y falta de entrenamiento (R09).

**Medidas propuestas:** fortalecer credenciales y MFA, actualizar o migrar software obsoleto, controlar visitantes, revisar exposición externa y registros, y formalizar procedimientos y simulacros. Los plazos y las verificaciones son **propuestas**, no remediaciones ejecutadas.

### Evidencia consultable
- [Registro bilingüe de riesgos (CSV)](risk-register-bilingual.csv): **resumen** de los nueve escenarios, no sustituto del Excel original.
- [Distribución de riesgos (SVG)](risk-distribution.svg): visualización de las clasificaciones académicas.
- El archivo Excel original se revisó para elaborar esta descripción, pero **todavía no está cargado en esta carpeta de GitHub**.

### Límites
El caso ficticio no especifica CVE concretos, rutas precisas de exposición ni intrusiones exitosas. El 30 % describe empleados con contraseñas débiles o repetidas, **no la probabilidad de una filtración**. No realicé escaneos ni implementé los controles propuestos.

**Framework connection / Relación con marcos:** Asset identification and risk assessment map conceptually to **NIST CSF 2.0 ID.AM and ID.RA**. / La identificación de activos y evaluación de riesgos se relacionan conceptualmente con **NIST CSF 2.0 ID.AM e ID.RA**.

**Source / Fuente:** ESI School of Management, *Caso DataProtect de Guatemala, S. A.* (fictional case / caso ficticio), and the academic workbook prepared for the assignment. / Caso académico y matriz elaborada para la actividad.
