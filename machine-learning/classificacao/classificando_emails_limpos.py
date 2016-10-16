#!-*- coding: utf8 -*-
from collections import Counter
# from sklearn.cross_validation import cross_val_score
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
import nltk

# nltk.download('punkt')
classificacoes = pd.read_csv('csv/emails.csv', encoding='utf-8')
textosPuros = classificacoes['email']
frases = textosPuros.str.lower()
textosQuebrados = [nltk.tokenize.word_tokenize(frase) for frase in frases]

# nltk.download('stopwords')
# Remove palavras comum que não precisamos utilizar para avaliarmos o nosso texto, são chamadas de palavras de parada, ou
# tecnicamente, stop words.
stopwords = nltk.corpus.stopwords.words('portuguese')

# nltk.download('rslp')
# Tira o sufixo e fica com a raiz da palavra.
# EX: stemmer.stem("cachorros") => u'cachorr'
stemmer = nltk.stem.RSLPStemmer()

dicionario = set()
for lista in textosQuebrados:
    validas = [stemmer.stem(palavra) for palavra in lista if palavra not in stopwords and len(palavra) > 2]
    dicionario.update(validas)
# print dicionario

totalDePalavras = len(dicionario)
tuplas = zip(dicionario, xrange(totalDePalavras))
tradutor = {palavra: indice for palavra, indice in tuplas}
print "total de Palavras : {0}".format(totalDePalavras)


def vetorizar_texto(texto, tradutor):
    vetor = [0] * len(tradutor)

    for palavra in texto:
        if len(palavra) > 0:
            raiz = stemmer.stem(palavra)
            if raiz in tradutor:
                posicao = tradutor[raiz]
                vetor[posicao] += 1

    return vetor


vetoresDeTexto = [vetorizar_texto(texto, tradutor) for texto in textosQuebrados]
# print vetoresDeTexto[0]
marcas = classificacoes['classificacao']

X = np.array(vetoresDeTexto)
Y = np.array(marcas.tolist())

porcentagem_de_treino = 0.8

tamanho_do_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_validacao = len(Y) - tamanho_do_treino

print "Tamanho do treino : {0}".format(tamanho_do_treino)

treino_dados = X[0:tamanho_do_treino]
treino_marcacoes = Y[0:tamanho_do_treino]

validacao_dados = X[tamanho_do_treino:]
validacao_marcacoes = Y[tamanho_do_treino:]


def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes):
    k = 10
    scores = cross_val_score(modelo, treino_dados, treino_marcacoes, cv=k)
    taxa_de_acerto = np.mean(scores)

    msg = "Taxa de acerto do {0}: {1}".format(nome, taxa_de_acerto)
    print msg
    return taxa_de_acerto


resultados = {}

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

modeloOneVsRest = OneVsRestClassifier(LinearSVC(random_state=0))
resultadoOneVsRest = fit_and_predict("OneVsRest", modeloOneVsRest, treino_dados, treino_marcacoes)
resultados[resultadoOneVsRest] = modeloOneVsRest

from sklearn.multiclass import OneVsOneClassifier

modeloOneVsOne = OneVsOneClassifier(LinearSVC(random_state=0))
resultadoOneVsOne = fit_and_predict("OneVsOne", modeloOneVsOne, treino_dados, treino_marcacoes)
resultados[resultadoOneVsOne] = modeloOneVsOne

from sklearn.naive_bayes import MultinomialNB

modeloMultinomial = MultinomialNB()
resultadoMultinomial = fit_and_predict("MultinomialNB", modeloMultinomial, treino_dados, treino_marcacoes)
resultados[resultadoMultinomial] = modeloMultinomial

from sklearn.ensemble import AdaBoostClassifier

modeloAdaBoost = AdaBoostClassifier()
resultadoAdaBoost = fit_and_predict("AdaBoostClassifier", modeloAdaBoost, treino_dados, treino_marcacoes)
resultados[resultadoAdaBoost] = modeloAdaBoost
print resultados
maximo = max(resultados)
vencedor = resultados[maximo]
print "Vencedor: "
print vencedor

vencedor.fit(treino_dados, treino_marcacoes)
resultado = vencedor.predict(validacao_dados)
print resultado
acertos = (resultado == validacao_marcacoes)

total_de_acertos = sum(acertos)
total_de_elementos = len(validacao_marcacoes)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

msg = "Taxa de acerto do vencedor entre os dois algoritmos no mundo real: {0}".format(taxa_de_acerto)
print(msg)


# a eficacia do algoritmo que chuta
# tudo um unico valor
acerto_base = max(Counter(validacao_marcacoes).itervalues())
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)
print("Total de testes: %d " % len(validacao_dados))




# Testando outras frases.

texto1 = "tenho direito a desconto?"
print "Valida a frase -> : {0}".format(texto1)


texto1Example = [nltk.tokenize.word_tokenize(texto1.lower())]
vetorTexto1 = [vetorizar_texto(texto, tradutor) for texto in texto1Example]
texto1Preparado = np.array(vetorTexto1)

resultadoTexto1 = vencedor.predict(texto1Preparado)
print resultadoTexto1


texto2 = [unicode( "Gostaria de receber informações sobre o curso de java!", "utf-8" ), "Como trocar o player?"]
print "Valida as 2 frase abaixo: \n Frase 1 : - {0} \n Frase 2 : - {1}".format(texto2[0].encode( "utf-8" ),texto2[1])
texto2Example = [nltk.tokenize.word_tokenize(frase) for frase in texto2]
vetoresDeTexto2 = [vetorizar_texto(texto, tradutor) for texto in texto2Example]
texto2Preparado = np.array(vetoresDeTexto2)

resultadoTexto2 = vencedor.predict(texto2Preparado)
print resultadoTexto2