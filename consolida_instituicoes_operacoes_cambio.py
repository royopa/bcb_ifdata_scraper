import os
from utils import merge_arquivos

download_folder = os.path.join('downloads', 'instituicoes_operacoes_cambio')


instituicoes_operacoes_cambio_resumo_relatorios = []

for file_name in sorted(os.listdir(download_folder)):
    file_path = os.path.join(download_folder, file_name)

    if not file_path.endswith('.csv'):
        continue

    if 'movimentacao_cambio' in file_name:
        instituicoes_operacoes_cambio_resumo_relatorios.append(file_path)




# relatórios
merge_arquivos(
    instituicoes_operacoes_cambio_resumo_relatorios,
    'inst_op_cambio_mov_trimestre.csv'
)
