import random 


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
    

def funcao_objetivo_cb(individuo):
    """ computa a função objetivo no problema das caixas binárias.
    
    Args: 
        Individuo: lista contendo os genes das caixas binárias

    Return:
        Um valor representando a soma dos genes dos indivíduos.
    """
    return sum(individuo) + 1

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

