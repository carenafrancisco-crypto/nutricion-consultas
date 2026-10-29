# Auditoría protocolo Lp(a) — v0.1 (BORRADOR, solo puntos de seguridad)

- Fecha: 2026-10-25
- Estado: **borrador. No aprobado. Revisión parcial:** solo los puntos de seguridad y de mayor impacto. La revisión completa (alimentación, fibra, actividad física) queda pendiente.
- Original: `01_ORIGINALES/LPA LPMQTRMP.docx` (sin cambios).
- **Contexto (Francisco, 2026-10-25):** el protocolo se hizo para UNA paciente. No es universal. Acá se lo usa como insumo del futuro programa de dislipemias/Lp(a). Los puntos de abajo son lo que habría que corregir para convertirlo en programa general, no una alerta sobre varios pacientes.

## Prioridad 1 — corregir antes de convertirlo en programa

| Indicación | Problema | Fuente | Propuesta |
|---|---|---|---|
| **Vitamina D3 5.000 UI/día (verano) – 7.000 UI/día (invierno), sin dosaje.** En la conversación también aparece un bolo inicial de 100.000 UI. | Las dos dosis superan el nivel máximo tolerable para adultos (100 µg = 4.000 UI/día). La Endocrine Society 2024 desaconseja suplementar por encima de la ingesta recomendada a adultos sanos menores de 75 años y prefiere dosis diarias bajas antes que bolos. Si encima no se mide nada, no hay forma de detectar exceso. | EFSA 2023 (UL 100 µg/día); Endocrine Society, JCEM 2024 | Sacarla como indicación universal. Si hay indicación individual, la decide el médico con dosis ≤ 4.000 UI/día salvo un motivo específico. |
| **Aspirina 75–100 mg "en la mayoría de los pacientes"** | En prevención primaria, la aspirina es una decisión individual por riesgo de sangrado. USPSTF 2022: decisión individual entre 40 y 59 años con riesgo ≥10 %; no iniciarla desde los 60. Hay datos observacionales que sugieren más beneficio con Lp(a) alta, pero no alcanzan para indicarla "en la mayoría". | USPSTF 2022 | "La aspirina la decide su médico según su riesgo de sangrado." Retirar "en la mayoría". |
| **Niacina** "puede bajar Lp(a)" | Baja la Lp(a), pero los ensayos grandes (AIM-HIGH, HPS2-THRIVE†) no mostraron menos eventos y sí más efectos adversos. No se recomienda para este fin†. | † a verificar en el consenso EAS 2022 (Kronenberg, EHJ 2022) | Retirar. |
| **Berberina 500 mg ×2** | Interacciones por CYP (afecta a varios fármacos)†, contraindicada en embarazo†, y la evidencia sobre la Lp(a) es débil. | † | Retirar de la lista general. |
| **Vitamina K2** | Sin evidencia de eventos†. Interfiere con la warfarina y otros antagonistas de la vitamina K†. | † | Retirar, o dejarla solo con advertencia de anticoagulación. |
| **Ayuno 16 h diario + ayuno de 24 h semanal; "luego no se cena"** | Riesgo de hipoglucemia con insulina o sulfonilureas, y además personas mayores, trastornos de la conducta alimentaria y embarazo. En ensayos, el ayuno intermitente rinde parecido a la restricción calórica†. | † | Hacerlo opcional, con contraindicaciones explícitas, y no presentarlo como parte del tratamiento de la Lp(a). |
| **Composición corporal: IMC 18–22, 12–15 % de grasa** | Un IMC de 18 está en el límite del bajo peso. Como meta universal (por ejemplo, en una mujer de 70 años) favorece la pérdida de masa muscular. | † | Retirar la meta universal; individualizarla. |

## Prioridad 2 — corregir antes de volver a entregar

- **Metas automáticas (LDL < 55, "idealmente < 40") y estatina de alta potencia + ezetimiba "como base".** En las guías europeas la Lp(a) es un *modificador* de riesgo y la meta depende de la categoría de riesgo total. Pendiente leer la sección Lp(a) del 2025 ESC/EAS Focused Update (EHJ 2025;46:4359, doi 10.1093/eurheartj/ehaf190) antes de redactar.
- **Medir Lp(a) cada 3–6 meses.** La Lp(a) está determinada genéticamente: con medirla una vez en la vida suele bastar (consenso EAS 2022). Seguir con LDL y ApoB.
- **Ferritina "deseada 40–80".** No conozco evidencia de esa meta en prevención cardiovascular. Retirar la meta.
- **Cúrcuma con pimienta.** En cantidad culinaria, el riesgo es bajo. Hay reportes de daño hepático con suplementos potenciados†, y puede sumar efecto antiagregante con la aspirina†.
- **Magnesio (citrato 1 g/día).** Precaución en enfermedad renal.
- **Aceites:** "evitar completamente aceites de semillas" → ver D1 de la auditoría de la base común.
- **Microplásticos.** La asociación existe (Marfella, NEJM 2024: n = 304, observacional, HR 4,53 para el compuesto IAM/ACV/muerte), pero no prueba causalidad. No encontré respaldo para el ranking "el agua es la principal fuente", ni para "determinante en hombres", ni para el porcentaje de eficacia de los filtros. Propuesta: bajar a una nota breve de precaución razonable, sin ranking ni cifras.

## Lo que está bien orientado (conservar)

Legumbres + integrales como base del almuerzo; fibra alta con psyllium gradual y separado de los fármacos; pescado graso 2–3 veces/semana; lácteos magros o fermentados con cantidades; fuerza 2–3 veces/semana; zona 2 bien explicada; ajuste de porciones para jóvenes que entrenan; no fumar, no alcohol; el fármaco como eje y el plan como complemento.

## Fuentes verificadas hoy

- USPSTF. *Aspirin Use to Prevent CVD*, 2022. https://www.aafp.org/news/health-of-the-public/uspstf-aspirin-cvd.html
- EFSA NDA Panel. *Scientific opinion on the tolerable upper intake level for vitamin D*, EFSA Journal 2023. https://efsa.europa.eu/en/efsajournal/pub/8145
- Demay MB et al. *Vitamin D for the Prevention of Disease*, Endocrine Society, JCEM 2024, doi 10.1210/clinem/dgae290. Resumen: https://www.healio.com/news/endocrinology/20240715/endocrine-society-guideline-most-adults-do-not-benefit-from-additional-daily-vitamin-d
- Kronenberg F et al. *Lipoprotein(a) in atherosclerotic CVD and aortic stenosis: EAS consensus statement*, EHJ 2022;43:3925. https://pmc.ncbi.nlm.nih.gov/articles/PMC9639807/ — **pendiente leer las secciones de niacina y aspirina.**
- *2025 Focused Update of the 2019 ESC/EAS Dyslipidaemia Guidelines*, EHJ 2025;46:4359. https://discovery.ucl.ac.uk/id/eprint/10219290 — **pendiente leer la sección Lp(a).**
- Marfella R et al. *Microplastics and Nanoplastics in Atheromas and Cardiovascular Events*, NEJM 2024, doi 10.1056/NEJMoa2309822. Resumen: https://www.healio.com/news/cardiology/20240307/tiny-plastics-in-carotid-plaque-tied-to-elevated-risk-for-heart-attack-stroke-death
