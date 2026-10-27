# Equifax 2017 — Information Security Incident & Vulnerability Analysis
# Equifax 2017 — Análisis de incidente y vulnerabilidades de seguridad

**Type / Tipo:** Academic research essay and recorded summary / Ensayo de investigación y resumen grabado  
**Case / Caso:** Public 2017 Equifax data breach / Filtración pública de Equifax de 2017  
**Course / Materia:** Cybersecurity, ESI School of Management · October / octubre 2026  
**Skills / Competencias:** Incident analysis · CVE research · Patch management · Root-cause reasoning · Risk communication

[← Portfolio / Portafolio](../README.md)

## English

### Incident and business impact
The assignment investigated Equifax's 2017 breach affecting approximately **147 million people**. The coursework discussed identity-theft exposure, legal and reputational consequences, and a **2019 settlement of at least US$575 million, potentially reaching US$700 million**. These are figures reported in the cited public sources, not independently measured results of this project.

### What I analyzed
1. **Entry point:** an Apache Struts application vulnerable to **CVE-2017-5638**; a patch was available but was not successfully applied to the affected system.
2. **Compounding weaknesses:** deficiencies in patch verification, access to credentials, segmentation and monitoring.
3. **Response:** discovery of suspicious activity in late July 2017, investigation and containment, public disclosure in September and customer support challenges.
4. **Lessons:** asset/software visibility, ownership of remediation, verification of fixes, least privilege, segmentation, logging, and coordinated customer communication.

### Key observation
> Having an update policy is not enough; organizations need evidence that a critical vulnerability was actually remediated.

### Deliverables and scope
- Research-based written essay (original submission in Spanish).
- Spoken summary (original audio assignment in Spanish; **audio file is not hosted in this repository**).
- This bilingual page is a **portfolio synopsis**, not a forensic report or an independent vulnerability assessment.

**What I did not do:** I did not scan Equifax systems, perform forensic analysis or access breach data.

### Public references cited in the assignment
- [U.S. Government Accountability Office — GAO-18-559](https://www.gao.gov/products/gao-18-559)
- [Federal Trade Commission — 2019 settlement announcement](https://www.ftc.gov/news-events/news/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related-2017-data-breach)
- [U.S. House Oversight Committee — Equifax report](https://oversight.house.gov/report/committee-releases-report-revealing-new-information-on-equifax-data-breach/)

## Español

### Incidente e impacto empresarial
El ensayo investigó la filtración de Equifax en 2017, que afectó aproximadamente a **147 millones de personas**. Se analizaron los riesgos de robo de identidad y las consecuencias legales y reputacionales, incluido el **acuerdo anunciado en 2019 por al menos US$575 millones, con posibilidad de llegar a US$700 millones**. Las cifras provienen de las fuentes citadas, no de mediciones propias.

### Qué analicé
1. **Punto de entrada:** una aplicación con Apache Struts vulnerable a **CVE-2017-5638**, con parche disponible que no se aplicó efectivamente al sistema afectado.
2. **Debilidades adicionales:** verificación insuficiente de parches, protección de credenciales, segmentación y monitoreo.
3. **Respuesta:** detección de actividad sospechosa a finales de julio de 2017, investigación, contención, divulgación en septiembre y dificultades en los canales de atención.
4. **Lecciones:** inventario de aplicaciones, responsables de remediación, evidencia de cierre, mínimo privilegio, segmentación, registros y comunicación coordinada.

### Observación principal
> No basta con tener una política de actualizaciones: hay que comprobar que una vulnerabilidad crítica se corrigió realmente.

### Entregables y alcance
- Ensayo académico en español.
- Resumen oral grabado en español (**el audio original no está alojado en este repositorio**).
- Esta página bilingüe es una **síntesis para portafolio**, no un informe forense ni una evaluación independiente.

**Lo que no hice:** no escaneé sistemas de Equifax, no realicé análisis forense y no accedí a datos de la filtración.

### Fuentes públicas citadas
Las fuentes oficiales se encuentran enlazadas en la sección anterior.

**NIST relevance / Relación con NIST:** Vulnerability identification and risk assessment relate conceptually to **ID.RA**; response coordination relates to **RS**. / Identificación y evaluación de vulnerabilidades se relacionan conceptualmente con **ID.RA** y la respuesta con **RS**.
