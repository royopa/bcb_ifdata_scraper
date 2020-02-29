import os
import shutil
import pandas as pd
from sqlalchemy import create_engine
from utils import processa_import

from dotenv import load_dotenv
from dotenv import find_dotenv
load_dotenv(find_dotenv())


nome_relatorio = 'inst_individuais_demonstracao_resultado'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 41'
}

a_renomear = {
    'Instituição financeira':'nome_if',
    'Código':'co_if',
    'TCB':'tp_consolidado_bancario',
    'SR':'segmento',
    'TD':'tp_consolidacao',
    'TC':'tp_controle',
    'Cidade':'cidade',
    'UF':'uf',
    'Data':'dt_base',
    'Resultado de Intermediação Financeira':'rendas_op_credito',
    'Unnamed: 12':'rendas_op_arrendamento_mercantil',
    'Unnamed: 13':'rendas_op_tvm',
    'Unnamed: 14':'rendas_op_derivativos',
    'Unnamed: 15':'rendas_resultado_op_cambio',
    'Unnamed: 16':'rendas_aplicacoes_compulsorias',
    'Unnamed: 17':'receitas_intermediacao_financeira',
    'Unnamed: 18':'despesas_captacao',
    'Unnamed: 19':'despesas_obrigacoes_emprestimos_repasses',
    'Unnamed: 20':'despesas_operacoes_arrendamento_mercantil',
    'Unnamed: 21':'despesas_resultado_op_cambio',
    'Unnamed: 22':'resultado_provisao_credito_dificil_liquidacao',
    'Unnamed: 23':'despesas_intermediacao_financeira',
    'Unnamed: 24':'resultado_intermediacao_financeira',
    'Outras Receitas/Despesas Operacionais':'rendas_prestacao_servicos',
    'Unnamed: 26':'rendas_tarifas_bancarias',
    'Unnamed: 27':'despesas_pessoal',
    'Unnamed: 28':'despesas_administrativas',
    'Unnamed: 29':'despesas_tributarias',
    'Unnamed: 30':'resultado_participacoes',
    'Unnamed: 31':'outras_receitas_operacionais',
    'Unnamed: 32':'outras_despesas_operacionais',
    'Unnamed: 33':'outras_receitas_despesas_operacionais',
    'Resultado Operacional (e) = (c) + (d)':'resultado_operacional',
    'Resultado Não Operacional (f)':'resultado_nao_operacional',
    'Resultado antes da Tributação, Lucro e Participação (g) = (e) + (f)':'resultado_antes_tributacao_lucro_participacao',
    'Imposto de Renda e Contribuição Social (h)':'imposto_renda_contribuicao_social',
    'Participação nos Lucros (i)':'participacao_lucros',
    'Lucro Líquido (j) = (g) + (h) + (i)':'lucro_liquido',
    'Juros Sobre Capital Próprio (k)':'juros_sobre_capital_proprio',
    'Juros Sobre Capital Social de Cooperativas (k)':'juros_sobre_capital_cooperativas',
    'Conglomerado':'conglomerado',
    'Conglomerado Financeiro':'conglomerado_financeiro',
    'Conglomerado Prudencial':'conglomerado_prudencial',
    'TI':'ti'
}
processa_import(nome_relatorio, a_excluir, a_renomear)


nome_relatorio = 'inst_individuais_resumo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 19'
}

a_renomear = {
    'Instituição financeira':'nome_if',
    'Código':'co_if',
    'TCB':'tp_consolidado_bancario',
    'SR':'segmento',
    'TD':'tp_consolidacao',
    'TC':'tp_controle',
    'Cidade':'cidade',
    'UF':'uf',
    'Data':'dt_base',
    'Ativo Total':'ativo_total',
    'Carteira de Crédito Classificada':'carteira_credito_classificada',
    'Passivo Circulante e Exigível a Longo Prazo e Resultados de Exercícios Futuros':'passivo_circulante_exigivel_longo_prazo',
    'Captações':'captacoes',
    'Patrimônio Líquido':'patrimonio_liquido',
    'Lucro Líquido':'lucro_liquido',
    'Número de Agências':'nu_agencias',
    'Número de Postos de Atendimento':'nu_postos_atendimento',
    'Conglomerado':'conglomerado',
    'Conglomerado Financeiro':'conglomerado_financeiro',
    'Conglomerado Prudencial':'conglomerado_prudencial',
    'TI':'ti'
}

processa_import(nome_relatorio, a_excluir, a_renomear)

nome_relatorio = 'inst_individuais_ativo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 28'
}

a_renomear = {
    'Instituição financeira':'nome_if',
    'Código':'co_if',
    'TCB':'tp_consolidado_bancario',
    'SR':'segmento',
    'TD':'tp_consolidacao',
    'TC':'tp_controle',
    'Cidade':'cidade',
    'UF':'uf',
    'Data':'dt_base',
    'Disponibilidades (a)':'disponibilidades',
    'Aplicações Interfinanceiras de Liquidez (b)':'aplicacoes_interfinanceiras_liquidez',
    'TVM e Instrumentos Financeiros Derivativos (c)':'tvm_derivativos',
    'Operações de Crédito':'operacoes_credito',    
    'Unnamed: 15':'provisao_operacoes_credito',
    'Unnamed: 16':'operacoes_credito_liquidas_provisao',
    'Arrendamento Mercantil':'arrendamento_mercantil_receber',
    'Unnamed: 18':'imobilizado_de_arrendamento',
    'Unnamed: 19':'credores_antecipacao_valor_residual',
    'Unnamed: 20':'provisao_sobre_arrendamento_mercantil',
    'Unnamed: 21':'arrendamento_mercantil_liquido_provisao',
    'Outros Créditos - Líquido de Provisão (f)':'outros_creditos_liquidos_provisao',
    'Outros Ativos Realizáveis (g)':'outros_ativos_realizaveis',
    'Permanente Ajustado (h)':'permanente_ajustado',
    'Ativo Total Ajustado (i) = (a) + (b) + (c) + (d) + (e) + (f) + (g) + (h)':'ativo_total_ajustado',
    'Credores por Antecipação de Valor Residual (j)':'credores_antecipacao_valor_residual_2',
    'Ativo Total (k) = (i) - (j)':'ativo_total',
    'Conglomerado':'conglomerado',
    'Conglomerado Financeiro':'conglomerado_financeiro',
    'Conglomerado Prudencial':'conglomerado_prudencial',
    'TI':'ti'
}

processa_import(nome_relatorio, a_excluir, a_renomear)

nome_relatorio = 'inst_individuais_passivo'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 32'
}

a_renomear = {
    'Instituição financeira':'nome_if',
    'Código':'co_if',
    'TCB':'tp_consolidado_bancario',
    'SR':'segmento',
    'TD':'tp_consolidacao',
    'TC':'tp_controle',
    'Cidade':'cidade',
    'UF':'uf',
    'Data':'dt_base',
    'Captações':'depositos_vista',
    'Unnamed: 12':'depositos_poupanca',
    'Unnamed: 13':'depositos_interfinanceiros',
    'Unnamed: 14':'depositos_prazo',
    'Unnamed: 15':'outros_depositos',
    'Unnamed: 16':'deposito_total',
    'Unnamed: 17':'obrigacoes_operacoes_compromissadas',
    'Unnamed: 18':'letras_credito_imobiliario',
    'Unnamed: 19':'letras_credito_agronegocio',
    'Unnamed: 20':'letras_financeiras',
    'Unnamed: 21':'obrigacoes_titulos_valores_mobiliarios_exterior',
    'Unnamed: 22':'outros_recursos_aceites_emissao_titulos',
    'Unnamed: 23':'recursos_aceites_emissao_titulos',
    'Unnamed: 24':'obrigacoes_emprestimos_repasses',
    'Unnamed: 25':'captacoes',
    'Instrumentos Derivativos (f)':'instrumentos_derivativos',
    'Outras Obrigações (g)':'outras_obrigacoes',
    'Passivo Circulante e Exigível a Longo Prazo (h) = (e) + (f) + (g)':'passivo_circulante_exigivel_longo_prazo',
    'Resultados de Exercícios Futuros (i)':'resultado_exercicios_futuros',
    'Patrimônio Líquido (j)':'patrimonio_liquido',
    'Passivo Total (k) = (h) + (i) + (j)':'passivo_total',
    'Conglomerado':'conglomerado',
    'Conglomerado Financeiro':'conglomerado_financeiro',
    'Conglomerado Prudencial':'conglomerado_prudencial',
    'TI':'ti'    
}
processa_import(nome_relatorio, a_excluir, a_renomear)

