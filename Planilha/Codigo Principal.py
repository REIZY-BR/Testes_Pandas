import pandas as pd
import openpyxl
from Planilha import Modulos_excell as me
from operator import itemgetter
# planilha = pd.read_excel(r"C:\Users\tesse\Downloads\Vendas Loja.xlsx", sheet_name='Fevereiro22')
# lista_marcas = me.conta_marca(planilha)
# top = me.top_marcas(planilha, lista_marcas, True)

preco_cabuloso_thermo = me.localiza_preco(caminho_ate_planilha=r"C:\Users\tesse\Downloads\Vendas Loja.xlsx", nome_marca='B2R')
