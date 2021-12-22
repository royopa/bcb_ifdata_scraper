import os
from utils import get_instituicoes, merge_arquivos


download_folder = os.path.join('downloads', 'instituicoes_individuais')

instituicoes_individuais_resumo_relatorios, instituicoes_individuais_ativo_relatorios, \
    instituicoes_individuais_passivo_relatorios, instituicoes_individuais_demonstracao_resultado_relatorios = get_instituicoes(
        download_folder
    )


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
