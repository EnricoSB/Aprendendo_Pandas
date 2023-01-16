# -Utilizando um par de parênteses: ()
tupla = (1,2,3)

# -Utilizando uma vírgula à direita: x,
tupla = 1,2,3

# -Utilizando um par de parênteses com itens separados por vírgulas: (x,y,z)
tupla = (1,2,3)

# -Utilizando: tuple() ou tuple(iterador)
nome_tupla = tuple(['Informação','Nome','Outra informação'])

# Acessando informações em tuplas
tupla=('Joao','40',('Fusca','Gol'))
print(tupla[-1][1])
# Ele está acessando a informação da tupla dentro da tupla e pegando a informação que está na posição 1

# Iteração com Tuplas
for item in tupla:
    print(item)

# Desempacotando tuplas:
a,b,c = tupla
print(c)
# Quando eu quiser pular algum item eu coloco o nome da variavel como '_'
_,a,_ = tupla
print(a)
# Quando eu quiser ignorar todos os items após a informação que eu necessito eu coloco somente o '*_' depois:
y,*_=tupla
print(y)

# Tranformando listas em conjunto de tuplas:
nomes = ['Joao','Carlos','Rodrigo']
idade = [23,13,42]
tupla = list(zip(nomes,idade))
print(tupla)
# Iterando sobre essa tupla:
for item in tupla:
    print(item)
# Iterando e desempacotando:
for nome,valor in zip(nomes,idade):
    print(nome)