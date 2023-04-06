# Esse arquivo contém as funções utilizadas nos experimentos de algoritmos genéticos 
# Para fins organizacionais, as funções estarão agrupadas em experimentos
# Uma função pode ter sido utilizada em mais de um algoritmo, mas ela estará disponível na seção do primeiro experimetno em que ela foi utilizada.

#---------------------------------
import random 
#---------------------------------

###############################################################################
#                                   Suporte                                   #
##############################################################################+


# NOVIDADE
def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


# NOVIDADE
def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades


###############################################################################
#                           Experimento caixas binárias                       #
#                                busca aleatória                              #
###############################################################################

def gene_caixabinaria():
    """ gera um gene válido para o problema das caixas binarias
    Return:
     Um valor zero ou um.
     """
    lista = [0,1]
    gene = random.choice(lista)
    return gene
     
def individuo_cb(n):
    """ gera um indivíduo para o problema das caixas binárias. 

    Args: 
        n: numero de genes do individuo

    Return:
     Uma lista com n genes. Cada gene é um valor zero ou um.
     """
    individuo = []
    for i in range(n):
        gene = gene_caixabinaria()
        individuo.append(gene)
    return individuo

def funcao_objetivo_cb(individuo):
    """ computa a função objetivo no problema das caixas binárias.
    
    Args: 
        Individuo: lista contendo os genes das caixas binárias

    Return:
        Um valor representando a soma dos genes dos indivíduos.
    """
    return sum(individuo) + 1

###############################################################################
#                           Experimento caixas binárias                       #
#                                  busca em grade                             #
###############################################################################
def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias a partir de individuos
    
    Args: 
    tamanho: tamanho da funcao
    n: numero de genes de um individuo
    
    Returns:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes.
    
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao


###############################################################################
#                           Experimento caixas binárias                       #
#                              algoritmos genéticos                           #
###############################################################################

def funcao_objetivo_pop_cb(populacao):
    """ Calcula a funcao objetivo para todos os membros de um populacao.
    
    Args:
        População: lista com todos os indivíduos da população.
    
    Return: 
        Lista de valores representando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness

def selecao_roleta_max(populacao, fitness):
    """ Seleciona indivíduos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
        população: lista com todos os individuos da populacao
        fitness: lista com o valor da funcao objetivo dos indivíduos da população
        
    Returns:
        População dos indivíduos selecionados.
    
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def cruzamento_ponto_simples(pai, mae):
    """ Operador de cruzamento de ponto simples.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias
    
    Returns:
        Duas listas,s sendo que cada uma representa um filho dos pais que foram os argumentos.
    """

    ponto_de_corte = random.randint(1,len(pai)-1)
        
    filho1 = pai[:ponto_de_corte]+mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte]+pai[ponto_de_corte:]
        
    return filho1, filho2


def mutacao_cb(individuo):
    """ Realiza a mutação de um gene no problema das caixas binárias.
    
    Args: 
        individuo: uma lista representand um indivíduo no problema das caixas binárias
    
    Return:
        Um indivíduo com um gene mutado.
    """
    
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_caixabinaria()
    return individuo


###############################################################################
#                       Experimento caixas não binárias                       #
#                            algoritmos genéticos                             #
###############################################################################

def gene_cnb(valor_max_caixa):
    """ Gera um gene válido para o problema das caixas não binárias.
    
    Arg:
        valor_max_caixa: Valor máximo que a caixa pode assumir
        
    Return: 
        Um valor de 0 a "valor_max_caixa" incluso
    """
    gene = random.randint(0, valor_max_caixa)
    return gene


def individuo_cnb(numero_gene, valor_max_caixa):
    """ Gera um indivíduo válido para o problema das caixas não biárias. Com o número de genes e o valor m´ximo que cada gene assume.
    
    Args:
        numero_genes: numero de genes na lista que representa o individuo
        valor_max_caixa: valor maximo que cada gene pode assumir
        
    Returns:
        Uma lista que representa um individuo válido para o problema das CNB
    """
    individuo = []
    for _ in range(numero_gene):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo


def populacao_cnb(tamanho_populacao, numero_gene, valor_max_caixa):
    """ Cria uma população de individuos para o problema das caixas não-binárias
    
    Args:
        tamanho_populacao: número de indivíduos da população
        numero_genes: número de genes do indivíduo
        valor_max_caixa: valor maximo que a caixa pode assumir
        
    Returns:
        uma lista onde cada item representa um individuo
    """
    populacao = []
    for _ in range(tamanho_populacao):
        populacao.append(individuo_cnb(numero_gene, valor_max_caixa))
    return populacao



def funcao_objetivo_cnb(individuo):
    """ Calcula o fitness do individuo para o problema das caixas não-binárias
    
    Args:
      individiuo: lista contendo os genes das caixas não-binárias
      
    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)


def funcao_objetivo_pop_cnb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população
    
    Args:
      populacao: lista com todos os individuos da população
      
    Return:
      Lista de valores represestando a fitness de cada individuo da população.
    """
    
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cnb(individuo)
        fitness.append(fobj)
    return fitness


def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação de um gene no problema das caixas não-binárias
    
    Args:
    
      individuo:
        uma lista representado um individuo no problema das caixas não-binárias
      valor_max_caixa:
        maior número inteiro possível dentro de uma caixa
        
    Return:
      Um individuo com um gene mutado.
    """
    
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo

###############################################################################
#                        Experimento descobrindo a senha                      #
#                            algoritmos genéticos                             #
###############################################################################
#Esse é um problema de minimização

def gene_letra(letras): #agora os genes são as letras que podemos ter 
    """Sorteia uma letra.
    
    Args:
      letras: letras possíveis de serem sorteadas.
      
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    
    letra = random.choice(letras)
    return letra

def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
      
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato

def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
      
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização. 
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos 
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento "populacao".
    """
    
    selecionados = [] #indivíduos com menor fitnesss

    par_populacao_fitness = list(zip(populacao, fitness)) # zip lsta de tuplas, onde a i-ésima tupla contém o i-ésimo elemento de cada um dos argumentos

    for _ in range(len(populacao)): 
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio) 
        
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness: 
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados 

def mutacao_senha(individuo, letras): 
    """Realiza a mutação de um gene no problema da senha.
    
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
      
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo

def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
      
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira): 
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial)) # ord está permitindo converter a letra em um número
    return diferenca
    
def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
      
    Return:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado

###############################################################################
#                          Experimento liga ternária                          #
#                            algoritmos genéticos                             #
###############################################################################

def gene_lt(valor_max_peso): #valor da massa
    """ gera um gene válido (que pode assumir o valor minímo de l e máximo de l) para o problema da liga ternária mais cara. 
    
    Args: 
        valor_max_peso: o limite de valor que o gene pode assumir
    
    Return:
        gene: um valor dentro das condições
     
     """
    lista = [5,valor_max_peso] #Precisa tirar a possibilidade de o gene assumir o valor de 100
    gene = random.uniform(lista)
    return gene

def individuo_lt(numero_genes):
    """ gera um indivíduo válido para o problema da liga ternária mais cara. 

    Args: 
        numero_genes: numero de genes do individuo

    Return:
        individuo: lista contendo um indivíduo dentro das condições estabelecidas
     """
    # (que contenha apenas 3 valores =! 0 com no valor mínimo de 5 e a soma dentro dos genes do individuo devem ser 100)
    individuo = [0 for _ in range(0,92)] #definindo que a lista tenha 92 itens #aqui a soma em cada individuo é 100, tem que ter 3 e no minimo 5g em cada
    valor_max_peso = 100 
    for _ in range(numero_genes): #se não soma for 100 aí refaz um loop
        while True:
            j = random.uniform(len(individuo))
            if individuo[j] == 0: # o elemento não foi escolhido ainda
                gene = gene_lt(valor_max_peso)
                individuo[j] = gene 
                valor_max_peso = valor_max_peso - gene 
                break
    return individuo

def populacao_inicial_lt(tamanho_populacao, numero_genes): 
    """Cria população inicial no problema da liga ternária
    
    Args
      tamanho_populacao: quantidade de indivíduos em uma população. 
      numero_genes: numero de genes do individuo
      
    Returns:
      Lista com todos os indivíduos da população 
    """
    populacao = []
    for _ in range(tamanho_populacao):
        populacao.append(individuo_lt(numero_genes))
    return populacao

def funcao_objetivo_lt(individuo, preco):
    """ Calcula o fitness do individuo para o problema da liga ternária
    
    Args:
      individiuo: lista contendo os genes das ligas ternárias
      
    Return:
      Um valor representando a fórmula para o cálculo do preço total da liga ternária.
    """
    valor = 0
    for massa, valor_p_kg in zip(individuo, preco.values()):
        valor = valor + (massa*valor_p_kg)/1000 #tranformamos em valor por grama

    return valor #xAbYcZ, pegar o indivíduo e multiplicar pela lista de preços

def funcao_objetivo_pop_lt(individuo, preco): #Salva a lista de todos os fitness de todos os individuos de uma
    """ Calcula a funcao objetivo para todos os membros de um populacao.
    
    Args:
        População: lista com todos os indivíduos da população.
    
    Return: 
        Lista de valores representando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_lt(individuo, preco)
        fitness.append(fobj)
    return fitness


def selecao_torneio_max(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    
    Nota: da forma que está implementada, só funciona em problemas de
    maximização.
    
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos indivíduos
      tamanho_torneio: quantidade de invidiuos que batalham entre si
      
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento "populacao".
    """
    selecionados = []
    par_populacao_fitness = list(zip(populacao, fitness))
    for _ in range(len(populacao)):
        combatentes = rd.sample(par_populacao_fitness, tamanho_torneio)
        maximo_fitness = 0
        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]
            if fit > maximo_fitness:
                selecionado = individuo
                maximo_fitness = fit
        selecionados.append(selecionado)
    return selecionados


def cruzamento_ponto_simples(pai, mae): #DEVE MANTER A SOMA EM 100
    """ Operador de cruzamento de ponto simples.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias
    
    Returns:
        Duas listas em que cada uma representa um filho dos pais que foram os argumentos.
    """

    ponto_de_corte = random.randint(1,len(pai)-1)
    
    #FAZer um laço de repetição que enquanto for verdade a condição soma = 100 corta o gene?
    #mudar a 
        
    filho1 = pai[:ponto_de_corte]+mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte]+pai[ponto_de_corte:]
        
    return filho1, filho2



def mutacao_troca_lt(individuo):
    """ Realiza a mutação de um gene no problema das ligas ternárias.
    
    Args: 
        individuo: uma lista representando um indivíduo no problema das ligas ternárias
    
    Return:
        Um indivíduo com um gene mutado.
    """
    #garantir que a soma continua em 100 
    #troca -> pega um valor e troca em um local onde é 0
    
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1) #aqui tem que ser onde o gene =! 0.
    individuo[gene_a_ser_mutado] = gene_caixabinaria()
    return individuo

###############################################################################
#                          Experimento liga ternária                          #
#                            algoritmos genéticos                             #
###############################################################################

def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    pass

def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return 

def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    # preencher o código

    return distancia

def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado