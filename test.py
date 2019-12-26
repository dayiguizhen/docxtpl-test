import jinja2
from docxtpl import InlineImage, DocxTemplate
from docx.shared import Mm


# template = DocxTemplate('template.docx')
template = DocxTemplate('template_without_line.docx')


def get_inline_image(template):
    inline_image = {}
    inline_image['img1'] = InlineImage(template, 'img1.png', width=Mm(146.4))
    inline_image['img2'] = InlineImage(template, 'img2.png', width=Mm(146.4))
    inline_image['img3'] = InlineImage(template, 'img3.png', width=Mm(146.4))
    inline_image['img4'] = InlineImage(template, 'img4.png', width=Mm(146.4))
 
    return inline_image


data = get_inline_image(template)
jinja_env = jinja2.Environment(autoescape=True)

template.render(data, jinja_env)

template.save('result.docx')
