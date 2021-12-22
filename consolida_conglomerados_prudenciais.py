import os
from utils import get_prud, merge_arquivos, merge_files
from utils import prepare_bases_folder

download_folder = os.path.join('downloads', 'conglomerados_prudenciais')

prud_resumo_relatorios, prud_segmentacao_relatorios, prud_ativo_relatorios, prud_passivo_relatorios, prud_informacoes_capital_relatorios, prud_demonstracao_resultado_relatorios = get_prud(
    download_folder
)

merge_files(
    prud_resumo_relatorios,
    prud_segmentacao_relatorios,
    prud_ativo_relatorios,
    prud_passivo_relatorios,
    prud_informacoes_capital_relatorios,
    prud_demonstracao_resultado_relatorios
)
