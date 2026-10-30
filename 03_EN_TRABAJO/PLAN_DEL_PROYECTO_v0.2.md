# Plan del proyecto - v0.2 (BORRADOR)

- Fecha: 2026-10-30
- Reemplaza a `PLAN_DEL_PROYECTO_v0.1.md`, que queda como antecedente. Su arquitectura por patología y su tabla de evidencia siguen valiendo y se integran acá.
- Encuadre: `00_CONTEXTO/VISION_DEL_PROYECTO_v1.md`. Inventario de piezas: `INDICE_MAESTRO_v0.1.md`.

## 1. Reglas de trabajo

1. **Producir mientras se construye.** Cada etapa termina con al menos una pieza `LISTO PARA PROBAR` en consulta. Usar algo no significa que esté aprobado: se mejora usándolo.
2. **No abrir frentes sin cerrar.** Antes de empezar una pieza nueva, revisar qué pieza ya está en uso.
3. **Indicaciones de Francisco: se habla con él antes de tocar.** El original se conserva; si hay evidencia en contra, se marca la objeción con su respaldo y él decide explícitamente qué llega al paciente.
4. **Fuente única.** Cada conocimiento reutilizable vive en un solo archivo de `03_EN_TRABAJO/conocimiento/`. El Word, la infografía, el bot y la app lo toman de ahí.
5. **El seguimiento se diseña con cada pieza**: objetivo, acción, pregunta semanal, barreras y resultado evaluable (índice, sección 7).
6. **No se duplica lo que ya existe en el bot** (`drcarenaleonbotnutri/`, repo aparte). Primero se revisa qué hay.
7. **Segundo consultor.** Las dudas científicas o estratégicas importantes se contrastan con ChatGPT. La decisión final es de Francisco.

## 2. Arquitectura

```
CONOCIMIENTO (fuente única: fórmulas, reglas, respaldo)
   |
   +-- Biblioteca: A. Conocer / B. Preparar / C. Organizar / Merencenas
   |      en 3 niveles: N1 ficha, N2 guía, N3 técnico
   |
   +-- Programas: General (P0) + patologías (P1-P5) + Pediatría (P6, aparte)
   |      cada programa elige piezas de la biblioteca y agrega solo lo propio
   |
   +-- Bot (repo aparte): seguimiento, cocina, organización
   |      toma fórmulas y preguntas de seguimiento de la fuente única
   |
   +-- Seguimiento: objetivo -> acción -> pregunta semanal -> barrera -> resultado
```

## 3. Etapas (orden de la visión, con dos cambios)

| Etapa | Qué | Entregable usable | Estado |
|---|---|---|---|
| 1 | Índice maestro + kit de consulta v0 | K1 medallones, K2 legumbres, K3 merencenas | EN CURSO |
| 2 | Arquitectura del acompañamiento | Preguntas semanales del kit cargadas en el bot (T1) | PENDIENTE |
| 3 | Sistema editorial | Plantilla única de hoja N1 (la de K2 y K3) | PENDIENTE |
| 4 | Piloto | Sumar hummus, yogures, ensaladas y la ficha de fibra | PENDIENTE |
| 5 | Validación **+ piloto comercial chico** | Ver sección 4 | PENDIENTE |
| 6 | Ampliación | Biblioteca, merencenas, programas por patología | PENDIENTE |
| 7 | Producto comercial | Versión vendible con lo que funcionó | PENDIENTE |

Cambios respecto de la visión:
- El seguimiento entra desde la etapa 1 (sección 7 del índice), no en la 2.
- La prueba de venta se adelanta a la etapa 5, sin esperar a la biblioteca completa.

## 4. Piloto comercial chico (M1)

- Qué se ofrece: el kit, el bot de Telegram que ya funciona y una pregunta semanal de seguimiento durante 4 a 8 semanas.
- A quién: pacientes propios. El número lo decide Francisco.
- Qué se mide: uso, continuidad a 4 y 8 semanas, si están dispuestos a pagar, horas de trabajo de Francisco por participante y costo de la IA.
- Precio y forma de cobro: sin decidir.
- Antes de empezar hay que resolver: consentimiento y protección de datos de salud (Ley 25.326, datos sensibles). Queda por averiguar si al bot le corresponde algún requisito de ANMAT como software médico.

## 5. Decisiones pendientes de Francisco

| # | Decisión | Por qué importa |
|---|---|---|
| D1 | Qué no le gusta de las guías de medallones v0.2 | Hoy se usan tal cual, marcadas LISTO PARA PROBAR |
| D2 | Meta de legumbres por semana para la hoja K2 | La hoja tiene el campo en blanco |
| D3 | Si el bot educativo (T4) puede usar IA para responder desde la base aprobada | Hoy las reglas del bot lo prohíben |
| D4 | Proporción por defecto del medallón: 2:1 (guía) o 1:1 (bot) | Fuente única; propuesta: 2:1 |
| D5 | Dónde vive el repo del bot (ver registro de trabajo 2026-10-30) | Hoy está dentro de esta carpeta |

## 6. Evidencia por programa

Sigue la tabla de la sección 3 de `PLAN_DEL_PROYECTO_v0.1.md`, todavía sin verificar (†). Para las merencenas: `kit_consulta_v0/K3_merencenas_ficha_profesional_v0.1.md`.

## 7. Próximo paso acordado (2026-10-30): piloto corto antes de ampliar

Recorrido: legumbres (K2) → medallones (K1) → una pregunta de seguimiento a la semana ("¿cocinaste la legumbre? ¿hiciste medallones? ¿qué te costó?").
Qué se observa: si la persona entiende, cocina y repite, y cuánto tiempo de consulta ahorra. Con eso, la pieza pasa a `PROBADO`.
Versión para celular (bloques con letra mayor): K2 y K6 hechas (`kit_consulta_v0/movil/`), aparte de la versión impresa.
