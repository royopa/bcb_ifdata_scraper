import os
from utils import get_cong, merge_cong_files

download_folder = os.path.join('downloads', 'conglomerados_financeiros')

conglomerados_financeiros_resumo_relatorios, conglomerados_financeiros_ativo_relatorios,\
    conglomerados_financeiros_passivo_relatorios, conglomerados_financeiros_demonstracao_resultado_relatorios = get_cong(
        download_folder
    )

merge_cong_files(
    conglomerados_financeiros_resumo_relatorios,
    conglomerados_financeiros_ativo_relatorios,
    conglomerados_financeiros_passivo_relatorios,
    conglomerados_financeiros_demonstracao_resultado_relatorios
)
