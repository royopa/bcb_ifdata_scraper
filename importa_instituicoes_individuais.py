import os
import shutil
import pandas as pd
from sqlalchemy import create_engine

from dotenv import load_dotenv
from dotenv import find_dotenv
load_dotenv(find_dotenv())

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'), echo=False)


nome_relatorio = 'inst_individuais_resumo'
file_name = '{}.csv'.format(nome_relatorio)
df = pd.read_csv(os.path.join('bases', file_name), low_memory=False)
df.columns
df.head()

# remove unnamed columns
df.drop('Unnamed: 0', axis=1, inplace=True)
df.drop('Unnamed: 19', axis=1, inplace=True)

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
    'Patrimônio de Referência para Comparação com o RWA':'patrimonio_referencia',
    'Índice de Basileia':'ic_basileia',
    'Índice de Imobilização':'ic_imobilizacao',
    'Número de Agências':'nu_agencias',
    'Número de Postos de Atendimento':'nu_postos_atendimento',
    'Conglomerado':'conglomerado',
    'Conglomerado Financeiro':'conglomerado_financeiro',
    'Conglomerado Prudencial':'conglomerado_prudencial',
    'TI':'ti'
}

# renomeia as colunas
df = df.rename(columns=a_renomear)

# remove informações que são consolidadas
df = df[df['co_if'].notnull()]

# convert just columns "a" and "b"
df['co_if'] = df['co_if'].astype(int)
df['tp_controle'] = df['tp_controle'].astype(int)

# salva os registros no banco de dados
df.to_sql('{}_import'.format(nome_relatorio), con=engine, if_exists='replace')

# executa para ver os resultados retornados que foram importados
df_banco = engine.execute("SELECT * FROM {}_import".format(nome_relatorio)).fetchall()
print(nome_relatorio)
print(len(df_banco))
print('Registros importados com sucesso.')


nome_relatorio = 'inst_individuais_ativo'
file_name = '{}.csv'.format(nome_relatorio)
df = pd.read_csv(os.path.join('bases', file_name), low_memory=False)

# remove unnamed columns
df.drop('Unnamed: 0', axis=1, inplace=True)
df.drop('Unnamed: 15', axis=1, inplace=True)
df.drop('Unnamed: 20', axis=1, inplace=True)
df.drop('Unnamed: 21', axis=1, inplace=True)
df.drop('Unnamed: 28', axis=1, inplace=True)

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
    'Unnamed: 13':'provisao_operacoes_credito',
    'Unnamed: 14':'operacoes_credito_liquidas_provisao',
    'Arrendamento Mercantil':'arrendamento_mercantil_receber',
    'Unnamed: 16':'imobilizado_de_arrendamento',
    'Unnamed: 17':'credores_antecipacao_valor_residual',
    'Unnamed: 18':'provisao_sobre_arrendamento_mercantil',
    'Unnamed: 19':'arrendamento_mercantil_liquido_provisao',
    'Outros Créditos - Líquido de Provisão (f)':'outros_creditos_liquidos_provisao',
    'Outros Ativos Realizáveis (g)':'outros_ativos_realizaveis',
    'Permanente Ajustado (h)':'permanente_ajustado',
    'Ativo Total Ajustado (i) = (a) + (b) + (c) + (d) + (e) + (f) + (g) + (h)':'ativo_total_ajustado',
    'Credores por Antecipação de Valor Residual (j)':'credores_antecipacao_valor_residual',
    'Ativo Total (k) = (i) - (j)':'ativo_total',
    'Conglomerado':'conglomerado',
    'Conglomerado Financeiro':'conglomerado_financeiro',
    'Conglomerado Prudencial':'conglomerado_prudencial',
    'TI':'ti'
}

# renomeia as colunas
df = df.rename(columns=a_renomear)

# remove informações que são consolidadas
df = df[df['co_if'].notnull()]

# convert just columns "a" and "b"
df['co_if'] = df['co_if'].astype(int)
df['tp_controle'] = df['tp_controle'].astype(int)

# salva os registros no banco de dados
df.to_sql('{}_import'.format(nome_relatorio), con=engine, if_exists='replace')

# executa para ver os resultados retornados que foram importados
df_banco = engine.execute("SELECT * FROM {}_import".format(nome_relatorio)).fetchall()
print(nome_relatorio)
print(len(df_banco))
print('Registros importados com sucesso.')


nome_relatorio = 'inst_individuais_passivo'
file_name = '{}.csv'.format(nome_relatorio)
df = pd.read_csv(os.path.join('bases', file_name), low_memory=False)

# remove unnamed columns
df.drop('Unnamed: 0', axis=1, inplace=True)
df.drop('Unnamed: 24', axis=1, inplace=True)
df.drop('Unnamed: 25', axis=1, inplace=True)
df.drop('Unnamed: 32', axis=1, inplace=True)


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
    'Unnamed: 10':'depositos_poupanca',
    'Unnamed: 11':'depositos_interfinanceiros',
    'Unnamed: 12':'depositos_prazo',
    'Unnamed: 13':'outros_depositos',
    'Unnamed: 14':'deposito_total',
    'Unnamed: 15':'obrigacoes_operacoes_compromissadas',
    'Unnamed: 16':'letras_credito_imobiliario',
    'Unnamed: 17':'letras_credito_agronegocio',
    'Unnamed: 18':'letras_financeiras',
    'Unnamed: 19':'obrigacoes_titulos_valores_mobiliarios_exterior',
    'Unnamed: 20':'outros_recursos_aceites_emissao_titulos',
    'Unnamed: 21':'recursos_aceites_emissao_titulos',
    'Unnamed: 22':'obrigacoes_emprestimos_repasses',
    'Unnamed: 23':'captacoes',
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

# renomeia as colunas
df = df.rename(columns=a_renomear)

# remove informações que são consolidadas
df = df[df['co_if'].notnull()]

# convert just columns "a" and "b"
df['co_if'] = df['co_if'].astype(int)
df['tp_controle'] = df['tp_controle'].astype(int)



# salva os registros no banco de dados
df.to_sql('{}_import'.format(nome_relatorio), con=engine, if_exists='replace')

# executa para ver os resultados retornados que foram importados
df_banco = engine.execute("SELECT * FROM {}_import".format(nome_relatorio)).fetchall()
print(nome_relatorio)
print(len(df_banco))
print('Registros importados com sucesso.')



nome_relatorio = 'inst_individuais_demonstracao_resultado'
file_name = '{}.csv'.format(nome_relatorio)
df = pd.read_csv(os.path.join('bases', file_name), low_memory=False)

# remove unnamed columns
df.drop('Unnamed: 0', axis=1, inplace=True)
df.drop('Unnamed: 23', axis=1, inplace=True)
df.drop('Unnamed: 32', axis=1, inplace=True)
df.drop('Unnamed: 33', axis=1, inplace=True)
df.drop('Unnamed: 41', axis=1, inplace=True)


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
    'Unnamed: 10':'rendas_op_arrendamento_mercantil',
    'Unnamed: 11':'rendas_op_tvm',
    'Unnamed: 12':'rendas_op_derivativos',
    'Unnamed: 13':'resultado_op_cambio',
    'Unnamed: 14':'rendas_aplicacoes_compulsorias',
    'Unnamed: 15':'receitas_intermediacao_financeira',
    'Unnamed: 16':'despesas_captacao',
    'Unnamed: 17':'despesas_obrigacoes_emprestimos_repasses',
    'Unnamed: 18':'despesas_operacoes_arrendamento_mercantil',
    'Unnamed: 19':'resultado_op_cambio',
    'Unnamed: 20':'resultado_provisao_credito_dificil_liquidacao',
    'Unnamed: 21':'despesas_intermediacao_financeira',
    'Unnamed: 22':'resultado_intermediacao_financeira',
    'Outras Receitas/Despesas Operacionais':'rendas_prestacao_servicos',
    'Unnamed: 24':'rendas_tarifas_bancarias',
    'Unnamed: 25':'despesas_pessoal',
    'Unnamed: 26':'despesas_administrativas',
    'Unnamed: 27':'despesas_tributarias',
    'Unnamed: 28':'resultado_participacoes',
    'Unnamed: 29':'outras_receitas_operacionais',
    'Unnamed: 30':'outras_despesas_operacionais',
    'Unnamed: 31':'outras_receitas_despesas_operacionais',
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

# renomeia as colunas
df = df.rename(columns=a_renomear)

# remove informações que são consolidadas
df = df[df['co_if'].notnull()]

# convert just columns "a" and "b"
df['co_if'] = df['co_if'].astype(int)
df['tp_controle'] = df['tp_controle'].astype(int)



# salva os registros no banco de dados
df.to_sql('{}_import'.format(nome_relatorio), con=engine, if_exists='replace')

# executa para ver os resultados retornados que foram importados
df_banco = engine.execute("SELECT * FROM {}_import".format(nome_relatorio)).fetchall()
print(nome_relatorio)
print(len(df_banco))
print('Registros importados com sucesso.')

