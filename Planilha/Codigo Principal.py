import pandas as pd
# import openpyxl
from Planilha import Modulos_excell as me
# from operator import itemgetter
planilha_original = pd.ExcelFile(r"C:\Users\tesse\Downloads\Vendas Loja.xlsx")
planilha_testepy = pd.read_excel(planilha_original, sheet_name='Testepy')
# # lista_marcas = me.conta_marca(planilha)
# # top = me.top_marcas(planilha, lista_marcas, True)
# #
# # preco_cabuloso_thermo = me.localiza_preco(caminho_ate_planilha=r"C:\Users\tesse\Downloads\Vendas Loja.xlsx", nome_marca='B2R')
#
#
# for indice, marca in enumerate(planilha["MARCA"]):
#     produto = planilha["PRODUTO"][indice]
#     preco = me.pega_preco(r"C:\Users\tesse\Downloads\Vendas Loja.xlsx", nome_marca=str(marca), nome_produto=produto)
#     print(f'O Produto {produto} tem o valor R${preco}')


for indice, linha in planilha_testepy.iterrows():
    marca = linha["MARCA"]
    produto = linha["PRODUTO"]
    qtd = linha["QTD"]
    preco = me.pega_preco(planilha_original, marca, produto)
    print(f'O produto {produto}, {marca} tem o valor {preco}')