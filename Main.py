# para criar uma variável:
# variavel = 'valor'
#nome = "karol"
#sobrenome = "leandro"

# para somar strings:
# 'texto 1' + 'texto 2' -> 'texto1texto2'
#print(nome+sobrenome)

# para obter o tamanho de uma string (texto):
# len('texto') -> 5

# argumento é o que é passado para uma função
# nesse caso, nome é o argumento passado
# o método len retorna o tamanho de uma lista ou string passada como parametro
#print(len(nome))
#print(len(sobrenome))


# para definir uma lista, podemos fazer:
# lista = []

lista = [24, 31, 24, 25, 40, 32]
print(lista)
print(len(lista))

# para acessar um elemento de uma lista ou string, utilizamos [indice]
valor = lista[0]
print(valor)
print(valor * 2)
print(lista[-2])


# para adicionar elementos a uma lista, utiliza-se o método append
novo_valor = 90
lista.append(novo_valor)
#[24, 31, 25, 40, 32, 90]

print(lista)

lista.append(129)
print(lista)

lista.pop()
print(lista)
lista.remove(24)
print(lista)

# um dicionario é um conjunto chave - valor, onde os valores são acessados a partir dos índices "chaves"
# para criar um dicionário:
# dict = {'key': value}
# para acessar um valor do dicionário: dict['key']
value = 'jose roberto'
dicionario = {'nome': value, 'idade': 22, 'sobrenome': 'dsadas', 'cep': 43321123}
print(dicionario)
print(dicionario['nome'], dicionario['idade'])
# adicionar novo par chave - valor ao dicionário
dicionario['chave'] = 'valor'
print(dicionario)
# remover um par chave - valor
dicionario.pop('cep')
print(dicionario)


# criar duas variáveis, uma correspondente ao seu nome e outra à sua idade e criar um dicionário com seu nome e sua idade

value = 'karol'
variavel_idade = 'idade'
dicionario = {'nome': value, 'idade': 22}
print(dicionario)

variavel_altura = 1.67
dicionario['altura'] = variavel_altura
print(dicionario)
dicionario.pop('idade')
print(dicionario)

var_idade = int(input("Digite sua idade: "))
print(var_idade)
lista.append(var_idade)
lista.sort()
print(lista)

# para ordenar os itens, necessário colocar o lista.sort() (espaço em branco) para poder solicitar a impressão dos quesitos

vr_alturas = [1.70, 1.55, 1.60]
# vr_nomes = [carla, laura, pedro]

vr_alturas = []
vr_nomes = []
print(vr_nomes)
# input("Digite seu nome: ")
qtd = int(input("Digite a quantidade: "))
for x in range(qtd):
    nome = input("Digite seu nome: ")
    vr_nomes.append(nome)
    altura = input("Digite sua altura")
    vr_alturas.append(altura)
print(vr_nomes)
print(vr_alturas)
idade = int(input)
# strings de nomes 
# imprimir as duas listas

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print ('verdadeiro')

else:
    print ('falso')

