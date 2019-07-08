from PIL import Image, ImageDraw
import os
import sys

class ComparadorDeImagem:

    def __init__(self):
        self.analyze()

    def analyze(self):

        imagem1 = Image.open("./imagem1.jpg") #Colocar aqui o diretório da primeira imagem a ser comparada
        imagem2 = Image.open("./imagem2.jpg") #Colocar aqui o diretório da segunda imagem a ser comparada
        colunas = 20
        linhas = 20
        tela_altura, tela_largura = imagem1.size

        bloco_largura = ((tela_altura - 1) // colunas) + 1 
        bloco_altura = ((tela_largura - 1) // linhas) + 1


        for y in range(0, tela_largura, bloco_altura+1):
            for x in range(0, tela_altura, bloco_largura+1):
                regiao_imagem1 = self.processar_regiao(imagem1, x, y, bloco_largura, bloco_altura)
                regiao_imagem2 = self.processar_regiao(imagem2, x, y, bloco_largura, bloco_altura)

                #Compara as duas regiões das imagem, e se forem diferentes, ele desenha um retângulo na região
                if regiao_imagem1 is not None and regiao_imagem2 is not None and regiao_imagem2 != regiao_imagem1:
                    draw = ImageDraw.Draw(imagem1)
                    draw.rectangle((x, y, x+bloco_largura, y+bloco_altura), outline = "red")

        imagem1.save("result.png")

    def processar_regiao(self, imagem, x, y, largura, altura):
        regiao_total = 0

        #Fator de sensitividade.
        #quanto maior o fator, menor a sensibilidade
        fator = 100

        for cordenadaY in range(y, y+altura):
            for cordenadaX in range(x, x+largura):
                try:
                    pixel = imagem.getpixel((cordenadaX, cordenadaY))
                    regiao_total += sum(pixel)/4
                except:
                    return

        return regiao_total/fator

ComparadorDeImagem()

