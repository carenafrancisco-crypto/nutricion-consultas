# ALIMENTACIÓN EN CONSULTA
## Hacia un programa de educación, acompañamiento y autogestión de salud

- Fecha: 2026-10-30
- Autor: Francisco (texto aportado por él, sin editar).
- Estado: documento de visión vigente. Reemplaza el encuadre de `03_EN_TRABAJO/PLAN_DEL_PROYECTO_v0.1.md` donde haya diferencias.

### 1. La visión general

Estamos construyendo algo que inicialmente surgió de una necesidad cotidiana: explicarles a los pacientes cómo alimentarse mejor, sin tener que repetir las mismas indicaciones en cada consulta y, sobre todo, sin convertir la alimentación saludable en una lista interminable de prohibiciones, recetas rígidas y menús que nadie termina cumpliendo.

Pero el proyecto es bastante más ambicioso que elaborar folletos nutricionales.

Queremos crear un sistema educativo que permita comprender los fundamentos de una alimentación saludable y adquirir habilidades concretas para llevarlos a la práctica.

Este sistema tendrá inicialmente una aplicación clínica, pero está pensado para convertirse en parte de un **programa de autogestión de salud**, que eventualmente queremos comercializar.

La aspiración es que una persona, independientemente de su nivel educativo, experiencia culinaria o situación económica, pueda aprender a tomar mejores decisiones sin depender permanentemente de un profesional.

El desafío consiste en combinar:

- **Rigor científico:** recomendaciones justificadas, con evidencia identificable.
- **Aplicabilidad:** que las personas puedan comprar, cocinar y organizar su alimentación.
- **Educación:** desarrollar comprensión y autonomía.
- **Acompañamiento:** ayudar a sostener los cambios en la vida cotidiana.
- **Personalización:** adaptar las herramientas a distintas necesidades y dificultades.
- **Escalabilidad comercial:** que el sistema pueda atender a muchas personas sin exigir una intervención profesional individual permanente.

Hay una intención económica explícita: **queremos construir un producto que genere ingresos**. Esto no es secundario. La rentabilidad permitirá sostener, mejorar y ampliar el programa.

Sin embargo, la monetización debe apoyarse en un valor real para las personas: ayudarlas a conseguir cambios saludables, medibles y sostenibles.

### 2. Las preparaciones universales: el concepto central

La primera experiencia fue una guía para elaborar medallones vegetales combinando legumbres, cereales y pseudocereales.

La idea surgió de explicar a una paciente, en un papel, cómo preparar diferentes medallones sin depender de una receta exacta.

En lugar de enseñar una receta de lentejas, otra de garbanzos y otra de porotos, queremos enseñar **una estructura común que permita crear muchas preparaciones distintas**.

Esta lógica se extenderá a buena parte de nuestro material culinario.

Por ejemplo, aprender una fórmula para preparar yogures completos permite elaborar decenas de desayunos y meriendas modificando frutas, semillas, frutos secos, cereales y fuentes de proteína.

Lo mismo ocurre con licuados, hummus, ensaladas, guisos, cremas y otras preparaciones.

No queremos producir cien recetas independientes. Queremos identificar unas pocas estructuras que permitan crear cientos de combinaciones.

Cada preparación universal debería enseñar:

1. Qué ingredientes forman su estructura.
2. Qué función nutricional y culinaria cumple cada uno.
3. Qué alternativas pueden utilizarse.
4. En qué proporciones conviene combinarlos.
5. Cómo prepararlos paso a paso.
6. Cómo resolver dificultades de textura, sabor y conservación.
7. Cómo adaptar la preparación a distintas necesidades nutricionales.

Cada estructura tendrá una guía visual y una explicación complementaria para quienes quieran profundizar.

### 3. Primera revisión: los medallones vegetales

Las versiones actuales del repositorio son un punto de partida, no materiales terminados.

Conservaría su filosofía, pero revisaría los siguientes aspectos.

**Proporciones y calidad proteica.** La combinación entre legumbres y cereales puede aprovechar diferencias en sus perfiles de aminoácidos. Sin embargo, no existe una proporción universal entre alimentos cocidos que garantice la máxima calidad proteica. La relación 2:1 a favor de las legumbres puede servir como punto de partida culinario, pero no debe presentarse como científicamente optimizada.

**Remojo, fermentación y antinutrientes.** Queremos conservar la posibilidad del remojo prolongado de 24–36 horas con acidificación o fermentación, que formaba parte de la propuesta original. Debemos distinguir remojo, acidificación y fermentación propiamente dicha, y explicar cuándo corresponde cada procedimiento, teniendo en cuenta su eficacia y seguridad.

No todos los antinutrientes son necesariamente perjudiciales, ni todos se eliminan mediante los mismos procesos.

**Facilidad de elaboración.** La receta debe funcionar con ingredientes económicos y utensilios habituales. Las proporciones serán orientativas, pero se enseñará a identificar mezclas demasiado húmedas, secas o quebradizas.

**Adherencia.** Cocinar legumbres en cantidad, fraccionarlas y congelarlas es uno de los componentes más valiosos. Reduce enormemente las barreras cotidianas.

**Presentación.** Revisaremos la infografía para que pueda interpretarse rápidamente y no termine convertida en una hoja sobrecargada de texto pequeño.

También sería conveniente validar algunas combinaciones en una cocina real. Una preparación nutricionalmente adecuada que se desarma, tiene mala textura o no resulta agradable no cumple nuestro objetivo.

### 4. El esqueleto de la biblioteca

Propongo organizar el contenido en tres grandes familias.

#### A. CONOCER LOS ALIMENTOS

Fichas educativas, preferentemente de una página, acompañadas por documentación ampliada cuando corresponda.

| Tema | Contenido principal |
|---|---|
| Legumbres | Beneficios, proteínas, fibra, remojo, cocción, digestibilidad, gases y preparaciones |
| Semillas | Lino, chía, sésamo, zapallo, girasol: características y formas de consumo |
| Frutos secos | Nueces, almendras, maní, castañas, avellanas: composición, porciones y conservación |
| Cereales y pseudocereales | Diferencias, integrales y refinados, proteínas, fibra y preparación |
| Frutas | Fruta entera, jugos, fibra, maduración, variedades y estacionalidad |
| Fibra alimentaria | Tipos, fuentes, efectos digestivos, metabólicos y sobre la microbiota |
| Fermentados | Yogur, kéfir, vegetales fermentados, elaboración, conservación y evidencia |
| Vegetales | Diversidad, formas de cocción, conservación y aprovechamiento |
| Grasas alimentarias | Aceites, composición de grasas, usos culinarios y evidencia cardiometabólica |

Las fichas deberían responder preguntas reales: ¿por qué debería consumir este alimento?, ¿cómo lo preparo?, ¿cuánto necesito?, ¿qué dificultades pueden aparecer?

La ficha sobre fibra merece especial atención por su conexión con función intestinal, microbiota, constipación, dislipemias, regulación glucémica y prevención del cáncer colorrectal.

Debemos distinguir efectos demostrados de asociaciones epidemiológicas, y también diferenciar prebióticos, probióticos y alimentos fermentados.

#### B. APRENDER A PREPARAR COMIDAS

Esta será nuestra biblioteca de preparaciones universales.

**Desayunos y meriendas**

- Yogures completos y sus combinaciones.
- Licuados nutritivos.
- Porridge y preparaciones de avena u otros granos.
- Pudines de chía y otras semillas.
- Panqueques, waffles, muffins y tortillas.
- Untables, patés y hummus.
- Tostadas y comidas simples para quienes no quieren cocinar.

**Almuerzos y cenas**

- Medallones, hamburguesas y croquetas vegetales.
- Ensaladas completas.
- Hummus, patés y cremas de legumbres.
- Guisos universales.
- Sopas y cremas de vegetales enriquecidas.
- Salteados.
- Tortillas y omelettes.
- Verduras rellenas y preparaciones al horno.

**Preparaciones transversales**

- Fermentos caseros.
- Caldos y bases culinarias.
- Salsas y aderezos.
- Mezclas de condimentos.
- Conservación, congelación y organización semanal.

El sistema debe contemplar distintos patrones alimentarios, vegetarianos y omnívoros, sin convertir las proteínas animales en componentes obligatorios.

#### C. ORGANIZAR LAS COMIDAS Y LOS HÁBITOS

No alcanza con saber qué alimentos son saludables ni cómo prepararlos.

También necesitamos enseñar:

- Cómo resolver desayunos y meriendas.
- Cómo armar almuerzos y cenas completos.
- Cómo organizar compras.
- Cómo cocinar una vez y aprovechar los alimentos varios días.
- Cómo improvisar con lo disponible.
- Cómo alimentarse saludablemente con poco tiempo o presupuesto.
- Cómo ajustar porciones y combinaciones a diferentes necesidades.

Este bloque transforma una biblioteca de recetas en un programa de aprendizaje de hábitos.

### 5. Una línea especial: las MERENCENAS

Propongo desarrollar un subproducto llamado **MERENCENAS**.

Consistirá en meriendas completas y suficientemente abundantes para reemplazar la cena tradicional.

No hablamos simplemente de un yogur o una fruta, sino de una comida nutricionalmente suficiente que funcione como última ingesta del día.

Esto permitiría explorar una alimentación más temprana, con una ventana nocturna prolongada sin ingestas calóricas.

La crononutrición proporciona fundamentos interesantes, especialmente en relación con sensibilidad a la insulina y metabolismo glucémico.

Podría ser particularmente útil en determinados pacientes con resistencia a la insulina o alteraciones glucémicas, aunque no debemos asumir beneficios uniformes ni imponer un ayuno de 16 horas a toda la población.

Deberemos desarrollar ejemplos concretos, horarios, adaptaciones, contraindicaciones y criterios de seguimiento.

Me interesa que las merencenas se conviertan en una herramienta práctica que facilite la vida, no en una nueva regla rígida.

### 6. Cómo deben construirse los materiales

Propongo tres niveles de profundidad.

**Nivel 1. Ficha visual.** Idealmente una página, clara, atractiva y directamente aplicable.

**Nivel 2. Guía práctica ampliada.** Variaciones, sustituciones, problemas frecuentes, organización y explicaciones accesibles.

**Nivel 3. Documento técnico profesional.** Fundamentos, evidencia, limitaciones y bibliografía verificable.

No todos los contenidos necesitarán tres documentos independientes.

Lo importante es que podamos ofrecer simplicidad a quien la necesita y profundidad a quien la busca, sin perder información.

El diseño deberá ser coherente, legible, agradable e identificable como parte de una misma colección.

Cada pieza tendrá su identidad y relaciones con otras piezas, para evitar repeticiones innecesarias.

### 7. Los bots como herramientas de acompañamiento

Este punto es fundamental para el futuro producto.

**No queremos que el programa dependa exclusivamente de documentos que las personas reciben y después abandonan.**

Estamos explorando desde hace tiempo distintos asistentes y bots, algunos ya esbozados o parcialmente diseñados. Debemos considerar cómo aprovechar ese trabajo en lugar de empezar nuevamente desde cero.

Entre ellos aparecen el concepto de Nutribot, los bots de indicaciones y seguimiento, y la posible integración futura con Tendrel y otros sistemas existentes.

Claude Code deberá revisar los proyectos y diseños disponibles que Francisco autorice, identificar qué funcionalidades pueden reutilizarse y proponer una arquitectura coherente. No debe suponerse que todos esos desarrollos están terminados ni iniciar integraciones sin una decisión específica.

Me imagino diferentes funciones.

**Bot educativo.** Responde preguntas sobre el contenido del programa y explica conceptos utilizando nuestras fuentes y materiales validados.

**Bot culinario.** Ayuda a decidir qué cocinar según los ingredientes disponibles, preferencias, tiempo y necesidades nutricionales. Puede utilizar las fórmulas universales de nuestro sistema.

**Bot de organización.** Ayuda con compras, preparación semanal, conservación y planificación de comidas.

**Bot de acompañamiento.** Mantiene contacto con el paciente, pregunta cómo está avanzando, identifica dificultades y propone soluciones concretas.

**Bot de seguimiento clínico.** Recopila información relevante para el profesional dentro de un esquema autorizado, sin tomar decisiones médicas autónomas.

Estas funciones no necesitan convertirse en cinco bots diferentes. Podrían integrarse dentro de un mismo asistente con distintos módulos.

**La idea es que los bots apliquen una base de conocimiento creada, revisada y aprobada por nosotros**, en lugar de inventar recomendaciones desde cero en cada conversación.

Además, tendremos que definir cómo actualizamos esa base de conocimiento una sola vez para que los cambios se propaguen a los distintos canales.

No queremos desarrollar bots por el atractivo tecnológico. Cada función tiene que resolver un problema real de las personas o mejorar de manera concreta la eficiencia del programa.

### 8. Seguimiento de pacientes: una pieza central

La educación, por sí sola, no garantiza cambios de comportamiento.

Una persona puede comprender perfectamente las recomendaciones y no conseguir incorporarlas a su rutina.

Por eso debemos diseñar un sistema de seguimiento que permita conocer cómo evolucionan los participantes, qué dificultades encuentran y qué podemos hacer para ayudarlos.

El sistema debe ser útil tanto para pacientes que están realizando una consulta médica como para personas que más adelante contraten el programa de autogestión de forma independiente.

**Evaluación inicial**

Al ingresar, sería conveniente registrar algunos aspectos:

- Objetivos personales y motivos para participar.
- Hábitos alimentarios actuales.
- Disponibilidad de tiempo y recursos.
- Experiencia culinaria.
- Dificultades percibidas.
- Necesidades nutricionales y condiciones de salud relevantes.
- Nivel inicial de conocimientos y confianza para realizar cambios.

No necesitamos crear un interrogatorio interminable. Hay que identificar las pocas variables que realmente ayuden a personalizar el acompañamiento.

**Seguimiento periódico**

Los bots podrían realizar preguntas breves, por ejemplo:

- ¿Pudiste incorporar legumbres esta semana?
- ¿Probaste alguna de las preparaciones?
- ¿Qué fue lo que más te costó?
- ¿Te resultaron agradables las comidas?
- ¿Qué cambio te gustaría trabajar ahora?

El sistema debería registrar tendencias sin convertir cada comida en una obligación de rendir cuentas.

**Identificación de barreras**

Es importante distinguir entre problemas de conocimiento, tiempo, costo, organización, tolerancia digestiva, gustos, motivación o dificultades del entorno familiar.

Cada barrera necesita una respuesta diferente.

Si alguien no consume legumbres porque no tiene tiempo para cocinarlas, darle una nueva explicación sobre sus beneficios probablemente no cambie nada. Necesita herramientas de organización.

**Evaluación de resultados**

Deberíamos medir diferentes dimensiones:

- Comprensión y habilidades adquiridas.
- Cambios de comportamiento.
- Adherencia y continuidad en el programa.
- Satisfacción y facilidad de uso.
- Resultados clínicos cuando corresponda: peso, perímetro abdominal, presión arterial, glucemias, HbA1c, perfil lipídico, síntomas digestivos u otros indicadores pertinentes.

No todas las personas necesitan los mismos controles, ni todo cambio saludable tiene que reflejarse en un laboratorio.

También debemos evitar presentar la mera utilización de la plataforma como prueba de mejoría clínica.

**Retroalimentación y adaptación**

La información recopilada debe servir para ajustar el acompañamiento.

Si una persona no avanza, el sistema debería intentar comprender qué sucede y ofrecer alternativas razonables.

La finalidad no es controlar al paciente, sino ayudarlo a sostener hábitos saludables con el menor esfuerzo innecesario.

Será necesario definir consentimiento, protección de información sanitaria, límites de automatización y situaciones que requieran intervención profesional.

El seguimiento no debe depender de mensajes constantes ni transformarse en una fuente de ansiedad o culpa.

### 9. Adherencia: cómo convertir aprendizaje en hábitos

Creo que esta será una de las principales dificultades y también una de las oportunidades de diferenciación del producto.

Muchos programas de salud ofrecen información correcta. Bastantes menos consiguen acompañar de manera efectiva su aplicación cotidiana.

Podríamos diseñar un recorrido progresivo en lugar de entregar todo el contenido de golpe.

Por ejemplo:

Una persona empieza aprendiendo a cocinar legumbres. Durante la primera semana prepara y congela algunas porciones. Después aprende a hacer medallones o hummus. Más adelante incorpora ensaladas completas.

Cada incorporación se apoya en la habilidad adquirida anteriormente.

Este aprendizaje progresivo podría combinarse con:

- Objetivos pequeños y realizables.
- Recordatorios oportunos.
- Evaluaciones breves.
- Refuerzo de los avances.
- Soluciones personalizadas ante obstáculos.
- Posibilidad de retomar después de interrupciones, sin penalizaciones.

No debemos confundir adherencia con obediencia perfecta a una dieta.

Una persona puede estar progresando aun cuando no cumpla todas las sugerencias. De hecho, el sistema debería ayudar a desarrollar flexibilidad y autonomía.

Con el tiempo, podríamos estudiar qué intervenciones mejoran realmente la continuidad y los resultados.

### 10. El modelo de negocio: queremos ganar dinero

Este objetivo debe quedar explícito desde el diseño inicial.

Queremos desarrollar un producto comercial de autogestión de salud que pueda generar ingresos de manera sostenida y, eventualmente, crecer más allá de nuestra propia consulta.

Para ello debemos pensar desde el principio en:

**Producto gratuito o de entrada.** Algunas fichas, infografías o herramientas sencillas pueden servir para dar a conocer el sistema y demostrar su utilidad.

**Programa educativo pago.** Un recorrido estructurado que combine contenidos, preparaciones, planificación, objetivos y seguimiento.

**Suscripción con acompañamiento.** Acceso continuo a herramientas, bots, nuevas preparaciones, personalización y seguimiento automatizado, con distintos niveles de servicio.

**Programas específicos.** Versiones orientadas a necesidades concretas, como alimentación cardiometabólica, prediabetes, dislipemias, control de peso o salud digestiva, con las debidas delimitaciones clínicas.

**Uso profesional o institucional.** En el futuro, podríamos ofrecer herramientas a otros profesionales, consultorios o instituciones mediante licencias.

No tenemos que decidir ahora el precio ni el modelo comercial definitivo.

Pero sí debemos diseñar una arquitectura que permita ofrecer diferentes niveles de acceso y servicios sin duplicar todo el contenido.

También deberíamos tener en cuenta desde el principio los costos reales: producción y actualización científica, mantenimiento de software, utilización de modelos de IA, atención humana, soporte, adquisición de clientes y seguridad de los datos.

**No alcanza con conseguir usuarios: necesitamos ofrecer valor suficiente para que quieran pagar y permanecer.**

La rentabilidad dependerá de encontrar un equilibrio entre utilidad, costo de prestación, precio y retención.

Debemos evitar que el crecimiento del número de clientes obligue a multiplicar proporcionalmente las horas de trabajo profesional.

Y la comercialización no debe depender de inducir consultas, suplementos o compras innecesarias. El valor del producto debe sostenerse por sus propias herramientas educativas y de acompañamiento.

### 11. El futuro programa de autogestión de salud

La alimentación será uno de los primeros pilares, pero no necesariamente el único.

En una etapa posterior, el programa podría incorporar:

- Actividad física.
- Sueño y ritmos circadianos.
- Estrés y herramientas de regulación emocional.
- Organización de hábitos cotidianos.
- Seguimiento de objetivos de salud.

El contenido alimentario debería poder integrarse a este sistema más amplio sin tener que rehacerse.

Por eso cada pieza debe contar con identidad, objetivo educativo, fuentes, versión, estado de aprobación y relaciones con otros contenidos.

La futura experiencia podría integrar materiales educativos, bots, tareas, seguimiento y comunicación con profesionales cuando corresponda.

No necesitamos programar toda esa plataforma en esta etapa. Pero sí evitar decisiones editoriales o técnicas que dificulten su construcción posterior.

### 12. Cómo vamos a trabajar

El brazo ejecutor será **Claude Code**, sobre el repositorio de GitHub existente.

Su función será organizar, editar, crear materiales, mantener las versiones y registrar el avance.

Las decisiones científicas, pedagógicas y estratégicas podrán contrastarse con ChatGPT y otros modelos o especialistas cuando sea útil y existan los canales disponibles.

Queremos trabajar como un equipo de consultores, con una ejecución técnica centralizada.

No necesitamos que todos estén de acuerdo. Las discrepancias bien fundamentadas son útiles para detectar errores y mejorar las decisiones.

La última decisión clínica, editorial y estratégica corresponde a Francisco.

Un principio importante: no queremos asistentes que simplemente confirmen las ideas iniciales.

Pero tampoco queremos transformar una receta sencilla en un documento lleno de advertencias triviales o tecnicismos que dificulten su uso.

El criterio será **máxima utilidad práctica con rigor científico suficiente y verificable**.

También debemos mantener una diferencia clara entre contenido aprobado, borradores, hipótesis y recomendaciones que necesitan revisión.

### 13. Orden de trabajo

Ahora mismo **la prioridad es construir el esqueleto completo, no desarrollar de golpe todos los contenidos ni programar todos los bots**.

Propongo esta secuencia:

**Etapa 1. Arquitectura general**

Crear el índice maestro del sistema:

- Fichas de alimentos.
- Preparaciones universales.
- Organización alimentaria.
- Merencenas.
- Módulos clínicos.
- Bots y herramientas.
- Seguimiento y adherencia.
- Futuros componentes comerciales.

Para cada pieza registrar propósito, destinatario, formato, relaciones, prioridad y estado.

**Etapa 2. Arquitectura del acompañamiento**

Definir qué datos necesitamos recoger, qué objetivos podremos seguir, cómo intervendrán los bots y cuándo se necesitará un profesional.

Diseñar el flujo conceptual sin desarrollar todavía toda la tecnología.

**Etapa 3. Sistema editorial**

Definir plantillas de infografías, guías ampliadas, documentos científicos y materiales interactivos.

**Etapa 4. Primer conjunto piloto**

Trabajar sobre medallones, legumbres, fibra, hummus, yogures y ensaladas completas.

Usar este conjunto para comprobar si el sistema es coherente, práctico y comprensible.

**Etapa 5. Validación**

Probar los materiales y el acompañamiento con participantes reales, idealmente de distintas edades y niveles educativos.

Evaluar comprensión, facilidad de ejecución, costos, aceptación de las comidas, adherencia y resultados pertinentes.

**Etapa 6. Ampliación**

Completar progresivamente la biblioteca, las merencenas y los programas por patología.

**Etapa 7. Producto comercial**

Diseñar y validar una primera versión vendible, utilizando los materiales y herramientas que hayan demostrado utilidad.

Registrar costos, ingresos, permanencia de los participantes y carga de trabajo profesional para comprobar si el modelo resulta económicamente viable.

No necesitamos esperar a tener una biblioteca gigantesca para probar si existe demanda por el producto.

### 14. El resultado que buscamos

Imaginemos a una persona que termina una consulta y recibe una recomendación de consumir más legumbres.

En lugar de llevarse solamente un folleto, podrá comprender por qué son importantes, aprender a prepararlas, disponer de fórmulas para elaborar distintas comidas y contar con un asistente que la ayude cuando aparezcan dificultades.

Días después, el sistema podrá preguntarle si consiguió incorporarlas, identificar obstáculos y sugerir soluciones.

El profesional podrá conocer la evolución sin tener que intervenir manualmente en cada pequeño paso.

Otra persona utilizará el programa para mejorar su consumo de fibra. Otra para organizar sus comidas. Otra para explorar una alimentación más temprana. Todas compartirán una biblioteca educativa común, adaptada a sus necesidades.

Y algunas personas podrán utilizar estas herramientas sin estar necesariamente bajo seguimiento médico individual.

**El producto que buscamos no es una dieta, una colección de recetas ni un chatbot. Es un sistema que enseña, acompaña y ayuda a sostener cambios saludables.**

Su valor dependerá de que realmente funcione para las personas y de que podamos ofrecerlo a una escala económicamente sostenible.

Nuestra primera tarea es construir correctamente su arquitectura.

Después iremos desarrollando, probando y mejorando sus componentes, sin perder de vista los dos resultados que buscamos: **mejorar la capacidad de las personas para cuidar su salud y construir un negocio rentable alrededor de ese valor**.
