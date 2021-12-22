import os
from dotenv import find_dotenv
from dotenv import load_dotenv
from utils import processa_import
from utils import prepare_bases_folder
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
        conglomerados_financeiros_demonstracao_resultado_relatorios.append(
            file_path)

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

    data_base = file_name[:7]
    ano = file_name.split('_')[0]
    trimestre = file_name.split('_')[1]
    relatorio = file_name.split('_')[3]
    restante_arquivo = file_name[7:]

    #print(ano, trimestre, relatorio, restante_arquivo)


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


load_dotenv(find_dotenv())

nome_relatorio = 'congl_financeiros_ativo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 15',
    'Unnamed: 20',
    'Unnamed: 21',
    'Unnamed: 26',
    'Unnamed: 28'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Disponibilidades (a)': 'disponibilidades',
    'Aplicações Interfinanceiras de Liquidez (b)': 'aplicacoes_interfinanceiras_liquidez',
    'TVM e Instrumentos Financeiros Derivativos (c)': 'tvm_derivativos',
    'Operações de Crédito': 'operacoes_credito',
    'Unnamed: 13': 'provisao_operacoes_credito',
    'Unnamed: 14': 'operacoes_credito_liquidas_provisao',
    'Arrendamento Mercantil': 'arrendamento_mercantil_receber',
    'Unnamed: 16': 'imobilizado_de_arrendamento',
    'Unnamed: 17': 'credores_antecipacao_valor_residual',
    'Unnamed: 18': 'provisao_sobre_arrendamento_mercantil',
    'Unnamed: 19': 'arrendamento_mercantil_liquido_provisao',
    'Outros Créditos - Líquido de Provisão (f)': 'outros_creditos_liquidos_provisao',
    'Outros Ativos Realizáveis (g)': 'outros_ativos_realizaveis',
    'Permanente Ajustado (h)': 'permanente_ajustado',
    'Ativo Total Ajustado (i) = (a) + (b) + (c) + (d) + (e) + (f) + (g) + (h)': 'ativo_total_ajustado',
    'Credores por Antecipação de Valor Residual (j)': 'credores_antecipacao_valor_residual_2',
    'Ativo Total (k) = (i) - (j)': 'ativo_total',
    'Conglomerado': 'conglomerado',
    'Conglomerado Financeiro': 'conglomerado_financeiro',
    'Conglomerado Prudencial': 'conglomerado_prudencial',
    'TI': 'ti'
}
processa_import(nome_relatorio, a_excluir, a_renomear)


nome_relatorio = 'congl_financeiros_resumo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 19',
    'Unnamed: 20'
}


a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Ativo Total': 'ativo_total',
    'Carteira de Crédito Classificada': 'carteira_credito_classificada',
    'Passivo Circulante e Exigível a Longo Prazo e Resultados de Exercícios Futuros': 'passivo_circulante_exigivel_longo_prazo',
    'Captações': 'captacoes',
    'Patrimônio Líquido': 'patrimonio_liquido',
    'Lucro Líquido': 'lucro_liquido',
    'Patrimônio de Referência para Comparação com o RWA': 'patrimonio_referencia',
    'Índice de Basileia': 'ic_basileia',
    'Índice de Imobilização': 'ic_imobilizacao',
    'Número de Agências': 'nu_agencias',
    'Número de Postos de Atendimento': 'nu_postos_atendimento',
    'Conglomerado': 'conglomerado',
    'Conglomerado Financeiro': 'conglomerado_financeiro',
    'Conglomerado Prudencial': 'conglomerado_prudencial',
    'TI': 'ti'
}
processa_import(nome_relatorio, a_excluir, a_renomear)


nome_relatorio = 'congl_financeiros_passivo'
a_excluir = {
    'Unnamed: 0',
    'Unnamed: 24',
    'Unnamed: 25',
    'Unnamed: 32',
    'Unnamed: 30'
}
a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Captações': 'depositos_vista',
    'Unnamed: 10': 'depositos_poupanca',
    'Unnamed: 11': 'depositos_interfinanceiros',
    'Unnamed: 12': 'depositos_prazo',
    'Unnamed: 13': 'outros_depositos',
    'Unnamed: 14': 'deposito_total',
    'Unnamed: 15': 'obrigacoes_operacoes_compromissadas',
    'Unnamed: 16': 'letras_credito_imobiliario',
    'Unnamed: 17': 'letras_credito_agronegocio',
    'Unnamed: 18': 'letras_financeiras',
    'Unnamed: 19': 'obrigacoes_titulos_valores_mobiliarios_exterior',
    'Unnamed: 20': 'outros_recursos_aceites_emissao_titulos',
    'Unnamed: 21': 'recursos_aceites_emissao_titulos',
    'Unnamed: 22': 'obrigacoes_emprestimos_repasses',
    'Unnamed: 23': 'captacoes',
    'Instrumentos Derivativos (f)': 'instrumentos_derivativos',
    'Outras Obrigações (g)': 'outras_obrigacoes',
    'Passivo Circulante e Exigível a Longo Prazo (h) = (e) + (f) + (g)': 'passivo_circulante_exigivel_longo_prazo',
    'Resultados de Exercícios Futuros (i)': 'resultado_exercicios_futuros',
    'Patrimônio Líquido (j)': 'patrimonio_liquido',
    'Passivo Total (k) = (h) + (i) + (j)': 'passivo_total',
    'Conglomerado': 'conglomerado',
    'Conglomerado Financeiro': 'conglomerado_financeiro',
    'Conglomerado Prudencial': 'conglomerado_prudencial',
    'TI': 'ti'
}
processa_import(nome_relatorio, a_excluir, a_renomear)

nome_relatorio = 'congl_financeiros_demonstracao_resultado'
a_excluir = {
    'Unnamed: 0',
    'Unnamed: 23',
    'Unnamed: 32',
    'Unnamed: 33',
    'Unnamed: 39',
    'Unnamed: 41'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Resultado de Intermediação Financeira': 'rendas_op_credito',
    'Unnamed: 10': 'rendas_op_arrendamento_mercantil',
    'Unnamed: 11': 'rendas_op_tvm',
    'Unnamed: 12': 'rendas_op_derivativos',
    'Unnamed: 13': 'rendas_resultado_op_cambio',
    'Unnamed: 14': 'rendas_aplicacoes_compulsorias',
    'Unnamed: 15': 'receitas_intermediacao_financeira',
    'Unnamed: 16': 'despesas_captacao',
    'Unnamed: 17': 'despesas_obrigacoes_emprestimos_repasses',
    'Unnamed: 18': 'despesas_operacoes_arrendamento_mercantil',
    'Unnamed: 19': 'despesas_resultado_op_cambio',
    'Unnamed: 20': 'resultado_provisao_credito_dificil_liquidacao',
    'Unnamed: 21': 'despesas_intermediacao_financeira',
    'Unnamed: 22': 'resultado_intermediacao_financeira',
    'Outras Receitas/Despesas Operacionais': 'rendas_prestacao_servicos',
    'Unnamed: 24': 'rendas_tarifas_bancarias',
    'Unnamed: 25': 'despesas_pessoal',
    'Unnamed: 26': 'despesas_administrativas',
    'Unnamed: 27': 'despesas_tributarias',
    'Unnamed: 28': 'resultado_participacoes',
    'Unnamed: 29': 'outras_receitas_operacionais',
    'Unnamed: 30': 'outras_despesas_operacionais',
    'Unnamed: 31': 'outras_receitas_despesas_operacionais',
    'Resultado Operacional (e) = (c) + (d)': 'resultado_operacional',
    'Resultado Não Operacional (f)': 'resultado_nao_operacional',
    'Resultado antes da Tributação, Lucro e Participação (g) = (e) + (f)': 'resultado_antes_tributacao_lucro_participacao',
    'Imposto de Renda e Contribuição Social (h)': 'imposto_renda_contribuicao_social',
    'Participação nos Lucros (i)': 'participacao_lucros',
    'Lucro Líquido (j) = (g) + (h) + (i)': 'lucro_liquido',
    'Juros Sobre Capital Próprio (k)': 'juros_sobre_capital_proprio',
    'Juros Sobre Capital Social de Cooperativas (k)': 'juros_sobre_capital_cooperativas',
    'Conglomerado': 'conglomerado',
    'Conglomerado Financeiro': 'conglomerado_financeiro',
    'Conglomerado Prudencial': 'conglomerado_prudencial',
    'TI': 'ti'
}

processa_import(nome_relatorio, a_excluir, a_renomear)


load_dotenv(find_dotenv())

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'), echo=False)

nome_relatorio = 'prud_resumo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 20',
    'Unnamed: 17'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Ativo Total': 'ativo_total',
    'Carteira de Crédito Classificada': 'carteira_credito_classificada',
    'Passivo Circulante e Exigível a Longo Prazo e Resultados de Exercícios Futuros': 'passivo_circulante_exigivel_longo_prazo',
    'Captações': 'captacoes',
    'Patrimônio Líquido': 'patrimonio_liquido',
    'Lucro Líquido': 'lucro_liquido',
    'Patrimônio de Referência para Comparação com o RWA': 'patrimonio_referencia',
    'Índice de Basileia': 'ic_basileia',
    'Índice de Imobilização': 'ic_imobilizacao',
    'Número de Agências': 'nu_agencias',
    'Número de Postos de Atendimento': 'nu_postos_atendimento',
}

processa_import(nome_relatorio, a_excluir, a_renomear)

nome_relatorio = 'prud_ativo'
a_excluir = {
    'Unnamed: 0',
    'Unnamed: 26'
}


a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Disponibilidades (a)': 'disponibilidades',
    'Aplicações Interfinanceiras de Liquidez (b)': 'aplicacoes_interfinanceiras_liquidez',
    'TVM e Instrumentos Financeiros Derivativos (c)': 'tvm_derivativos',
    'Operações de Crédito': 'operacoes_credito',
    'Unnamed: 13': 'provisao_operacoes_credito',
    'Unnamed: 14': 'operacoes_credito_liquidas_provisao',
    'Arrendamento Mercantil': 'arrendamento_mercantil_receber',
    'Unnamed: 16': 'imobilizado_de_arrendamento',
    'Unnamed: 17': 'credores_antecipacao_valor_residual',
    'Unnamed: 18': 'provisao_sobre_arrendamento_mercantil',
    'Unnamed: 19': 'arrendamento_mercantil_liquido_provisao',
    'Outros Créditos - Líquido de Provisão (f)': 'outros_creditos_liquidos_provisao',
    'Outros Ativos Realizáveis (g)': 'outros_ativos_realizaveis',
    'Permanente Ajustado (h)': 'permanente_ajustado',
    'Ativo Total Ajustado (i) = (a) + (b) + (c) + (d) + (e) + (f) + (g) + (h)': 'ativo_total_ajustado',
    'Credores por Antecipação de Valor Residual (j)': 'credores_antecipacao_valor_residual_2',
    'Ativo Total (k) = (i) - (j)': 'ativo_total'
}
processa_import(nome_relatorio, a_excluir, a_renomear)


nome_relatorio = 'prud_passivo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 30'
}


a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Captações': 'depositos_vista',
    'Unnamed: 10': 'depositos_poupanca',
    'Unnamed: 11': 'depositos_interfinanceiros',
    'Unnamed: 12': 'depositos_prazo',
    'Unnamed: 13': 'outros_depositos',
    'Unnamed: 14': 'deposito_total',
    'Unnamed: 15': 'obrigacoes_operacoes_compromissadas',
    'Unnamed: 16': 'letras_credito_imobiliario',
    'Unnamed: 17': 'letras_credito_agronegocio',
    'Unnamed: 18': 'letras_financeiras',
    'Unnamed: 19': 'obrigacoes_titulos_valores_mobiliarios_exterior',
    'Unnamed: 20': 'outros_recursos_aceites_emissao_titulos',
    'Unnamed: 21': 'recursos_aceites_emissao_titulos',
    'Unnamed: 22': 'obrigacoes_emprestimos_repasses',
    'Unnamed: 23': 'captacoes',
    'Instrumentos Derivativos (f)': 'instrumentos_derivativos',
    'Outras Obrigações (g)': 'outras_obrigacoes',
    'Passivo Circulante e Exigível a Longo Prazo (h) = (e) + (f) + (g)': 'passivo_circulante_exigivel_longo_prazo',
    'Resultados de Exercícios Futuros (i)': 'resultado_exercicios_futuros',
    'Patrimônio Líquido (j)': 'patrimonio_liquido',
    'Passivo Total (k) = (h) + (i) + (j)': 'passivo_total'
}
processa_import(nome_relatorio, a_excluir, a_renomear)


nome_relatorio = 'prud_informacoes_capital'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 28'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Patrimônio de Referência para Comparação com o RWA': 'capital_principal',
    'Unnamed: 10': 'capital_complementar',
    'Unnamed: 11': 'patrimonio_referencia_nivel_1',
    'Unnamed: 12': 'capital_nivel_2',
    'Unnamed: 13': 'patrimonio_referencia',
    'Ativos Ponderados pelo Risco (RWA)': 'rwa_risco_credito',
    'Unnamed: 15': 'rwa_cam',
    'Unnamed: 16': 'rwa_com',
    'Unnamed: 17': 'rwa_jur',
    'Unnamed: 18': 'rwa_acs',
    'Unnamed: 19': 'rwa_risco_mercado',
    'Unnamed: 20': 'rwa_risco_operacional',
    'Unnamed: 21': 'rwa_ativos_ponderados_risco',
    'Exposição Total (j)': 'exposicao_total',
    'Índice de Capital Principal (k) = (a) / (i)': 'ic_capital_principal',
    'Índice de Capital Nível I (l) = (c) / (i)': 'ic_capital_nivel_1',
    'Índice de Basileia (m) = (e) / (i)': 'ic_basileia',
    'Razão de Alavancagem (n) = (c) / (j)': 'razao_alavancagem',
    'Índice de Imobilização (o)': 'ic_imobilizacao',
}
processa_import(nome_relatorio, a_excluir, a_renomear)


nome_relatorio = 'prud_demonstracao_resultado'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 39'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Resultado de Intermediação Financeira': 'rendas_op_credito',
    'Unnamed: 10': 'rendas_op_arrendamento_mercantil',
    'Unnamed: 11': 'rendas_op_tvm',
    'Unnamed: 12': 'rendas_op_derivativos',
    'Unnamed: 13': 'rendas_resultado_op_cambio',
    'Unnamed: 14': 'rendas_aplicacoes_compulsorias',
    'Unnamed: 15': 'receitas_intermediacao_financeira',
    'Unnamed: 16': 'despesas_captacao',
    'Unnamed: 17': 'despesas_obrigacoes_emprestimos_repasses',
    'Unnamed: 18': 'despesas_operacoes_arrendamento_mercantil',
    'Unnamed: 19': 'despesas_resultado_op_cambio',
    'Unnamed: 20': 'resultado_provisao_credito_dificil_liquidacao',
    'Unnamed: 21': 'despesas_intermediacao_financeira',
    'Unnamed: 22': 'resultado_intermediacao_financeira',
    'Outras Receitas/Despesas Operacionais': 'rendas_prestacao_servicos',
    'Unnamed: 24': 'rendas_tarifas_bancarias',
    'Unnamed: 25': 'despesas_pessoal',
    'Unnamed: 26': 'despesas_administrativas',
    'Unnamed: 27': 'despesas_tributarias',
    'Unnamed: 28': 'resultado_participacoes',
    'Unnamed: 29': 'outras_receitas_operacionais',
    'Unnamed: 30': 'outras_despesas_operacionais',
    'Unnamed: 31': 'outras_receitas_despesas_operacionais',
    'Resultado Operacional (e) = (c) + (d)': 'resultado_operacional',
    'Resultado Não Operacional (f)': 'resultado_nao_operacional',
    'Resultado antes da Tributação, Lucro e Participação (g) = (e) + (f)': 'resultado_antes_tributacao_lucro_participacao',
    'Imposto de Renda e Contribuição Social (h)': 'imposto_renda_contribuicao_social',
    'Participação nos Lucros (i)': 'participacao_lucros',
    'Lucro Líquido (j) = (g) + (h) + (i)': 'lucro_liquido',
    'Juros Sobre Capital Próprio (k)': 'juros_sobre_capital_proprio',
    'Juros Sobre Capital Social de Cooperativas (k)': 'juros_sobre_capital_cooperativas'
}
processa_import(nome_relatorio, a_excluir, a_renomear)


nome_relatorio = 'prud_segmentacao'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 15'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Instituição Sujeita à Apuração da Exposição Total': 'ic_apuracao_exposicao_total',
    'Instituição Sujeita à Apuração do Patrimônio de Referência': 'ic_apuracao_patrimonio_referencia',
    'Instituição Utiliza Metodologia Simplificada': 'ic_metodologia_simplificada',
    'Exposição Total ou Ativo Total (R$ mil)': 'exposicao_total',
    'Total de Ativos Consolidados no Exterior (US$ mil)': 'total_ativos_consolidado_exterior',
    'Data da Última Alteração de Segmento': 'dt_ultima_alteracao_segmento'
}
processa_import(nome_relatorio, a_excluir, a_renomear)


load_dotenv(find_dotenv())


nome_relatorio = 'inst_individuais_demonstracao_resultado'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 41'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Resultado de Intermediação Financeira': 'rendas_op_credito',
    'Unnamed: 12': 'rendas_op_arrendamento_mercantil',
    'Unnamed: 13': 'rendas_op_tvm',
    'Unnamed: 14': 'rendas_op_derivativos',
    'Unnamed: 15': 'rendas_resultado_op_cambio',
    'Unnamed: 16': 'rendas_aplicacoes_compulsorias',
    'Unnamed: 17': 'receitas_intermediacao_financeira',
    'Unnamed: 18': 'despesas_captacao',
    'Unnamed: 19': 'despesas_obrigacoes_emprestimos_repasses',
    'Unnamed: 20': 'despesas_operacoes_arrendamento_mercantil',
    'Unnamed: 21': 'despesas_resultado_op_cambio',
    'Unnamed: 22': 'resultado_provisao_credito_dificil_liquidacao',
    'Unnamed: 23': 'despesas_intermediacao_financeira',
    'Unnamed: 24': 'resultado_intermediacao_financeira',
    'Outras Receitas/Despesas Operacionais': 'rendas_prestacao_servicos',
    'Unnamed: 26': 'rendas_tarifas_bancarias',
    'Unnamed: 27': 'despesas_pessoal',
    'Unnamed: 28': 'despesas_administrativas',
    'Unnamed: 29': 'despesas_tributarias',
    'Unnamed: 30': 'resultado_participacoes',
    'Unnamed: 31': 'outras_receitas_operacionais',
    'Unnamed: 32': 'outras_despesas_operacionais',
    'Unnamed: 33': 'outras_receitas_despesas_operacionais',
    'Resultado Operacional (e) = (c) + (d)': 'resultado_operacional',
    'Resultado Não Operacional (f)': 'resultado_nao_operacional',
    'Resultado antes da Tributação, Lucro e Participação (g) = (e) + (f)': 'resultado_antes_tributacao_lucro_participacao',
    'Imposto de Renda e Contribuição Social (h)': 'imposto_renda_contribuicao_social',
    'Participação nos Lucros (i)': 'participacao_lucros',
    'Lucro Líquido (j) = (g) + (h) + (i)': 'lucro_liquido',
    'Juros Sobre Capital Próprio (k)': 'juros_sobre_capital_proprio',
    'Juros Sobre Capital Social de Cooperativas (k)': 'juros_sobre_capital_cooperativas',
    'Conglomerado': 'conglomerado',
    'Conglomerado Financeiro': 'conglomerado_financeiro',
    'Conglomerado Prudencial': 'conglomerado_prudencial',
    'TI': 'ti'
}
processa_import(nome_relatorio, a_excluir, a_renomear)


nome_relatorio = 'inst_individuais_resumo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 19'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Ativo Total': 'ativo_total',
    'Carteira de Crédito Classificada': 'carteira_credito_classificada',
    'Passivo Circulante e Exigível a Longo Prazo e Resultados de Exercícios Futuros': 'passivo_circulante_exigivel_longo_prazo',
    'Captações': 'captacoes',
    'Patrimônio Líquido': 'patrimonio_liquido',
    'Lucro Líquido': 'lucro_liquido',
    'Número de Agências': 'nu_agencias',
    'Número de Postos de Atendimento': 'nu_postos_atendimento',
    'Conglomerado': 'conglomerado',
    'Conglomerado Financeiro': 'conglomerado_financeiro',
    'Conglomerado Prudencial': 'conglomerado_prudencial',
    'TI': 'ti'
}

processa_import(nome_relatorio, a_excluir, a_renomear)

nome_relatorio = 'inst_individuais_ativo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 28'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Disponibilidades (a)': 'disponibilidades',
    'Aplicações Interfinanceiras de Liquidez (b)': 'aplicacoes_interfinanceiras_liquidez',
    'TVM e Instrumentos Financeiros Derivativos (c)': 'tvm_derivativos',
    'Operações de Crédito': 'operacoes_credito',
    'Unnamed: 15': 'provisao_operacoes_credito',
    'Unnamed: 16': 'operacoes_credito_liquidas_provisao',
    'Arrendamento Mercantil': 'arrendamento_mercantil_receber',
    'Unnamed: 18': 'imobilizado_de_arrendamento',
    'Unnamed: 19': 'credores_antecipacao_valor_residual',
    'Unnamed: 20': 'provisao_sobre_arrendamento_mercantil',
    'Unnamed: 21': 'arrendamento_mercantil_liquido_provisao',
    'Outros Créditos - Líquido de Provisão (f)': 'outros_creditos_liquidos_provisao',
    'Outros Ativos Realizáveis (g)': 'outros_ativos_realizaveis',
    'Permanente Ajustado (h)': 'permanente_ajustado',
    'Ativo Total Ajustado (i) = (a) + (b) + (c) + (d) + (e) + (f) + (g) + (h)': 'ativo_total_ajustado',
    'Credores por Antecipação de Valor Residual (j)': 'credores_antecipacao_valor_residual_2',
    'Ativo Total (k) = (i) - (j)': 'ativo_total',
    'Conglomerado': 'conglomerado',
    'Conglomerado Financeiro': 'conglomerado_financeiro',
    'Conglomerado Prudencial': 'conglomerado_prudencial',
    'TI': 'ti'
}

processa_import(nome_relatorio, a_excluir, a_renomear)

nome_relatorio = 'inst_individuais_passivo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 32'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'SR': 'segmento',
    'TD': 'tp_consolidacao',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Captações': 'depositos_vista',
    'Unnamed: 12': 'depositos_poupanca',
    'Unnamed: 13': 'depositos_interfinanceiros',
    'Unnamed: 14': 'depositos_prazo',
    'Unnamed: 15': 'outros_depositos',
    'Unnamed: 16': 'deposito_total',
    'Unnamed: 17': 'obrigacoes_operacoes_compromissadas',
    'Unnamed: 18': 'letras_credito_imobiliario',
    'Unnamed: 19': 'letras_credito_agronegocio',
    'Unnamed: 20': 'letras_financeiras',
    'Unnamed: 21': 'obrigacoes_titulos_valores_mobiliarios_exterior',
    'Unnamed: 22': 'outros_recursos_aceites_emissao_titulos',
    'Unnamed: 23': 'recursos_aceites_emissao_titulos',
    'Unnamed: 24': 'obrigacoes_emprestimos_repasses',
    'Unnamed: 25': 'captacoes',
    'Instrumentos Derivativos (f)': 'instrumentos_derivativos',
    'Outras Obrigações (g)': 'outras_obrigacoes',
    'Passivo Circulante e Exigível a Longo Prazo (h) = (e) + (f) + (g)': 'passivo_circulante_exigivel_longo_prazo',
    'Resultados de Exercícios Futuros (i)': 'resultado_exercicios_futuros',
    'Patrimônio Líquido (j)': 'patrimonio_liquido',
    'Passivo Total (k) = (h) + (i) + (j)': 'passivo_total',
    'Conglomerado': 'conglomerado',
    'Conglomerado Financeiro': 'conglomerado_financeiro',
    'Conglomerado Prudencial': 'conglomerado_prudencial',
    'TI': 'ti'
}
processa_import(nome_relatorio, a_excluir, a_renomear)


load_dotenv(find_dotenv())


nome_relatorio = 'inst_op_cambio_mov_trimestre'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 31'
}

a_renomear = {
    'Instituição financeira': 'nome_if',
    'Código': 'co_if',
    'TCB': 'tp_consolidado_bancario',
    'Segmento': 'segmento',
    'TD': 'tp_consolidacao',
    'SR': 'segmento',
    'TC': 'tp_controle',
    'Cidade': 'cidade',
    'UF': 'uf',
    'Data': 'dt_base',
    'Exportações': 'export_nu_operacoes',
    'Unnamed: 10': 'export_valor',
    'Importações': 'import_nu_operacoes',
    'Unnamed: 12': 'import_valor',
    'Total Primário Comercial': 'total_prim_comercial_nu_operacoes',
    'Unnamed: 14': 'total_prim_comercial_valor',
    'Transferências do Exterior': 'transf_do_exterior_nu_operacoes',
    'Unnamed: 16': 'transf_do_exterior_valor',
    'Transferências para o Exterior': 'transf_para_exterior_nu_operacoes',
    'Unnamed: 18': 'transf_para_exterior_valor',
    'Total Primário Financeiro': 'total_prim_financeiro_nu_operacoes',
    'Unnamed: 20': 'total_prim_financeiro_valor',
    'Total Primário': 'total_prim_nu_operacoes',
    'Unnamed: 22': 'total_prim_valor',
    'Interbancário Compra': 'interb_compra_nu_operacoes',
    'Unnamed: 24': 'interb_compra_valor',
    'Interbancário Venda': 'interb_venda_nu_operacoes',
    'Unnamed: 26': 'interb_venda_valr',
    'Total Interbancário': 'total_interb_nu_operacoes',
    'Unnamed: 28': 'total_interb_nu_valor',
    'Total': 'total_nu_operacoes',
    'Unnamed: 30': 'total_valor'
}

processa_import(nome_relatorio, a_excluir, a_renomear)
