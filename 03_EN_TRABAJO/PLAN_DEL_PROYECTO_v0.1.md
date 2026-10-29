# Plan del proyecto — v0.1 (BORRADOR, propuesta B, sin aprobar)

- Fecha: 2026-10-25
- Encuadre (A, dicho por Francisco): un **programa general** y **programas secundarios por patología**, para público general y para patologías puntuales, con material pedagógico y **evidencia dura de que funcionan**. Para qué: ahorrar tiempo de consulta y no repetir todo cada vez.
- Los materiales actuales son insumos perfectibles. El protocolo Lp(a) se hizo para una sola paciente.

## 1. Arquitectura

```
PROGRAMA GENERAL (base para todos)
 ├── Diabetes / prediabetes
 ├── Obesidad / sobrepeso
 ├── Hipertensión
 ├── Dislipemias (incluye Lp(a))
 └── Digestivo (dispepsia, colon irritable, constipación)
PEDIATRÍA (rama separada; no hereda del programa de adultos)
```

Regla: cada programa secundario **solo agrega o cambia** lo que la patología exige. Todo lo demás lo hereda del general, sin repetirlo.

## 2. Qué trae cada programa (el mismo molde para todos)

| Pieza | Para quién | Extensión |
|---|---|---|
| Ficha técnica: objetivo, a quién aplica, contraindicaciones y evidencia de eficacia | Francisco | 1 página |
| Guía pedagógica | Paciente | 1–2 páginas |
| Plan individual (plantilla para completar en consulta) | Paciente | 1 página |
| Ejemplos de comidas argentinas | Paciente | 1 página |
| Seguimiento: qué medir, cuándo y qué hacer si no responde | Francisco | 1/2 página |
| Guion de consulta: 3–5 mensajes clave | Francisco | 1/2 página |

## 3. Evidencia de eficacia por programa (base tentativa)

Todo lo de esta tabla está citado **de memoria (†)**. Hay que verificarlo antes de usarlo.

| Programa | Ensayos o patrones con resultados duros |
|---|---|
| General | PREDIMED (dieta mediterránea + aceite de oliva o frutos secos, menos eventos cardiovasculares)†; guía AHA 2021 (verificada) |
| Diabetes / prediabetes | Diabetes Prevention Program (estilo de vida, menos progresión a diabetes)†; DiRECT (remisión de la diabetes tipo 2 con pérdida de peso)†; ADA Standards 2026, sección 5 (pendiente de leer) |
| Obesidad | Look AHEAD (intervención intensiva de estilo de vida)†; ensayos que comparan dietas (lo que cuenta es la adherencia, más que el reparto de macronutrientes)† |
| Hipertensión | DASH y DASH-Sodio†; reducción de sal† |
| Dislipemias | Portfolio diet (baja el LDL)†; fibra soluble y esteroles†; consenso EAS 2022 sobre Lp(a) (encontrado, pendiente de leer) |
| Digestivo | Dieta baja en FODMAP en colon irritable (ensayos y guías)†; fibra / psyllium en constipación† |

## 4. Orden de trabajo propuesto

1. **Programa general** (con los insumos actuales: Fran, Desayuno, legumbres). Para cerrarlo hacen falta tus respuestas a D1–D8 de `AUDITORIA_BASE_COMUN_v0.1.md`.
2. **Diabetes/prediabetes + obesidad**, juntos porque comparten la mitad de las piezas. Insumo: la tabla IG, que se reemplaza.
3. **Hipertensión** (DASH).
4. **Dislipemias / Lp(a)** (insumo: el protocolo de la paciente, despersonalizado y corregido).
5. **Digestivo**.
6. **Pediatría 6–12 meses** (insumo: conv. 9 y el libro, que necesita OCR).

## 5. Decisiones que necesito de Francisco

- ¿Aprobás la arquitectura y el molde de piezas (secciones 1–2)?
- ¿Te sirve este orden o empezamos por otro programa?
- D1–D8 (para cerrar el programa general).
