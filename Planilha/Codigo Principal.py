import pandas as pd
import openpyxl
from Planilha import Modulos_excell as me
from operator import itemgetter
planilha = pd.read_excel(r"C:\Users\tesse\Downloads\Vendas Loja.xlsx", sheet_name='Testepy')
# lista_marcas = me.conta_marca(planilha)
# top = me.top_marcas(planilha, lista_marcas, True)
#
# preco_cabuloso_thermo = me.localiza_preco(caminho_ate_planilha=r"C:\Users\tesse\Downloads\Vendas Loja.xlsx", nome_marca='B2R')


for indice, marca in enumerate(planilha["MARCA"]):
    produto = planilha["PRODUTO"][indice]
    preco = me.pega_preco(r"C:\Users\tesse\Downloads\Vendas Loja.xlsx", nome_marca=marca, nome_produto=produto)
    print(f'O Produto {produto} tem o valor R${preco}')

