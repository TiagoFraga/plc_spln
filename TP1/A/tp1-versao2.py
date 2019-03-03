#!/usr/bin/python3
import re




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
        if len(numero) == 3:
            temp = list(numero)
            aux1 = temp[0] + '00'
            aux2 = temp[1] + '0'
            aux3 = temp[1] + temp[2]
            # Representar ex:101
            if temp[0] == '1' and temp[1] == '0':
                return 'cento e ' + dic_numeros[temp[2]]
            else:
                #Representar ex:110,111
                if temp[0] == '1' and temp[1] == '1':
                    return 'cento e ' + dic_numeros[aux3]
                else:
                     #Representar ex:121,122
                    if temp[0] == '1' and temp[2] == '0':
                        return 'cento e ' + dic_numeros[aux2]  
                    else:
                        if temp[0] == '1':
                            return 'cento e ' + dic_numeros[aux2] + dic_numeros[temp[2]]
                        else: 
                        #representar ex:201
                            if temp[1] == '0':
                                return dic_numeros[aux1] + ' e ' + dic_numeros[temp[2]]
                            else:
                                #representar ex:211
                                if temp[1] == '1':
                                    return dic_numeros[aux1] + ' e ' + dic_numeros[aux3]
                                else:
                                    return dic_numeros[aux1] + ' e ' + dic_numeros[aux2] + ' e ' + dic_numeros[temp[2]]
        else:
            if len(numero) == 4:
                temp = list(numero)
                aux1 = temp[0] + '000'
                aux2 = temp[1] + '00'
                aux3 = temp[2] + '0'
                aux4 = temp[2] + temp[3]
                if temp[1] == '0' and temp[2] == '0':
                    return dic_numeros[aux1] + ' e ' + dic_numeros[temp[3]]
                else:
                    if temp[1] == '0' and temp[2] == '1':
                        return dic_numeros[aux1] + ' e ' + dic_numeros[aux4]
                    else:
                        if temp[1] == '0':
                            return dic_numeros[aux1] + ' e ' + dic_numeros[aux3] + ' e ' + dic_numeros[temp[3]]
                        else:
                            if temp[1] == '1' and temp[2] == '0':
                                return dic_numeros[aux1] + ' cento e ' + dic_numeros[temp[3]]
                            else:
                                if temp[1] == '1' and temp[2] == '1':
                                    return dic_numeros[aux1] + ' cento e ' + dic_numeros[aux4]
                                else:
                                    if temp[1] == '1':
                                        return dic_numeros[aux1] + ' cento e ' + dic_numeros[aux3] + ' e ' + dic_numeros[temp[3]]
                                    else:
                                        if temp[2] == '0':
                                            return dic_numeros[aux1] + ' ' + dic_numeros[aux2] + ' e ' + dic_numeros[temp[3]]
                                        else:
                                            if temp[2] == '1':
                                                return dic_numeros[aux1] + ' ' + dic_numeros[aux2] + ' e ' + dic_numeros[aux4]
                                            else:
                                                return dic_numeros[aux1] + ' ' + dic_numeros[aux2] + ' e ' + dic_numeros[aux3] + ' e ' + dic_numeros[temp[3]] 
                    

def numeroParaExtenso(filename,dic):
    file = open(filename)
    texto = file.read()
    texto = cleanText(texto)
    out = open('output.txt','w')
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
            else:
                numero = traduz(word,dic_numeros)
                texto = re.sub(word,numero,texto)
        texto = re.sub(r'%',r'por cento',texto)
    out.write(texto)
    return texto


numeroParaExtenso('input.txt',dic_numeros)









