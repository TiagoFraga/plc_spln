#!/usr/bin/python3
import re
from num2words import num2words

lingua = 'pt'

def cleanText(texto):
    texto = re.sub(r'(\d+),(\d+)',r'\1.\2',texto)
    texto = re.sub(r'(\w+),|(\d+),', r'\1 , \2',texto)
    texto = re.sub(r'(\d+)\. ', r'\1 .',texto)
    texto = re.sub(r'(\d+)%',r'\1 %',texto)
    return texto


def criarDic():
    file = open('numeros.txt')
    dic_numeros = {}
    for line in file.readlines():
        line = line.rstrip()
        key = line.split('-')[0]
        value = line.split('-')[1]
        dic_numeros[key]=value
    return dic_numeros

dic_numeros = {}
dic_numeros = criarDic()


def traduz(numero,dic_numeros):
    if numero in dic_numeros:
        return dic_numeros[numero]
    else:
        if re.match(r'\w{3}',numero):
            temp = list(numero)
            aux1 = temp[0] + '00'
            aux2 = temp[1] + '0'
            if temp[1] == '0':
                return dic_numeros[aux1] + ' e ' + dic_numeros[temp[2]]
            elif temp[2] == '0':
                return dic_numeros[aux1] + ' e ' + dic_numeros[aux2]
            else:
                aux3 = temp[1] + temp[2]
                if temp[1] == '1':
                    return dic_numeros[aux1] + ' e ' + dic_numeros[aux3]
                else:
                    if temp[0] == '1': 
                        return 'cento e' + dic_numeros[aux3]
                    else:    
                        return dic_numeros[aux1] + ' e ' + dic_numeros[aux2] + ' e ' + dic_numeros[temp[2]]
        else:
            if re.match(r'\w{4}',numero):
                temp = list(numero)
                aux1 = temp[0] + '000'
                aux2 = temp[1] + '00'
                aux3 = temp[2] + '0'
                aux4 = temp[2] + temp[3]
                if temp[0] == '1' and temp[1] == '0' and temp[2] == '0':
                    return 'mil e ' + dic_numeros[temp[3]]
                else: 
                    if temp[0] == '1' and temp[1] == '0' and temp[2] == '1':
                        return 'mil e ' + dic_numeros[aux4]
                    else:
                        if temp[0] == '1' and temp[1] == '0':
                            return  'mil e ' + dic_numeros[aux3]  + ' e ' + dic_numeros[temp[3]]
                        else:
                            if temp[0] == '1' and temp[2] == '0' and temp[3] == '0' :
                                return 'mil e ' + dic_numeros[aux2]
                            else:
                                if temp[0] == '1' and temp[1] == '1' and temp[2] == '1':
                                    return 'mil cento e' + dic_numeros[aux4]
                                else:
                                    if temp[0] == '1' and temp[1] == '1' and temp[3] == '0':
                                        return 'mil cento e' + dic_numeros[aux3]
                                    else:
                                        if temp[0] == '1' and temp[1] == '1':
                                            return 'mil cento e' + dic_numeros[aux3] + ' e ' + dic_numeros[temp[3]]
                                        else:
                                            #falta acabar 
                                            if temp[0] == '1' and temp[]:

def numeroParaExtensoV2(filename,dic):
    file = open(filename)
    texto = file.read()
    texto = cleanText(texto)
    for word in texto.split(' '):
        numero = re.match(r'\d+',word)
        if numero:
            if '.' in word:
                aux = word.split('.')
                primeiraParte = aux[0]
                primeiraParte = traduz(primeiraParte,dic_numeros)
                segundaParte = aux[1]
                segundaParte = traduz(segundaParte,dic_numeros)
                result = primeiraParte + ' vírgula ' + segundaParte
                texto = re.sub(word,result,texto)
                print(result)
            else:
                numero = traduz(word,dic_numeros)
                texto = re.sub(word,numero,texto)
        texto = re.sub(r'%',r'por cento',texto)
    return texto



print(numeroParaExtensoV2('input.txt',dic_numeros))



def numeroParaExtenso(filename):
    file = open(filename)
    texto = file.read()
    texto = cleanText(texto)
    for i in texto.split(' '):
        numero = re.match(r'\d+',i)
        if numero:
            try:
                print(i)
                temp = num2words(float(i),lang= lingua)
                texto = re.sub(i,temp,texto)
            except NotImplementedError:
                temp = num2words(float(i),lang= 'eng')
                texto = re.sub(i,temp,texto)
        texto = re.sub(r'%',r'por cento',texto)





#numeroParaExtenso('input.txt')
