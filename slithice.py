# Slithice - Módulo Python para processamento de imagens
# Escrita por Daniel Serezane (2022)
# Criada como parte da disciplina de Processamento Digital de Imagens, ministrada na FCT-UNESP

# As operações são feitas, em sua maioria, com base nos métodos
# putppixel e getpixel, que não são os mais eficientes. Contudo,
# são bastante seguros, desta forma evitando problemas.

from PIL import Image


def teste():
    print("oi!!!")


def converte_para_cinza(img):
    out = Image.new("L", (img.width, img.height))
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            gray = (r + g + b) // 3
            out.putpixel((i, j), gray)
    return out


def inverte_cinza(img):
    out = Image.new("L", (img.width, img.height))
    for i in range(img.width):
        for j in range(img.height):
            out.putpixel((i, j), 255 - img.getpixel((i, j)))
    return out
