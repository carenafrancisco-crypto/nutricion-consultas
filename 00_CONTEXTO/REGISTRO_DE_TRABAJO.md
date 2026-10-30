# Registro de trabajo

Para que cualquier agente continúe sin empezar de cero. Leer después de `00_LEER_PRIMERO_CONTEXTO_DEL_PROYECTO.txt`.

## 2026-10-25 — Sesión 1 (Claude Code)

### Reorganización
- Se crearon las carpetas `00_CONTEXTO`, `01_ORIGINALES`, `02_FUENTES`, `03_EN_TRABAJO`, `04_PARA_PACIENTES` y `99_ARCHIVO`.
- Los 5 materiales originales se **movieron** (no se copiaron ni modificaron) a `01_ORIGINALES/`. Las conversaciones se movieron a `00_CONTEXTO/`. El archivo LEER_PRIMERO quedó en la raíz.

### Qué se leyó (y qué no)
- Leído completo: el archivo de contexto; los 4 borradores (texto extraído); las conversaciones 1, 7 y 8 completas; **todos los mensajes de Francisco** de las 9 conversaciones (238 mensajes).
- **NO leído aún:** las respuestas del asistente en las conversaciones 2, 3, 4, 5, 6 y 9 (unas 14.000 líneas). Son propuestas de un asistente (B), no instrucciones. Leerlas al trabajar cada tema.
- **NO revisado:** el libro "¿Qué le doy de comer?" (escaneado, sin texto extraíble; en este equipo no hay OCR instalado).
- **Falta:** `Plan_alimentacion_en_consulta.md` (mencionado en el contexto, no está en la carpeta).

### Duplicados / versiones
- Desayuno y merienda: la versión de la conv. 7 (abr. 2025) es anterior al PDF. **El PDF es la vigente.**
- Protocolo Lp(a): el docx coincide con el texto final de la conv. 5 más la sección de microplásticos. **El docx es el vigente.**
- El texto de legumbres y la guía 6–12 meses existen solo dentro de las conversaciones.

### Producido
- `03_EN_TRABAJO/AUDITORIA_BASE_COMUN_v0.1.md`
- `03_EN_TRABAJO/AUDITORIA_PROTOCOLO_LPA_v0.1.md` (solo seguridad)
- `00_CONTEXTO/INDICE_MATERIALES.md`

### Decisiones de Francisco (confirmadas)
- **Encuadre del proyecto (A):** armar un programa general + programas secundarios por patología, con material pedagógico y evidencia dura de eficacia. Objetivo: ahorrar tiempo de consulta. Los materiales actuales son insumos perfectibles.
- **El protocolo Lp(a) se hizo para UNA paciente**; no es universal. Se usa como insumo del programa de dislipemias.
- Plan propuesto: `03_EN_TRABAJO/PLAN_DEL_PROYECTO_v0.1.md` (arquitectura y orden de trabajo **pendientes de aprobación**).

### Propuestas aún NO aceptadas
- D1–D8 de la auditoría de la base común.
- Calendario tentativo de 1.ª consulta, control a 2–4 semanas y reevaluación a 8–12 semanas (viene de la conv. 1, propuesta de ChatGPT).
- Primeros entregables: plan individual de 1 página, guía común de 2 páginas, 10 comidas.

### Pendientes
1. Que Francisco responda D1–D8 → con eso, redactar la guía común de 2 páginas v0.1.
2. Plantilla del plan individual de 1 página (no depende de D1–D8; se puede hacer ya).
3. Verificar las fuentes marcadas con † (texto completo).
4. Leer la sección 5 de la ADA 2026, la sección Lp(a) de la ESC/EAS 2025 y la niacina/aspirina del consenso EAS 2022.
5. OCR del libro (requiere instalar Tesseract o que Francisco lo apruebe) — solo para la rama pediátrica.
6. Leer las respuestas del asistente de las conversaciones 2–6 y 9 cuando se trabaje cada tema.

## 2026-10-29 — Guías de medallones vegetales (programa general)

### Entró
- Francisco aportó dos Word: guía práctica y guía ampliada de medallones vegetales. Los originales quedan sin tocar en `01_ORIGINALES/`.

### Producido
- `03_EN_TRABAJO/Guia_practica_medallones_vegetales_v0.2.docx` y `Guia_ampliada_medallones_vegetales_v0.2.docx`:
  - Membrete en el encabezado (falta el número de matrícula: `M.P. ______`).
  - Más ejemplos de legumbres, cereales y pseudocereales; nota sobre celiaquía (TACC), sal, bicarbonato, conservación (heladera 3 días / freezer 3 meses) y ligante sin huevo (chía o lino).
  - 3 combinaciones nuevas (ahora son 8).
  - Infografía al final de cada guía.
  - Ampliada: se sacó "la preparación original propone"; referencias verificadas (Europe PMC / Crossref):
    - [2] Herreman 2020: DIAAS 85 (arveja/trigo 60/40) y 92 (soja/avena 90/10) correctos, pero son con el patrón de **0,5–3 años** y modelados con datos de cerdo. Aclarado en el texto.
    - [3] Han 2021: mung 93, mijo 22, mezcla 66 (patrón >3 años). Correcto; se agregó el dato del mijo.
    - [5] completada: Anaemene D, Fadupin G. Appl Food Res 2022. La frase "24–48 h o más" no se pudo verificar → se sacó.
    - [6] Del-Angel 1982 no estaba citada en el texto → ahora se cita.
- `03_EN_TRABAJO/infografia_medallones/` (HTML editable, PNG y PDF).

### Pendientes
- ~~Número de matrícula~~ → cargada (6796L4F20).
- Aprobación de Francisco → pasar a `04_PARA_PACIENTES/`.
- **Estado (2026-10-29):** Francisco todavía NO aprobó las guías v0.2 ni la infografía ("no me gustan aún"). Las sigue trabajando en otra compu. Preguntarle qué no le gusta antes de seguir.
- Para regenerar los Word desde los originales: `python 03_EN_TRABAJO/herramientas/editar_guias.py 01_ORIGINALES 03_EN_TRABAJO 03_EN_TRABAJO/infografia_medallones/infografia.png` (requiere `pip install python-docx`). La infografía se edita en el HTML y se exporta a PNG/PDF con Edge o Chrome headless.

## 2026-10-30 — Documento de visión v1

### Entró
- Francisco aportó el documento "Alimentación en consulta: hacia un programa de educación, acompañamiento y autogestión de salud" (14 secciones).

### Producido
- `00_CONTEXTO/VISION_DEL_PROYECTO_v1.md`: texto tal cual lo pasó Francisco. Pasa a ser el encuadre vigente del proyecto.
- Cambios de encuadre respecto del plan v0.1: meta comercial explícita; preparaciones universales como eje; biblioteca en 3 familias (conocer, preparar, organizar); merencenas; 3 niveles de profundidad; bots con base de conocimiento propia; seguimiento y adherencia; orden de trabajo en 7 etapas.

### Pendientes
- Etapa 1: índice maestro (propósito, destinatario, formato, relaciones, prioridad y estado de cada pieza). Espera aprobación del plan.
- Actualizar `PLAN_DEL_PROYECTO_v0.1.md` → v0.2 y la sección "Visión" del `CLAUDE.md` del proyecto.
- Revisar la carpeta `drcarenaleonbotnutri/` (sin versionar) solo si Francisco lo autoriza (sección 7).

## 2026-10-30 (parte 2) - Etapa 1: índice maestro + kit de consulta v0

### Entró
- Francisco: no borrar indicaciones suyas por falta de evidencia; las merencenas (cena temprana y desayuno tarde) son firmes para dispepsia e hiperinsulinemia. Cada etapa tiene que dejar material usable ya.
- Respuesta de ChatGPT como segundo consultor, adoptada: separar indicación de Francisco, hipótesis fisiológica y eficacia demostrada; integrar con el bot; seguimiento desde el comienzo; piloto comercial temprano; proteger los datos del bot.
- Francisco autorizó revisar el bot (`drcarenaleonbotnutri/botnutriciondrcarenaleon`, repo propio).

### Producido
- `.gitignore`: excluye `drcarenaleonbotnutri/` (tiene `.env` con tokens y `panel_local.sqlite` con pacientes reales).
- `03_EN_TRABAJO/INDICE_MAESTRO_v0.1.md`: piezas con estado, respaldo (IF/E1/E2/E3), equivalente en el bot y seguimiento.
- `03_EN_TRABAJO/PLAN_DEL_PROYECTO_v0.2.md`: reglas de trabajo, etapas, piloto comercial chico, decisiones pendientes D1-D5.
- `03_EN_TRABAJO/conocimiento/FORMULA_MEDALLON_v0.1.md`: fuente única de la fórmula. Detectada diferencia guía 2:1 vs bot 1:1.
- `03_EN_TRABAJO/kit_consulta_v0/`: K2 legumbres y K3 merencenas (HTML + PDF de 1 hoja + PNG), y la ficha profesional de merencenas con respaldo clasificado y bibliografía de memoria (†, a verificar). K1 = guías de medallones v0.2 tal cual.
- `CLAUDE.md`: visión y reglas firmes actualizadas. `tasks/lessons.md` creado.

### Pendientes
- Decisiones D1-D5 del plan v0.2.
- Verificar la bibliografía † de la ficha de merencenas.
- Etapa 2: cargar en el bot las preguntas semanales del kit.
