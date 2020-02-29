# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import os
import shutil
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback
import pandas as pd
pd.set_option('display.max_columns', 200)

from sqlalchemy import create_engine

from dotenv import load_dotenv
from dotenv import find_dotenv
load_dotenv(find_dotenv())


def processa_relatorio(browser, id_tipo_if, download_folder_path):
    data_base = browser.execute_script('return document.getElementById("btnDataBase").innerText')
    data_base = data_base.replace("/","")
    trimestre = data_base[0:2]
    ano = data_base[2:]

    rel = browser.execute_script('return document.getElementById("btnRelatorio").innerText')
    rel = formata_nome_relatorio(rel)
    
    path_new_file = os.path.join(download_folder_path, '{}_{}_{}_{}.csv'.format(ano, trimestre, id_tipo_if, rel))
    path_downloaded_file = os.path.join(str(os.path.dirname(os.path.abspath(__file__))), 'downloads','dados.csv')

    if os.path.exists(path_new_file):
        print('Arquivo já baixado, pulando')
        print(path_new_file)
        os.remove(path_downloaded_file)
        return False

    print('Aguarda o carregamento do relatório')
    print('{} - {}/{}'.format(rel, trimestre, ano))
    countdown(5)

    wait = WebDriverWait(browser, 120)
    download_link = wait.until(EC.element_to_be_clickable((By.ID, "aExportCsv")))
    download_link.click()

    print('Baixa arquivo dados.csv')
    countdown(2)
   
    shutil.move(
        path_downloaded_file,
        path_new_file
    )


# retira caracteres especiais do nome do arquivo e formata nome
def formata_nome_relatorio(rel):
    rel = rel.lower()
    
    rel = rel.replace(
        'demonstração de resultado', 'demonstracao_de_resultado')
    rel = rel.replace(
        'informações de capital', 'informacoes_de_capital')
    rel = rel.replace(
        'segmentação', 'segmentacao')
    rel = rel.replace(
        'carteira de crédito ativa pessoa física - modalidade e prazo de vencimento'.lower(),
        'carteira_credito_ativa_pf_modalidade_prazo_vencimento')
    rel = rel.replace(
        'carteira de crédito ativa pessoa jurídica - modalidade e prazo de vencimento'.lower(),
        'carteira_credito_ativa_pj_modalidade_prazo_vencimento')
    rel = rel.replace(
        'carteira de crédito ativa pessoa jurídica -  por atividade econômica (cnae)'.lower(),
        'carteira_credito_ativa_pj_atividade_economica_cnae')
    rel = rel.replace(
        'carteira de crédito ativa pessoa jurídica - por porte do tomador'.lower(),
        'carteira_credito_ativa_pj_porte_tomador')
    rel = rel.replace(
        'carteira de crédito ativa - quantidade de clientes e de operações'.lower(),
        'carteira_credito_ativa_pj_quantidade_clientes_operacoes')
    rel = rel.replace(
        'carteira de crédito ativa - por nível de risco da operação'.lower(),
        'carteira_credito_ativa_pj_nivel_risco')
    rel = rel.replace(
        'carteira de crédito ativa - por indexador'.lower(),
        'carteira_credito_ativa_por_indexador')
    rel = rel.replace(
        'movimentação de câmbio no trimestre'.lower(),
        'movimentacao_cambio_trimestre')

    return rel


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1


def get_webdriver():
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    prefs = {"download.default_directory" : os.path.join(str(os.path.dirname(os.path.abspath(__file__))), 'downloads')}
    options.add_experimental_option("prefs",prefs)

    try:
        browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
    except Exception as e:
        tb = traceback.format_exc()
        print(e, "\n")
        print(tb)
        return False

    return browser


# monta os arquivos em um único arquivo
def merge_arquivos(lista_paths, file_name):
    print('='*80)
    print('Consolidando arquivos - {}'.format(file_name))
    print('='*80)
    
    dfs = []
    for file_path in sorted(lista_paths):
        df = pd.read_csv(file_path, sep=";")
        dfs.append(df)

    df = pd.concat(dfs, axis=0, ignore_index=True)

    df.to_csv(os.path.join('bases', file_name), sep=";")
    return True


def prepare_download_folder(folder_name):
    folder_path = os.path.join('downloads', folder_name)
    return prepare_folder(folder_path)


def prepare_bases_folder():
    folder_path = os.path.join('bases')
    return prepare_folder(folder_path)
   

def prepare_folder(folder_path):
    if not os.path.exists(folder_path):
        Path(folder_path).mkdir(parents=True, exist_ok=True)

    return folder_path


def prepare_bases_import_folder():
    folder_path = os.path.join('bases_import')
    return prepare_folder(folder_path)


def get_browser_ifdata():
    browser = get_webdriver()
    
    if browser is False:
        return False
    
    print('Acessa a página e aguarda o carregamento do combo de datas base')
    url = 'https://www3.bcb.gov.br/ifdata/index.html'
    browser.get(url)
    countdown(25)

    botao = browser.find_element_by_id('btnDataBase')
    botao.click()

    # última data disponível no combo, a partir que ela estiver visível
    # quer dizer que a página carregou completamente
    xpath = '//*[@id="ulDataBase"]/li[79]/a'
    wait = WebDriverWait(browser, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    
    botao.click()

    return browser


def main(folder_name, id_tipo_if, tipos_relatorios, datas_base, tipo_instituicao):
    print('='*80)
    print('Iniciando captura na página ifdata - {}'.format(tipo_instituicao))
    print('='*80)
    
    download_folder_path = prepare_download_folder(folder_name)
    browser = get_browser_ifdata()

    if browser is False:
        return False
    
    # baixa todas as bases de dados (de 0 a 78 em 08/02/2020)
    browser.implicitly_wait(10)
    for id_data_base in datas_base:
        browser.execute_script('selectDataBase(' + str(id_data_base) + ')')
        countdown(1)
        data_base = browser.execute_script('return document.getElementById("btnDataBase").innerText')
        print('Seleciona a data-base', data_base, "\n")

        try:
            browser.find_element_by_id('btnTipoInst').click()
            elem = browser.find_element_by_link_text(tipo_instituicao)
            elem.click()
        except:
            print('Tipo de instituição não encontrada na data base {}, pulando...'.format(data_base))
            print("\n")
            continue

        # itens do relatório
        for tipo_relatorio in tipos_relatorios:
            try:
                browser.find_element_by_id('btnRelatorio').click()
                elem = browser.find_element_by_link_text(tipo_relatorio)
                elem.click()
                processa_relatorio(browser, id_tipo_if, download_folder_path)
            except:
                print('Relatório: {}'.format(tipo_relatorio))
                print('Tipo de relatório não encontrado ou arquivo já baixado, pulando...')
                print("\n")
                continue

    browser.close()
    browser.quit()


def processa_import(nome_relatorio, a_excluir, a_renomear):
    print('='*80)
    print('Importando {} para a base'.format(nome_relatorio))
    print('='*80)

    engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'), echo=False)

    file_name = '{}.csv'.format(nome_relatorio)
    
    print('Lendo o csv {}'.format(file_name))
    df = pd.read_csv(
        os.path.join('bases', file_name),
        low_memory=False,
        sep=";"
    )

    print('O dataframe tem {} registros'.format(len(df)))    
    
    # renomeia as colunas
    print('Renomeando colunas')
    df = df.rename(columns=a_renomear)

    # remove informações que são consolidadas
    print('Removendo registros inválidos')
    df = df[df['co_if'].notnull()]

    # remove points from co_if
    df['co_if'] = df['co_if'].astype(str)
    df['co_if'] = df['co_if'].str.replace('.', '')

    # convert just columns "a" and "b"
    df['co_if'] = df['co_if'].astype(int)
    df['tp_controle'] = df['tp_controle'].fillna(0)
    df['tp_controle'] = df['tp_controle'].astype(int)
   
    # remove unnamed columns
    print('Removendo colunas não utilizadas')
    for nome_coluna in sorted(a_excluir):
        df.drop(nome_coluna, axis=1, inplace=True)

    # ignora as colunas que já possuem o campo do tipo string
    # e que não devem tem seu tipo alteradas
    lista_ignorar = [
        'nome_if',
        'co_if',  
        'tp_consolidado_bancario',
        'segmento',
        'tp_consolidacao',
        'tp_controle',
        'cidade', 
        'uf',
        'dt_base',
        'conglomerado',
        'dt_ultima_alteracao_segmento',
        'conglomerado',
        'conglomerado_financeiro',
        'conglomerado_prudencial',
    ]

    print('Alterando tipos das colunas e substituindo valores, caso necessário')
    for nome_coluna in a_renomear:
        coluna = a_renomear.get(nome_coluna)
        if coluna not in lista_ignorar:
            df[coluna] = df[coluna].astype(str)
            df[coluna] = df[coluna].str.replace('.', '')
            df[coluna] = df[coluna].str.replace(',', '.')
            df[coluna] = df[coluna].str.replace('Não', '0')
            df[coluna] = df[coluna].str.replace('Sim', '1')
            df[coluna] = df[coluna].str.replace('NI', '0')
            df[coluna] = df[coluna].str.replace('NA', '0')
            df[coluna] = df[coluna].str.replace('%', '')
            df[coluna] = df[coluna].str.replace('*', '0')

            df[coluna] = df[coluna].astype(float)
            #df[coluna] = df[coluna].apply(pd.to_numeric, errors='coerce')

    print('Criando os índices do dataframe')
    df.set_index(['co_if', 'dt_base'])

    # salva os registros no banco de dados    
    if os.environ.get('IMPORT_TO_DATABASE'):    
        print('Salvando registros no banco ({})'.format(len(df)))
        df.to_sql('{}_import'.format(nome_relatorio), con=engine, if_exists='replace')

        # executa um select na tabela para ver os registros importados
        query = "SELECT * FROM {}_import".format(nome_relatorio)
        df_banco = pd.read_sql(query, engine)
        df_banco.set_index(['co_if', 'dt_base'])
        print('Registros importados com sucesso.')
        
    if os.environ.get('SAVE_IMPORT_CSV'):
        print('Salvando arquivo csv dos registros ({})'.format(len(df)))
        bases_import_folder = prepare_bases_import_folder()
        file_name = '{}_import.csv'.format(nome_relatorio)
        file_import_database_path = os.path.join(bases_import_folder, file_name)
        df.to_csv(file_import_database_path, sep=";")

        # executa um select na tabela para ver os registros importados
        df_csv = pd.read_csv(file_import_database_path, sep=';', low_memory=False)
        df_csv.set_index(['co_if', 'dt_base'])
        print('Registros importados com sucesso.')        
        
    return True
