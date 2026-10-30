# Proyecto: Nutrición en consulta

Leer primero: `00_LEER_PRIMERO_CONTEXTO_DEL_PROYECTO.txt` (reglas: no tocar los originales, no inventar citas, no conectar Drive).

## Usuario
Dr. Francisco Carena León. Médico en Argentina, ovolactovegetariano. Español rioplatense.
Quiere respuestas en criollo, cortas y con una propuesta clara. Le importa ordenarse y ahorrar tiempo.

## Visión del proyecto (NO OLVIDAR)
Vigente: `00_CONTEXTO/VISION_DEL_PROYECTO_v1.md` (2026-10-30). En corto:
- Sistema que enseña, acompaña y ayuda a sostener cambios. Primero se usa en consulta y después pasa a ser un **producto comercial de autogestión** (meta explícita: generar ingresos).
- Biblioteca en tres familias (conocer, preparar, organizar) + merencenas, con **preparaciones universales** (fórmulas, no recetas sueltas) y tres niveles (ficha, guía, técnico).
- **Programa general** + programas por patología (diabetes/prediabetes, obesidad, HTA, dislipemias/Lp(a), digestivo; pediatría aparte).
- Bots con base de conocimiento propia y seguimiento desde el comienzo.
- Inventario: `03_EN_TRABAJO/INDICE_MAESTRO_v0.1.md`.

Reglas firmes de Francisco:
- **Material usable ya.** Cada etapa deja algo que se use en consulta (estado `EN USO`). No esperar a que esté perfecto.
- **No borrar indicaciones suyas por falta de evidencia.** Se conservan y se clasifican (`IF` indicación de Francisco, `E1` eficacia demostrada, `E2` respaldo parcial, `E3` hipótesis). Una `IF` sin `E1` se usa de forma individualizada, no como regla para toda la población.
- **Fuente única**: cada fórmula o regla en un solo archivo de `03_EN_TRABAJO/conocimiento/`.
- El bot vive en otro repo (`botnutriciondrcarenaleon`). No duplicar lo que ya tiene. Nunca versionar acá sus credenciales ni sus bases de pacientes.

Los materiales de `01_ORIGINALES` son insumo perfectible, no producto.

El protocolo Lp(a) (`LPA LPMQTRMP.docx`) se hizo para UNA paciente. No es universal ni se entregó en masa. Es insumo para el programa de dislipemias.

Cada propuesta tiene que decir a qué programa pertenece y qué evidencia la respalda. Plan: `03_EN_TRABAJO/PLAN_DEL_PROYECTO_v0.1.md`.

## Trabajo en varias compus (GitHub)
Repo privado: `carenafrancisco-crypto/nutricion-consultas`.
- Al empezar sesión: `git pull`.
- Al terminar: commit + `git push`.
- Registrar avances en `00_CONTEXTO/REGISTRO_DE_TRABAJO.md`.
