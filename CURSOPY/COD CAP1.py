from sklearn.naive_bayes import MultinomialNB

# Dados de treinamento
# [é gordinho?, tem perninha curta?, faz auau?]
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]  # Características: animais

marcacoes = [1, 1, 1, -1, -1, -1]  # Labels: 1 = porco, 0 = cachorro

# Criação do modelo
modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

# Teste do modelo com um novo conjunto de dados.py desconhecidos
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

teste = [misterioso1, misterioso2, misterioso3]  # Novos exemplos: novas caracteristicas de animal

marcacoes_teste = [-1, 1, -1]
resultado = modelo.predict(teste)

diferencas = resultado - marcacoes_teste
acertos = [d for d in diferencas if d == 0]
#Quantidade de acertos do array
total_de_acertos = len(acertos)
total_de_elementos = len(teste)
#Taxa de acerto em porcentagem
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(resultado)
print(diferencas)
print(taxa_de_acerto)