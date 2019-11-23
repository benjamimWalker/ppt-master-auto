from Pptx import Pptx
from Resources import Resources
from glob import glob
from random import choice

themes = glob('Themes/*.pptx')

assunto = input('Qual assunto que eu tenho que fazer? Seu preguiçoso! ')

ppt = Pptx(assunto, choice(themes))

rs = Resources(assunto)
lista = rs.get_text()
rs.get_images(len(lista))
images = glob(f'Images/{assunto}/*.jpg')

ppt.add_title_slide()


for c in range(len(lista)):

    ppt.add_context(lista[c] + '.', images[c])

ppt.add_thanks_for_watching_slide()

ppt.save()
