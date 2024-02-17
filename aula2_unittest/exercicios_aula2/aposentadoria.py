'''
função: verificar_qualificacao_empregado()
entrada: idade e tempo_de_servico
saída: 'Requerer aposentadoria' ou 'Não requerer'

Critérios para verificar se o funcionário está 
qualificado para aposentadoria:
 - Ter no mínimo 65 anos de idade.
 - Ter trabalhado no mínimo 30 anos.
 - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos. 

Restrição: os parâmetros de entrada, idade e tempo_de_servico, devem, necessariamente, ser números inteiros e maiores que zero.

'''
REQUERER = 'Requerer aposentadoria'
NAO_REQUERER = 'Não requerer'

def verificar_qualificacao_empregado(idade, tempo_de_servico):
    if idade == 0 or tempo_de_servico == 0:
        raise ValueError
    if type(idade) != int or type(tempo_de_servico) != int:
        raise TypeError 

    if idade >= 65:
        return REQUERER
    elif tempo_de_servico >= 30:
        return REQUERER
    elif idade >= 60 and tempo_de_servico >= 25:
        return REQUERER
    return NAO_REQUERER