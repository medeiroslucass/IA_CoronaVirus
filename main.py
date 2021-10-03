import pandas as pd
import numpy as np
from dados import atributos, resultados
from sklearn.naive_bayes import GaussianNB

# Triagem paciente
print("-"* 30)
print('Responda as perguntas com 0 para nao e 1 para sim.')
index = ['Febre', 'Cansaco', 'tosse seca', 'Espirro', 'dores no corpo', 'coriza', 'dor de garganta', 'diarreia', 'dor de cabeca', 'falta de ar']
novos = []
for i in index:
    resposta = int(input(f"Apresenta {i}?\n"))
    if resposta != 1 or 0:
        print('resposta invalida.Por favor responda 1 para sim e 0 para nao.')
        resposta = int(input(f"Apresenta {i}?\n"))
    novos.append(resposta)
a = []
a.append(novos)

# Tratando os dados
sintomas = np.array(atributos)
sintomas = sintomas[:,0:]


# Criando o modelo
modelo = GaussianNB()
modelo.fit(sintomas, resultados)


# Previsao
results = modelo.predict(a)
print(results)

# Condicao de Resultados
if results == 1:
    print('Voce esta com corona')
else:
    print('voce esta saudavel')