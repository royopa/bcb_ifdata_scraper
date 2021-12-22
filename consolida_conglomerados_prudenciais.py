import os
from utils import get_prud, merge_arquivos
from utils import prepare_bases_folder

download_folder = os.path.join('downloads', 'conglomerados_prudenciais')

prud_resumo_relatorios, prud_segmentacao_relatorios, prud_ativo_relatorios, prud_passivo_relatorios, prud_informacoes_capital_relatorios, prud_demonstracao_resultado_relatorios = get_prud(
    download_folder
)


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
