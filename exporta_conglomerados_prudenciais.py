import os
import pandas as pd
from sqlalchemy import create_engine

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'), echo=False)

# executa para ver os resultados retornados que foram importados
NOME_TABELA = 'prud_geral'
QUERY = "SELECT * FROM {} WHERE dt_base = '09/2019'".format(NOME_TABELA)
dataframe = pd.read_sql(QUERY, engine)

FILE_SAIDA = '{}.xlsx'.format(NOME_TABELA)
dataframe.to_excel(FILE_SAIDA, index=False)
print('{} registros exportados com sucesso.'.format(len(dataframe)), FILE_SAIDA)
