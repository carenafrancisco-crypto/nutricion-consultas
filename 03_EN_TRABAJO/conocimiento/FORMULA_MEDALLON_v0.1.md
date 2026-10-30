# Fórmula del medallón vegetal - fuente única v0.1 (BORRADOR)

- Fecha: 2026-10-30
- Programa: general (P0). Pieza del índice: K1-F.
- Regla: el Word, la infografía y el bot toman la fórmula de acá. Si cambia, cambia acá primero.

## Estructura

| Componente | Función | Obligatorio | Opciones | Cantidad de partida |
|---|---|---|---|---|
| Legumbre cocida | base, proteína, fibra | sí | lentejas, garbanzos, porotos, arvejas secas, habas, soja | 2 partes |
| Cereal o pseudocereal cocido | textura, complemento de aminoácidos | sí | avena, arroz, mijo, cebada, maíz, burgol, sorgo, quinoa, amaranto, trigo sarraceno | 1 parte (1:1 también funciona) |
| Sabores | sabor | no | cebolla, ajo, puerro, verdeo, morrón, zanahoria, zapallito, hierbas, especias, poca sal | a gusto |
| Ligante | unir | no | huevo; o 1 cda de chía o lino molido + 3 cdas de agua, 10 min; o harina de legumbre | 1 huevo por tanda |
| Ajuste de humedad | corregir textura | no | avena fina, harina de legumbres o de arroz | de a poco |
| Relleno | variar | no | queso | opcional |

La relación 2:1 es un punto de partida culinario, no una proporción que maximice la calidad proteica.

## Diferencias con el bot (a resolver)

El bot ya modela el medallón como plantilla RG009 (`docs/DESIGN_COCINA_SEMANAL.md`, sección 2.2.1), pero con otros valores:

| Punto | Guía v0.2 | Bot (RG009, propuesta sin cargar) | Propuesta |
|---|---|---|---|
| Proporción | 2 legumbre : 1 cereal | 90 g : 90 g (1:1) | Default 2:1. Rango del bot (legumbre 70-120 g, cereal 60-120 g) ya cubre ambas. |
| Ligante | huevo opcional; chía o lino | huevo; si no hay, harina de legumbre | Sumar chía o lino al bot. |
| Vegetal | dentro de la mezcla, como sabor | guarnición obligatoria, 150 g | Separar: sabores dentro; vegetal como acompañamiento del plato. |
| TACC | burgol y cebada incluidos, con aviso | catálogo sin TACC | Mantener las opciones con trigo y marcar `contiene TACC`. |

## Texturas (lo que más falla)

| Problema | Causa probable | Solución |
|---|---|---|
| Se desarma | mezcla húmeda o sin ligante | avena fina o harina de a poco; huevo o chía; reposar 10 min; heladera 30 min antes de cocinar |
| Queda seco o se agrieta | poca humedad o mucho grano | una cucharada de agua o de líquido de cocción |
| Pastoso por dentro | muy procesado | dejar parte de la legumbre con textura |
| Sin sabor | poca sal o pocos condimentos | sofrito de cebolla y ajo; comino, pimentón o curry |
