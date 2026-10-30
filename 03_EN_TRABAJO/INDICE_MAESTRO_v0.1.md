# Índice maestro - v0.1 (BORRADOR)

- Fecha: 2026-10-30
- Base: `00_CONTEXTO/VISION_DEL_PROYECTO_v1.md`, sección 13, etapa 1.
- Regla de uso: este índice se completa de a poco. No se llenan todas las celdas antes de producir. Una pieza entra con lo mínimo y se completa cuando se trabaja.

## Cómo se lee

**Estado**
- `EN USO` - borrador que Francisco ya puede usar en consulta. Se mejora usándolo. No es material clínicamente aprobado.
- `BORRADOR` - en elaboración.
- `PENDIENTE` - definido, sin empezar.
- `IDEA` - mencionado en la visión, sin definir.
- `APROBADO` - revisado y aprobado por Francisco (pasa a `04_PARA_PACIENTES/`).

**Respaldo** (se pueden combinar: por ejemplo `IF + E2`)
- `IF` - indicación clínica de Francisco. Se conserva siempre. Nunca se borra por falta de evidencia.
- `E1` - eficacia clínica demostrada (ensayos o metaanálisis con resultados clínicos).
- `E2` - respaldo parcial: ensayos chicos o cortos, desenlaces intermedios, estudios observacionales consistentes o recomendación de guía con evidencia limitada.
- `E3` - hipótesis fisiológica o mecanística.
- `?` - sin revisar.

Una indicación `IF` con respaldo `E2` o `E3` se usa de forma individualizada. No se presenta como regla para toda la población hasta tener `E1`.

**Nivel** (sección 6 de la visión): `N1` ficha visual · `N2` guía ampliada · `N3` documento técnico.

**Fuente única**: cada conocimiento reutilizable (una fórmula, una regla) vive en un solo archivo de `03_EN_TRABAJO/conocimiento/`. El Word, la infografía, el bot y la app lo toman de ahí. No se reescribe en cada formato.

## 1. Kit de consulta v0 (prioridad 1, ahora)

| ID | Pieza | Familia | Nivel | Programa | Estado | Respaldo | Archivo |
|---|---|---|---|---|---|---|---|
| K1 | Medallones vegetales | B. Preparar | N1 + N2 | General | EN USO | E2 (calidad proteica) | `Guia_practica_medallones_vegetales_v0.2.docx`, `Guia_ampliada_...v0.2.docx`, `infografia_medallones/` |
| K1-F | Fórmula del medallón (fuente única) | B. Preparar | Conocimiento | General | BORRADOR | E2 | `conocimiento/FORMULA_MEDALLON_v0.1.md` |
| K2 | Legumbres: cocinar una vez, comer toda la semana | A. Conocer + C. Organizar | N1 | General | EN USO | ? (pendiente de referencias) | `kit_consulta_v0/K2_legumbres_v0.1.html` |
| K3 | Merencenas: la última comida, más temprano | Merencenas | N1 (paciente) + N3 (profesional) | Digestivo; diabetes/prediabetes; obesidad | EN USO | IF + E2 (dispepsia, glucemia) + E3 (desayuno tardío) | `kit_consulta_v0/K3_merencenas_v0.1.html`, `kit_consulta_v0/K3_merencenas_ficha_profesional_v0.1.md` |

## 2. A. Conocer los alimentos

| ID | Pieza | Programa | Estado | Respaldo | Prioridad |
|---|---|---|---|---|---|
| A01 | Legumbres (ficha completa) | General | PENDIENTE (K2 es el primer recorte) | ? | 1 |
| A02 | Fibra alimentaria | General; digestivo; dislipemias; diabetes | PENDIENTE | ? | 1 |
| A03 | Semillas | General | IDEA | ? | 3 |
| A04 | Frutos secos | General; dislipemias | IDEA | ? | 2 |
| A05 | Cereales y pseudocereales | General | IDEA | ? | 3 |
| A06 | Frutas | General | IDEA | ? | 3 |
| A07 | Fermentados (prebióticos, probióticos, fermentados) | General; digestivo | IDEA | ? | 3 |
| A08 | Vegetales | General | IDEA | ? | 3 |
| A09 | Grasas alimentarias | General; dislipemias | IDEA | ? | 2 |

## 3. B. Preparar comidas (preparaciones universales)

| ID | Pieza | Estado | Plantilla del bot que la representa | Prioridad |
|---|---|---|---|---|
| B01 | Medallones, hamburguesas y croquetas | EN USO (K1) | RG009 (sin slots cargados) | 1 |
| B02 | Hummus, patés y cremas de legumbres | PENDIENTE | - | 1 |
| B03 | Yogures completos | PENDIENTE | - | 1 |
| B04 | Ensaladas completas | PENDIENTE | - | 1 |
| B05 | Guisos universales | IDEA | RG008 (poblada) | 2 |
| B06 | Licuados | IDEA | - | 2 |
| B07 | Porridge y granos | IDEA | - | 2 |
| B08 | Pudines de semillas | IDEA | - | 3 |
| B09 | Panqueques, waffles, muffins, tortillas | IDEA | "masa horneada" (nueva, sin crear) | 3 |
| B10 | Tostadas y comidas sin cocinar | IDEA | - | 2 |
| B11 | Sopas y cremas enriquecidas | IDEA | - | 3 |
| B12 | Salteados | IDEA | RG011 (sin slots) | 3 |
| B13 | Tortillas y omelettes | IDEA | RG002 | 3 |
| B14 | Verduras rellenas y al horno | IDEA | "masa horneada rellena" (nueva) | 3 |
| B15 | Fermentos caseros | IDEA | fuera de alcance en el bot | 3 |
| B16 | Caldos, salsas, aderezos, condimentos | IDEA | - | 3 |

## 4. C. Organizar comidas y hábitos

| ID | Pieza | Estado | Herramienta del bot que ya existe | Prioridad |
|---|---|---|---|---|
| C01 | Cocinar una vez, comer varios días | EN USO (dentro de K2) | Cocina Semanal: plan semanal | 1 |
| C02 | Lista de compras | PENDIENTE | Cocina Semanal: lista de compras cocido a crudo + catálogo Buena Vida con precios | 2 |
| C03 | Armar desayunos y meriendas | IDEA | - | 2 |
| C04 | Armar almuerzos y cenas completos | IDEA | regla "plato completo" de Cocina Semanal | 2 |
| C05 | Comer bien con poco tiempo o presupuesto | IDEA | catálogo con precios (costeo) | 2 |
| C06 | Improvisar con lo que hay | IDEA | `recommend` del motor nutricional | 3 |

## 5. Módulos clínicos (programas por patología)

Se apoyan en el programa general y solo agregan lo propio. Detalle en `PLAN_DEL_PROYECTO_v0.2.md`.

| ID | Programa | Piezas del kit que ya sirven | Capa del bot | Estado |
|---|---|---|---|---|
| P0 | General | K1, K2 | - | BORRADOR |
| P1 | Diabetes / prediabetes / hiperinsulinemia | K3 | (a revisar) | IDEA |
| P2 | Obesidad | K3 | (a revisar) | IDEA |
| P3 | HTA | - | (a revisar) | IDEA |
| P4 | Dislipemias / Lp(a) | K1, K2 | DISLIPEMIA | IDEA (insumo: protocolo Lp(a)) |
| P5 | Digestivo (dispepsia, colon irritable, constipación) | K3 | CONSTIPACION | IDEA |
| P6 | Pediatría (rama aparte) | - | - | IDEA |

## 6. Bots y herramientas

Repo: `drcarenaleonbotnutri/botnutriciondrcarenaleon` (aparte, no se versiona acá).

| ID | Función (visión, sección 7) | Qué ya existe | Qué falta / decisión pendiente |
|---|---|---|---|
| T1 | Bot de seguimiento clínico | Vinculación paciente-bot (código `BV-`), registro diario, `PRINCIPIOS_CLINICOS.md` | Preguntas semanales de seguimiento (sección 7 de este índice). |
| T2 | Bot culinario | Plantillas RG008/RG009, motor `recommend`, Cocina Semanal | Cargar la fórmula del medallón desde `conocimiento/`. |
| T3 | Bot de organización | Plan semanal, lista de compras, catálogo con precios | Probarlo en uso real (el bot espera eso desde 2026-09). |
| T4 | Bot educativo | Nada | **Decisión:** hoy la IA del bot solo clasifica intención. Responder preguntas desde la base aprobada requiere cambiar esa regla. |
| T5 | Bot de acompañamiento | Telegram operativo | Recordatorios (etapa 5 del roadmap del bot, sin empezar). |
| T6 | Integración con Tendrel | Contrato diseñado, sin conexión real | No tocar sin decisión específica. |

Frentes del bot abiertos sin cerrar: App Personal (pausado), Tendrel etapa 3 (pendiente), Cocina Semanal etapa 2 (esperando uso). No abrir frentes nuevos en el bot hasta usar uno.

## 7. Seguimiento y adherencia (desde el comienzo)

Cada pieza en uso tiene objetivo, acción, pregunta de seguimiento y resultado evaluable. Estas preguntas son las que después hará el bot (T1).

| Pieza | Objetivo | Acción concreta | Pregunta semanal | Barreras a distinguir | Resultado evaluable |
|---|---|---|---|---|---|
| K1 Medallones | Sumar una comida con legumbre que guste | Hacer una tanda y congelar | ¿Hiciste medallones? ¿Se desarmaron? ¿Te gustaron? | textura, sabor, tiempo | veces por semana; aceptación |
| K2 Legumbres | Legumbres varias veces por semana (meta a definir por Francisco) | Cocinar 1 tanda por semana y freezar | ¿Cuántos días comiste legumbres? ¿Tenés porciones en el freezer? | tiempo, gases, no sabe cocinar, gusto | días con legumbre por semana |
| K3 Merencenas | Terminar de comer más temprano | Merencena antes del horario pactado con el médico | ¿Cuántas noches terminaste de comer antes de la hora pactada? ¿Te fuiste a dormir con hambre? Acidez o ardor esta semana, de 0 a 10 | horario laboral, familia, hambre nocturna | noches cumplidas por semana; síntomas dispépticos 0-10; glucemia en ayunas, HbA1c, peso y cintura según el caso |

## 8. Futuros componentes comerciales

| ID | Pieza | Estado |
|---|---|---|
| M1 | Piloto comercial chico: kit + bot + seguimiento semanal | PENDIENTE (ver plan v0.2) |
| M2 | Material gratuito de entrada | IDEA |
| M3 | Programa educativo pago | IDEA |
| M4 | Suscripción con acompañamiento | IDEA |
| M5 | Licencia para profesionales o instituciones | IDEA |
