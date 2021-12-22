import os
import pandas as pd
from sqlalchemy import create_engine

from dotenv import load_dotenv
from dotenv import find_dotenv
load_dotenv(find_dotenv())

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'), echo=False)

# executa para ver os resultados retornados que foram importados
nome_tabela = 'prud_geral'
query = "SELECT * FROM {} WHERE dt_base = '09/2019'".format(nome_tabela)
df = pd.read_sql(query, engine)

file_saida = '{}.xlsx'.format(nome_tabela)
df.to_excel(file_saida, index=False)
print('{} registros exportados com sucesso.'.format(len(df)), file_saida)
