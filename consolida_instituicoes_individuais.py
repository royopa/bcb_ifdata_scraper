import os
from utils import merge_arquivos


download_folder = os.path.join('downloads', 'instituicoes_individuais')


instituicoes_individuais_resumo_relatorios = []
instituicoes_individuais_segmentacao_relatorios = []
instituicoes_individuais_ativo_relatorios = []
instituicoes_individuais_passivo_relatorios = []
instituicoes_individuais_informacoes_capital_relatorios = []
instituicoes_individuais_demonstracao_resultado_relatorios = []


for file_name in sorted(os.listdir(download_folder)):
    file_path = os.path.join(download_folder, file_name)

    if not file_path.endswith('.csv'):
        continue

    if 'resumo' in file_name:
        instituicoes_individuais_resumo_relatorios.append(file_path)

    if 'ativo' in file_name:
        instituicoes_individuais_ativo_relatorios.append(file_path)

    if 'passivo' in file_name:
        instituicoes_individuais_passivo_relatorios.append(file_path)

    if 'demonstracao_de_resultado' in file_name:
        instituicoes_individuais_demonstracao_resultado_relatorios.append(
            file_path)




# relatórios
merge_arquivos(
    instituicoes_individuais_resumo_relatorios,
    'inst_individuais_resumo.csv'
)

merge_arquivos(
    instituicoes_individuais_ativo_relatorios,
    'inst_individuais_ativo.csv'
)

merge_arquivos(
    instituicoes_individuais_passivo_relatorios,
    'inst_individuais_passivo.csv'
)

merge_arquivos(
    instituicoes_individuais_demonstracao_resultado_relatorios,
    'inst_individuais_demonstracao_resultado.csv'
)
