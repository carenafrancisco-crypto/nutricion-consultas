import copy, sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph

SRC = sys.argv[1]   # carpeta con los originales
OUT = sys.argv[2]   # carpeta de salida
IMG = sys.argv[3]   # png de la infografía

GREEN = RGBColor(0x32, 0x6C, 0x52)
DARK = RGBColor(0x26, 0x45, 0x45)


def paras(d):
    return [Paragraph(el, d._body) for el in d.element.body.iterchildren() if el.tag == qn('w:p')]


def find(d, start):
    hits = [p for p in paras(d) if p.text.startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]


def set_text(p, text):
    """Reemplaza el texto conservando el formato del primer run con texto."""
    runs = [r for r in p.runs if r.text]
    runs[0].text = text
    for r in runs[1:]:
        r._r.getparent().remove(r._r)


def set_tail(p, old, new):
    """Reemplaza un fragmento dentro del último run con texto (los numerados tienen run aparte)."""
    r = [r for r in p.runs if r.text][-1]
    assert old in r.text, (old, r.text)
    r.text = r.text.replace(old, new)


def clone_after(p, text):
    el = copy.deepcopy(p._p)
    p._p.addnext(el)
    q = Paragraph(el, p._parent)
    set_text(q, text)
    return q


def membrete(d):
    hdr = d.sections[0].header
    p0 = hdr.paragraphs[0]
    serie = p0.text
    for r in list(p0.runs):
        r._r.getparent().remove(r._r)
    r = p0.add_run('Dr. Francisco Carena León')
    r.bold = True; r.font.size = Pt(10); r.font.color.rgb = GREEN
    r = p0.add_run('  ·  Médico  ·  Mg. en Psiconeuroinmunoendocrinología  ·  Matrícula 6796L4F20  ·  2026')
    r.font.size = Pt(8); r.font.color.rgb = DARK
    # filete inferior
    pPr = p0._p.get_or_add_pPr()
    bdr = OxmlElement('w:pBdr'); b = OxmlElement('w:bottom')
    for k, v in (('val', 'single'), ('sz', '6'), ('space', '2'), ('color', '326C52')):
        b.set(qn('w:' + k), v)
    bdr.append(b); pPr.append(bdr)
    p1 = hdr.add_paragraph(style=p0.style)
    r = p1.add_run(serie)
    r.font.size = Pt(7.5); r.font.color.rgb = GREEN


def infografia(d, after_p, ancho=6.6):
    p = clone_after(after_p, 'x')
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    p.paragraph_format.page_break_before = True
    p.paragraph_format.alignment = 1
    p.add_run().add_picture(IMG, width=Inches(ancho))


def fill_rows(tbl):
    fills = ['EAF2EC', 'F9F6EF']
    for i, row in enumerate(tbl.rows):
        for j, c in enumerate(row.cells):
            c._tc.tcPr.find(qn('w:shd')).set(qn('w:fill'), fills[(i + j) % 2])


# ---------------------------------------------------------------- práctica
d = docx.Document(f'{SRC}/Guia_practica_medallones_vegetales.docx')
membrete(d)

tbl = d.tables[1]
granos = tbl.rows[1]._tr
pseudo = copy.deepcopy(granos)
granos.addnext(pseudo)
filas = [
    ('1 · Legumbres', 'Lentejas (comunes, rojas o turcas, negras), garbanzos, porotos (negros, colorados, alubia, mung, aduki, pallares), arvejas secas (enteras o partidas), habas, soja.'),
    ('2 · Cereales', 'Avena, arroz (blanco, integral, yamaní), mijo, cebada, maíz (choclo, polenta), trigo burgol, sorgo.'),
    ('3 · Pseudocereales', 'Quinoa, amaranto, trigo sarraceno (alforfón).'),
    ('4 · Sabores', 'Ajo, cebolla, puerro o verdeo salteados; morrón, zanahoria o zapallito rallados; perejil, albahaca, orégano; comino, pimentón, cúrcuma, curry, pimienta. Sal, poca.'),
    ('5 · Para unir / ajustar', 'Huevo opcional. Sin huevo: 1 cucharada de chía o lino molido en 3 de agua, 10 minutos. Si la pasta queda húmeda: avena fina, harina de legumbres o de arroz.'),
]
for row, (a, b) in zip(tbl.rows, filas):
    set_text(row.cells[0].paragraphs[0], a)
    set_text(row.cells[1].paragraphs[0], b)
fill_rows(tbl)

p = find(d, 'Podés combinar las opciones')
set_text(p, 'Podés combinar las opciones según lo que tengas. No hace falta usar todas. '
            '¿Celiaquía? Evitá trigo, cebada y centeno, y usá avena certificada sin TACC.')

set_tail(find(d, '1.  Remojá'), 'agregar un ácido no garantiza por sí solo una fermentación.',
         'agregar un ácido no garantiza por sí solo una fermentación. Si no buscás fermentar y el remojo va a ser largo, hacelo en la heladera.')
set_tail(find(d, '2.  Descartá'), 'Una pizca de bicarbonato puede ayudar a ablandarlas.',
         'Una pizca de bicarbonato puede ayudar a ablandarlas; no te pases: en exceso cambia el sabor y se pierden algunas vitaminas.')
set_tail(find(d, '3.  Escurrí'), 'para tener siempre opciones.',
         'para tener siempre opciones. Duran hasta 3 días en la heladera y hasta 3 meses en el freezer.')
set_tail(find(d, '1.  Procesá'), 'con ajo, sal, pimienta y condimentos', 'con ajo, poca sal, pimienta y condimentos')
set_tail(find(d, '5.  Cocinalos'), 'También podés congelarlos ya formados.',
         'También podés congelarlos ya formados: separalos en una bandeja y, cuando estén duros, guardalos juntos.')

set_text(find(d, 'Cinco combinaciones'), 'Ocho combinaciones para empezar')
last = find(d, 'Soja cocida + amaranto')
for t in reversed(['Porotos negros + choclo + cebolla de verdeo + comino.',
                   'Lentejas rojas + trigo sarraceno + zanahoria rallada + curry.',
                   'Garbanzos + cebada + espinaca + ajo.']):
    clone_after(last, t)

infografia(d, find(d, 'Para entender el remojo'))
d.save(f'{OUT}/Guia_practica_medallones_vegetales_v0.2.docx')

# ---------------------------------------------------------------- ampliada
d = docx.Document(f'{SRC}/Guia_ampliada_medallones_vegetales.docx')
membrete(d)

set_tail(find(d, 'Guía ampliada'), 'entender su fundamento nutricional',
         'entender su fundamento nutricional · Para quien quiere profundizar')

p = find(d, 'Legumbres: lentejas')
set_text(p, 'Legumbres: lentejas (comunes, rojas o turcas, negras), garbanzos, porotos (negros, colorados, alubia, mung, aduki, pallares), '
            'arvejas secas, habas, soja y otras variedades. Cereales: avena, arroz (blanco, integral, yamaní), mijo, cebada, maíz (choclo, polenta), '
            'trigo burgol, sorgo, centeno, teff y otros. Pseudocereales: quinoa, amaranto, trigo sarraceno (alforfón) y otros. '
            'Sabores: ajo, cebolla, puerro y verdeo salteados; morrón, zanahoria o zapallito rallados; hierbas frescas; sal con moderación, '
            'pimienta y especias como comino, pimentón, cúrcuma o curry.')
clone_after(p, 'Para personas con celiaquía: trigo, cebada y centeno (y sus derivados, como el burgol o la espelta) contienen gluten, y la avena '
               'puede estar contaminada, por lo que conviene usarla certificada sin TACC. Quinoa, amaranto, trigo sarraceno, arroz, mijo, maíz, sorgo '
               'y teff no contienen gluten, aunque también conviene elegirlos con sello sin TACC.')

p = find(d, 'Los medallones pueden hacerse con huevo')
set_text(p, p.text + ' Otra opción sin huevo es usar chía o lino molido hidratados (aproximadamente 1 cucharada en 3 cucharadas de agua, durante 10 minutos) como ligante.')
clone_after(p, 'Sobre la sal: conviene usarla con moderación, especialmente en personas con hipertensión arterial. Ajo, cebolla, hierbas, especias '
               'y limón permiten dar sabor con menos sodio.')

set_text(find(d, 'Remojar facilita la hidratación'),
         'Remojar facilita la hidratación y puede reducir ciertos componentes fermentables. El remojo habitual de una noche es una alternativa sencilla. '
         'Algunas preparaciones proponen remojos de 24–36 horas, con un chorrito de vinagre de manzana, limón o kéfir, como parte de un abordaje fermentativo. '
         'Los procesos de fermentación y germinación de legumbres varían en duración y condiciones, y sus efectos sobre los fitatos y otros compuestos '
         'dependen del alimento y del procedimiento [5].')

p = find(d, 'Después del remojo')
set_text(p, p.text.replace('Puede agregarse una pizca de bicarbonato para facilitar el ablandamiento.',
                           'Puede agregarse una pizca de bicarbonato para facilitar el ablandamiento; en cantidades mayores altera el sabor y la textura, '
                           'y aumenta la pérdida de algunas vitaminas del grupo B, como la tiamina, que son sensibles al medio alcalino.'))
p = find(d, 'Una estrategia para ahorrar tiempo')
set_text(p, p.text + ' Las legumbres cocidas se conservan hasta 3 días en la heladera y hasta 3 meses en el freezer.')

p = find(d, 'La calidad de una proteína depende')
set_text(p, p.text + ' Este efecto se estudia desde hace décadas: por ejemplo, ya en 1982 se describió que el valor nutritivo de mezclas de garbanzo '
                     'con cereales depende del tipo de cereal utilizado [6].')

set_text(find(d, 'En una revisión con modelado'),
         'En una revisión con modelado de combinaciones, una mezcla de proteínas de arveja y trigo presentó un máximo estimado de DIAAS 85 con 60% y 40% '
         'de contribución proteica, respectivamente. Para soja y avena, se informó DIAAS 92 con 90% de proteína de soja y 10% de avena [2]. Estos valores '
         'se calcularon con el patrón de referencia para niños de 6 meses a 3 años y con datos de digestibilidad promedio obtenidos en cerdos, no en '
         'preparaciones cocidas. Son resultados específicos de esos ingredientes y modelos, no reglas trasladables a todos los medallones.')
set_text(find(d, 'En otros estudios, combinar'),
         'En otros estudios, combinar no significó superar al mejor alimento de partida. Con digestibilidad medida en cerdos y el patrón para niños mayores, '
         'adolescentes y adultos, se informó un DIAAS de 93 para poroto mung cocido, 22 para mijo cocido y 66 para la mezcla cocida de ambos [3]: la mezcla '
         'mejoró mucho respecto del cereal solo, pero quedó por debajo de la legumbre sola. El huevo, si se agrega, también cambia el perfil proteico del plato.')

last = [p for p in paras(d) if p.text.startswith('Soja cocida + amaranto')][-1]
for t in reversed(['Porotos negros + choclo + cebolla de verdeo + comino.',
                   'Lentejas rojas + trigo sarraceno + zanahoria rallada + curry.',
                   'Garbanzos + cebada + espinaca + ajo.']):
    clone_after(last, t)

set_text(find(d, '2. Herreman'), '2. Herreman L, Nommensen P, Pennings B, Laus MC. Comprehensive overview of the quality of plant- and animal-sourced proteins '
         'based on the digestible indispensable amino acid score. Food Sci Nutr. 2020;8(10):5379–5391. doi:10.1002/fsn3.1809.')
set_text(find(d, '3. Han F'), '3. Han F, Moughan PJ, Li J, Stroebinger N, Pang S. The Complementarity of Amino Acids in Cooked Pulse/Cereal Blends and Effects '
         'on DIAAS. Plants (Basel). 2021;10(10):1999. doi:10.3390/plants10101999.')
set_text(find(d, '5. Anti-nutrient'), '5. Anaemene D, Fadupin G. Anti-nutrient reduction and nutrient retention capacity of fermentation, germination and combined '
         'germination-fermentation in legume processing. Appl Food Res. 2022;2(1):100059. doi:10.1016/j.afres.2022.100059.')

set_tail(find(d, '1.  Procesar'), 'con ajo, sal, pimienta', 'con ajo, poca sal, pimienta')
infografia(d, find(d, '6. Del-Angel'))
d.save(f'{OUT}/Guia_ampliada_medallones_vegetales_v0.2.docx')
print('ok')
