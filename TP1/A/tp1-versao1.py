#!/usr/bin/python3
import re
from num2words import num2words

lingua = 'pt'


# Função de limpeza de texto.
def cleanText(texto):
    # Substituí todos os números separados por vírgula por números separados por ponto
    texto = re.sub(r'(\d+),(\d+)',r'\1.\2',texto)
    # Adiciona um espaço antes de vírgulas seguidas de números
    texto = re.sub(r'(\w+),|(\d+),', r'\1 , \2',texto)
    # Adiciona um espaço antes de pontos seguidas de números
    texto = re.sub(r'(\d+)\. ', r'\1 .',texto)
    # Adiciona um espaço antes de percentagens seguidas de números
    texto = re.sub(r'(\d+)%',r'\1 %',texto)
    return texto

# Função que abre o ficheiro, lê e converte o texto, escrevendo por fim o resultado no ficheiro output.txt
def numeroParaExtenso(filename):
    file = open(filename)
    texto = file.read()
    texto = cleanText(texto)
    out = open('output.txt','w')
    for i in texto.split(' '):
        numero = re.match(r'\d+',i)
        if numero:
            try:
                temp = num2words(float(i),lang= lingua)
                texto = re.sub(i,temp,texto)
            except NotImplementedError:
                temp = num2words(float(i),lang= 'eng')
                texto = re.sub(i,temp,texto)
        texto = re.sub(r'%',r'por cento',texto)
    out.write(texto)
    return texto

numeroParaExtenso('input.txt')
