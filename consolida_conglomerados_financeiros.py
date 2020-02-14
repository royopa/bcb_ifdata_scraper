import os
import shutil
import pandas as pd
from sqlalchemy import create_engine
from utils import merge_arquivos


conglomerados_financeiros_resumo_relatorios = []
conglomerados_financeiros_segmentacao_relatorios = []
conglomerados_financeiros_ativo_relatorios = []
conglomerados_financeiros_passivo_relatorios = []
conglomerados_financeiros_informacoes_capital_relatorios = []
conglomerados_financeiros_demonstracao_resultado_relatorios = []


# appenda os arquivos baixados em apenas um arquivo
download_folder = os.path.join('downloads', 'conglomerados_financeiros')

for file_name in sorted(os.listdir(download_folder)):
    file_path = os.path.join(download_folder, file_name)
        
    if not file_path.endswith('.csv'):
        continue

    if 'resumo' in file_name:
        conglomerados_financeiros_resumo_relatorios.append(file_path)        
        
    if 'ativo' in file_name:
        conglomerados_financeiros_ativo_relatorios.append(file_path)        
        
    if 'passivo' in file_name:
        conglomerados_financeiros_passivo_relatorios.append(file_path)

    if 'demonstracao_de_resultado' in file_name:
        conglomerados_financeiros_demonstracao_resultado_relatorios.append(file_path)
        
    data_base = file_name[:7]
    ano = file_name.split('_')[0]
    trimestre = file_name.split('_')[1]
    relatorio = file_name.split('_')[3]
    restante_arquivo = file_name[7:]
    
    #print(ano, trimestre, relatorio, restante_arquivo)


merge_arquivos(
    conglomerados_financeiros_resumo_relatorios,
    'congl_financeiros_resumo.csv'
)

merge_arquivos(
    conglomerados_financeiros_ativo_relatorios,
    'congl_financeiros_ativo.csv'
)

merge_arquivos(
    conglomerados_financeiros_passivo_relatorios,
    'congl_financeiros_passivo.csv'
)

merge_arquivos(
    conglomerados_financeiros_demonstracao_resultado_relatorios,
    'congl_financeiros_demonstracao_resultado.csv'
)
