import pandas as pd


def marca(planilha, nome_marca):
    """
    :param planilha: banco de dados para ser analisado
    :param nome_marca: nome da marca escolhida
    :return: banco de dados referente ao nome_marca
    """
    import pandas as pd
    banco_dados = planilha.loc[planilha["MARCA"] == nome_marca]
    return banco_dados


def conta_marca(planilha):
    """
    :param planilha: banco de dados a ser analisado
    :return: uma lista com todas as marcas disponivel no banco de dados sem possiveis duplicatas
    """
    lista = list()
    for nome in planilha["MARCA"]:
        if nome not in lista:
            lista.append(nome)
    return lista


def top_marcas(planilha, lista_de_marcas, show=False):
    """
    :param planilha: Banco de dados a ser analisado
    :param lista_de_marcas: lista de marcas para analisar
    :param show: mostrar o banco de dados formatado em ordem decrescente levando em consideração a quantidade
    vendida
    :return: um dicionario formatado e organizado com as marcas selecionadas
    """
    # criando uma lista com varias listas dentro contendo o nome da marca e quantidade vendida
    dicionario = dict()
    for marca in lista_de_marcas:
        contador = 0
        for linha, nome in enumerate(planilha["MARCA"]):
            if nome == marca:
                contador += int(planilha["QTD"][linha])
        dicionario[marca] = contador
    # organizando o dicionario pela quantidade vendida
    from typing import Dict, Any
    new_dicionario: dict[Any, int] = dict()
    for i in sorted(dicionario, key=dicionario.get, reverse=True):
        new_dicionario[i] = dicionario[i]
    # mostrando o dicionario formatado
    if show:
        for chave, item in new_dicionario.items():
            print(f'|{chave:<20} = {item:>10}|')
    return new_dicionario


def localiza_preco(caminho_ate_planilha, nome_marca):
    """
    :param caminho_ate_planilha: local onde o arquivo esta localizado
    :param nome_marca: nome da marca a ser analisada(precisa ter uma plhanilha com o nome da marca salva)
    :return: o valor selecionado pelo usuario(permite guardar em uma variavel)
    """
    # Criando um banco de dados com o nome dos produtos
    banco_dados = pd.read_excel(rf'{caminho_ate_planilha}', sheet_name=nome_marca)
    # Mostrando os produtos com indices a ser escolhido
    print('-' * 40)
    for pos, produto in enumerate(banco_dados["PRODUTOS"]):
        print(f'|{pos}{produto:^40}{pos}|')
        print('-' * 40)
    # perguntando ao usuario qual produto deseja ver o preço
    while True:
        try:
            while True:
                posicao_produto = int(input('Qual produto deseja vizualizar o preço?'))
                if 0 < posicao_produto <= len(banco_dados["PRODUTOS"]) - 1:
                    break
                else:
                    print(f'ERRO, digite um número entre 0 e {len(banco_dados["PRODUTOS"]) - 1}!')
        except KeyboardInterrupt:
            print('\n\033[31mO usuario interrompeu o programa!\033[m ' * 6)
        except:
            print(f'ERRO, digite um número entre 0 e {len(banco_dados["PRODUTOS"]) - 1}!')
        else:
            break
    # apos achar o preço com o produto selecionado, printamos...
    preco = float(banco_dados["PRECOS"][posicao_produto])
    print(f'O preço do produto {banco_dados["PRODUTOS"][posicao_produto]} = R${preco:.2f}')
    return preco


def pega_preco(planilha, nome_marca, nome_produto):
    """
    :param planilha: Planilha ja carregada com todas as tabelas presentes
    :param nome_marca: Nome da marca do produto, é necessario um sheet=Nome da marca
    :param nome_produto: Nome do produto da marca selecionada
    :return: Uma mensagem de erro caso nao for encontrado ou o preço em float
    """
    # criando um banco de dados com base em um sheet dentro da planilha com o nome da marca
    banco_dados = pd.read_excel(planilha, sheet_name=nome_marca)
    # localizando o preço pelo nome do produto com um for e if comparativo
    linha = banco_dados.loc[banco_dados["PRODUTOS"] == nome_produto]
    preco = linha["PRECOS"]
    try:
        preco = float(preco)
    except:
        print(f'\033[31mHouve um erro na busca do produto {nome_produto}!\033[m')
        preco = None
    return preco
