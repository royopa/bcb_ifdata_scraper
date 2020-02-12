
# coding: utf-8

# In[17]:


import os
import shutil
import pandas as pd
from sqlalchemy import create_engine

from dotenv import load_dotenv
from dotenv import find_dotenv
load_dotenv(find_dotenv())

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'), echo=True)


# In[18]:


nome_relatorio = 'inst_op_cambio_mov_trimestre'
file_name = '{}.csv'.format(nome_relatorio)
df = pd.read_csv(os.path.join('bases', file_name))
df.columns
df.head()

# remove unnamed columns
df.drop('Unnamed: 0', axis=1, inplace=True)
df.drop('Unnamed: 31', axis=1, inplace=True)
df.drop('SR', axis=1, inplace=True)

a_renomear = {
    'Instituição financeira':'nome_if',
    'Código':'co_if',
    'TCB':'tp_consolidado_bancario',
    'Segmento':'segmento',
    'TD':'tp_consolidacao',
    'TC':'tp_controle',
    'Cidade':'cidade',
    'UF':'uf',
    'Data':'dt_base',
    'Exportações':'export_nu_operacoes',
    'Unnamed: 10':'export_valor',
    'Importações':'import_nu_operacoes',
    'Unnamed: 12':'import_valor',
    'Total Primário Comercial':'total_prim_comercial_nu_operacoes',
    'Unnamed: 14':'total_prim_comercial_valor',
    'Transferências do Exterior':'transf_do_exterior_nu_operacoes',
    'Unnamed: 16':'transf_do_exterior_valor',
    'Transferências para o Exterior':'transf_para_exterior_nu_operacoes',
    'Unnamed: 18':'transf_para_exterior_valor',
    'Total Primário Financeiro':'total_prim_financeiro_nu_operacoes',
    'Unnamed: 20':'total_prim_financeiro_valor',
    'Total Primário':'total_prim_nu_operacoes',
    'Unnamed: 22':'total_prim_valor',
    'Interbancário Compra':'interb_compra_nu_operacoes',
    'Unnamed: 24':'interb_compra_valor',
    'Interbancário Venda':'interb_venda_nu_operacoes',
    'Unnamed: 26':'interb_venda_valr',
    'Total Interbancário':'total_interb_nu_operacoes',
    'Unnamed: 28':'total_interb_nu_valor',
    'Total':'total_nu_operacoes',
    'Unnamed: 30':'total_valor',
}

# renomeia as colunas
df = df.rename(columns=a_renomear)

# remove informações que são consolidadas
df = df[df['co_if'].notnull()]

print(df.head())
print(df.dtypes)

# salva os registros no banco de dados
df.to_sql('{}_import'.format(nome_relatorio), con=engine, if_exists='replace')

# executa para ver os resultados retornados que foram importados
df_banco = engine.execute("SELECT * FROM {}_import".format(nome_relatorio)).fetchall()
print(len(df_banco))

print('Registros importados com sucesso.')

