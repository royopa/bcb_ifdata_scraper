import os
import shutil
import pandas as pd
from utils import merge_arquivos

download_folder = os.path.join('downloads', 'instituicoes_operacoes_cambio')


instituicoes_operacoes_cambio_resumo_relatorios = []

for file_name in sorted(os.listdir(download_folder)):
    file_path = os.path.join(download_folder, file_name)
        
    if not file_path.endswith('.csv'):
        continue

    if 'movimentacao_cambio' in file_name:
        instituicoes_operacoes_cambio_resumo_relatorios.append(file_path)        
        
    data_base = file_name[:7]
    ano = file_name.split('_')[0]
    trimestre = file_name.split('_')[1]
    relatorio = file_name.split('_')[3]
    restante_arquivo = file_name[7:]
    
    #print(ano, trimestre, relatorio, restante_arquivo)


# relatórios
merge_arquivos(
    instituicoes_operacoes_cambio_resumo_relatorios,
    'inst_op_cambio_mov_trimestre.csv'
)
