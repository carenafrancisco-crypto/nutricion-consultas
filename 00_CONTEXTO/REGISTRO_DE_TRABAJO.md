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

## 2026-10-30 (parte 3) - Corrección K2 legumbres
- Se había omitido el remojo fermentado de 24-36 h (indicación de Francisco). Repuesto como primera opción, con recuadro propio (por qué, cómo, señales de que va bien o hay que tirar) y en la semana de ejemplo (fermenta viernes, cocina domingo). Índice: K2 = IF + E2.

## 2026-10-30 (parte 4) - Rediseño visual del kit (prototipo K2)
- Francisco: el diseño v0.1 le parece una plantilla genérica de IA. Elegido: estilo "cuaderno de cocina", ilustraciones propias, impreso y celular, pacientes muy variados (letra grande).
- Prototipo `kit_consulta_v0/K2_legumbres_v0.2` (HTML, PDF 1 hoja, PNG): hoja de cuaderno cuadriculado argentino con margen rojo; títulos en Kalam (manuscrita), texto en Atkinson Hyperlegible (para baja visión); frasco fermentando dibujado, pegado con cinta como nota. Mismo contenido que v0.1, incluido el remojo fermentado.
- Pendiente: OK de Francisco para aplicar el estilo a K3 merencenas y a los medallones. Las fuentes se bajan de Google Fonts al renderizar (hace falta internet).

## 2026-10-30 (parte 5) - Kit en estilo cuaderno + hoja "Mejor juntas"
### Entró
- Francisco aprobó el estilo cuaderno; pidió apuntes prolijos (anotaciones en rojo, signos de exclamación, caritas en el margen).
- Indicación nueva: una legumbre y un cereal por semana; fraccionar en frasquitos reutilizados de queso crema o de crema, tapercitos o de plástico (los de vidrio cuestan desmoldar congelados); misma legumbre en preparaciones distintas toda la semana.
- Hoja nueva: por qué combinar legumbre y cereal el mismo día (mejor en el mismo plato) + su relato de las semillas (tuna en San Luis, dispersión por animales, antinutrientes, dientes, fuego y bacterias). Título elegido: "Legumbre + cereal: mejor juntas" ("hermandad" sonaba raro).
### Producido
- `kit_consulta_v0/cuaderno.css`: estilo compartido (fuente única del diseño).
- `K2_legumbres_v0.3`, `K3_merencenas_v0.2`, `K4_mejor_juntas_v0.1` (HTML + PDF de 1 hoja + PNG). Se borraron K2 v0.1/v0.2 y K3 v0.1 (quedan en el historial de git).
### Pendientes
- Pasar la infografía de medallones al estilo cuaderno.
- Revisión de Francisco de las tres hojas.

## 2026-10-30 (parte 6) - Medallones en estilo cuaderno
- `kit_consulta_v0/K1_medallones_v0.3` (HTML + PDF 1 hoja + PNG): misma fórmula, pasos, 8 combinaciones y 6 trucos que la infografía v0.2. La preparación de la legumbre ahora remite a la hoja de legumbres e incluye el remojo fermentado, que faltaba en la infografía vieja.
- La infografía vieja (`infografia_medallones/`) sigue embebida en las guías Word v0.2. Pendiente: decidir si los Word pasan a usar la hoja nueva.
- Guías Word pasadas a v0.3: mismo texto que v0.2; solo se cambió la imagen embebida (infografía vieja -> hoja K1 v0.3 en alta, `kit_consulta_v0/K1_medallones_v0.3_alta.png`). No se regeneraron con el script para no pisar ediciones manuales.

## 2026-10-30 (parte 7) - Desayunos y meriendas + decisiones de base común
### Entró
- Decisiones de Francisco: objetivo = bienestar y salud, no principalmente bajar de peso; dulce: primero no hace falta, después fruta/dátiles, después stevia pura (esteviol), otros edulcorantes no; lácteos con poca lactosa (fermentados); maní sí, con asterisco para dislipemias; productos especiales = toppings para variedad.
### Producido
- `03_EN_TRABAJO/conocimiento/BASE_COMUN_DECISIONES_v0.1.md` (D3-D6 con respaldo y matices).
- `kit_consulta_v0/K5_desayunos_v0.1` (2 carillas): todo el contenido del folleto "Desayuno y merienda" en estilo cuaderno, con la fórmula de 4 partes y la escalera para endulzar. Agregados de seguridad: boldo no diario ni en embarazo; castañas de Pará 1 o 2.
- `cuaderno.css`: soporte para hojas de varias carillas (`body.multi` + `.page`).
### Pendientes
- Matices a discutir: fermentados no bajan caseína; ensayos con maní tostado neutros/favorables en lípidos; frutos secos "5 a 7 unidades" vs puñado ~30 g; el apartado "cómo tratar frutos secos" del folleto no existe.

- Corrección (Francisco): se sacó "con leche pasteurizada" (advertencia desubicada). Puñado de frutos secos = lo que entra en el puño (reemplaza "5 a 7 unidades").

## 2026-10-30 (parte 8) - Grasas y plato saludable
### Entró
- Francisco pidió un estudio de grasas con las dos posturas (omega 6, manteca, ghee, coco) y, después, aplicarlo: oliva base, girasol alto oleico también sirve, manteca/ghee/coco poco y como sabor, no reciclar aceite.
- Plato saludable: salvar lo que valga la pena del cuadro original, mejorar el resto y acercarlo a la colección. Prioridad: que se entienda fácil. Usar las skills de diseño para todo.
- Pedido nuevo: pieza sobre tofu y similares (B17 en el índice).
### Producido
- `conocimiento/ESTUDIO_GRASAS_v0.1.md`; decisiones D1/D2 en `BASE_COMUN_DECISIONES_v0.1.md`.
- `kit_consulta_v0/K6_plato_saludable_v0.1` (HTML + PDF 1 hoja + PNG): plato claro con proporciones + 12 ilustraciones en acuarela tomadas del cuadro original (`kit_consulta_v0/img/`); texto corregido y ordenado; tips de legumbres fermentadas con bicarbonato, una legumbre por semana y el dulce de a poco. Se descartaron los iconos planos, la cruz gris y el texto dentro del plato.
- `K5_desayunos`: sección de grasas actualizada (girasol alto oleico, no reciclar aceite).
### Pendientes
- Actividad física del cuadro original ("2 veces por semana, 30 min") queda como indicación de Francisco; la OMS recomienda 150 min/semana + fuerza 2 días (a decidir).
- K6: actividad física = "9000 pasos (unos 40 min) + mínimo 150 min por semana" (Francisco).
- K7 `Legumbres listas para usar` (familia "Legumbres y granos", tono universal, no vegano): tofu, tempeh, texturizados de soja y otras legumbres, fideos y harinas de legumbre. Seitán fuera (no es legumbre).
- K7 ampliada a `Despensa para variar` (2 carillas): proteínas listas con seitán, pastas de legumbre e integrales, harinas, granos para hervir (agua y tiempos), soja orgánica, fitoestrógenos (menopausia, próstata). Francisco: no ser rígido, abrir las secciones.
- K7: soja texturizada como carne picada; formatos (fina, trozos, bloques tipo bife). Harinas de legumbre y de cereal/pseudocereal, mezcladas (masitas, budines, panqueques, hamburguesas, albóndigas); garbanzo para fainá, fainá pizza y masa del seitán.
- K2: "mejor orgánica certificada"; descartar agua + hervir baja residuos de superficie (glifosato: sin evidencia de reducción; foco en orgánico).
- Francisco: sus ideas al pasar son para filtrar (sumar, mejorar o guardar), no para meter a la fuerza. Cajón creado en `tasks/ideas.md`.
- K7: por qué mezclar harinas (más proteína completa, fibra y minerales que harina blanca o almidón); agroquímicos sin miedo ("no es motivo para dejar las legumbres: el trigo y la harina común se cultivan igual").
