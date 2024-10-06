# Importação da biblioteca para ler o arquivo csv
import csv

# Carregar as informações do arquivo
#x = dados
#y = marcações
def carregar_acessos():
    X = []
    Y = []

    # Designando a função arquivo
    arquivo = open('C:\\Users\\mibin\\PycharmProjects\\PythonAprendizado\\dados.py\\acesso.csv', 'r')

    # Função para abrir o arquivo
    with arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)

        #Pega o nome de cada coluna do arquivo para leitura
        for home, como_funciona, contato, comprou in leitor:


            #Adicionando os dados.py as colunas(COMO STRING)
            #X.append([acessou_home, acessou_como_funciona, acessou_contato])

            #Selecionando apenas como inteiros
            #X.append([int(acessou_home), int(acessou_como_funciona), int(acessou_contato)]), Y.append(int(comprou))

            #Organizando o nome dos dados
            X.append([int(home), int(como_funciona), int(contato)])

            #Adicionando as marcações
            Y.append(int(comprou))
    #Retorno dos dados
    return X, Y
X, Y = carregar_acessos()

# Exibir os dados carregados para ver se estão corretos
#print(X)
#print(Y)

#Testando o modelo
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(X, Y)
treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)

diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)
print(total_de_elementos)