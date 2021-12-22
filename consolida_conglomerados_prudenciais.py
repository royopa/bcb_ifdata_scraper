import os
from utils import merge_arquivos
from utils import prepare_bases_folder

download_folder = os.path.join('downloads', 'conglomerados_prudenciais')

prud_resumo_relatorios = []
prud_segmentacao_relatorios = []
prud_ativo_relatorios = []
prud_passivo_relatorios = []
prud_informacoes_capital_relatorios = []
prud_demonstracao_resultado_relatorios = []


for file_name in sorted(os.listdir(download_folder)):
    file_path = os.path.join(download_folder, file_name)

    if not file_path.endswith('.csv'):
        continue

    if 'segmentacao' in file_name:
        prud_segmentacao_relatorios.append(file_path)

    if 'resumo' in file_name:
        prud_resumo_relatorios.append(file_path)

    if 'ativo' in file_name:
        prud_ativo_relatorios.append(file_path)

    if 'passivo' in file_name:
        prud_passivo_relatorios.append(file_path)

    if 'informacoes_de_capital' in file_name:
        prud_informacoes_capital_relatorios.append(file_path)

    if 'demonstracao_de_resultado' in file_name:
        prud_demonstracao_resultado_relatorios.append(file_path)

    data_base = file_name[:7]
    ano = file_name.split('_')[0]
    trimestre = file_name.split('_')[1]
    relatorio = file_name.split('_')[3]
    restante_arquivo = file_name[7:]


# relatórios
prepare_bases_folder()

merge_arquivos(
    prud_resumo_relatorios,
    'prud_resumo.csv'
)

merge_arquivos(
    prud_segmentacao_relatorios,
    'prud_segmentacao.csv'
)

merge_arquivos(
    prud_ativo_relatorios,
    'prud_ativo.csv'
)

merge_arquivos(
    prud_passivo_relatorios,
    'prud_passivo.csv'
)

merge_arquivos(
    prud_informacoes_capital_relatorios,
    'prud_informacoes_capital.csv'
)

merge_arquivos(
    prud_demonstracao_resultado_relatorios,
    'prud_demonstracao_resultado.csv'
)
