import os
import pandas as pd
from sqlalchemy import create_engine

from dotenv import load_dotenv
from dotenv import find_dotenv
load_dotenv(find_dotenv())

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'), echo=False)


file_name = 'base.xlsx'
df = pd.read_excel(os.path.join('.', file_name))
print(df.columns)
print(df.head())

a_renomear = {
    'marcado':'marcado',
    'Alocado':'alocado',
    'SIRAT':'sirat',
    'Outro Nome':'outro_nome',
    'BACEN':'bacen',
    'CNPJ Base':'cnpj_base',
    'Conglomerado Financeiro':'conglomerado',
    'CNPJ':'cnpj',
    'CVM':'cvm',
    'PL (R$ Mil) - 3T19':'pl_mil_3T19'
}

# renomeia as colunas
df = df.rename(columns=a_renomear)

# salva os registros no banco de dados
df.to_sql('base_parametros', con=engine, if_exists='replace')

# executa para ver os resultados retornados que foram importados
df_banco = engine.execute("SELECT * FROM base_parametros").fetchall()
print('{} registros importados com sucesso.'.format(len(df_banco)))
