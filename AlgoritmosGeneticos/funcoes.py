def funcao_objetivo_cb(individuo):
    """ computa a função objetivo no problema das caixas binárias.
    
    Args: 
        Individuo: lista contendo os genes das caixas binárias

    Return:
        Um valor representando a soma dos genes dos indivíduos.
    """
    return sum(individuo)
