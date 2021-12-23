# -*- coding: utf-8 -*-
import time
import os
import glob
import shutil
from pathlib import Path
import traceback

from dotenv import find_dotenv, load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

pd.set_option('display.max_columns', 200)
load_dotenv(find_dotenv())


def main(folder_name, id_tipo_if, tipos_relatorios, datas_base, tipo_instituicao):
    print('='*80)
    print('Iniciando captura na página ifdata - {}'.format(tipo_instituicao))
    print('='*80)

    download_folder_path = prepare_download_folder(folder_name)
    browser = get_browser_ifdata()

    if browser is False:
        return False

    browser.implicitly_wait(10)
    for id_data_base in datas_base:
        browser.execute_script('selectDataBase(' + str(id_data_base) + ')')
        countdown(1)
        data_base = browser.execute_script(
            'return document.getElementById("btnDataBase").innerText')
        print('Seleciona a data-base', data_base, "\n")

        try:
            browser.find_element_by_id('btnTipoInst').click()
            elem = browser.find_element_by_link_text(tipo_instituicao)
            elem.click()

        except Exception:
            print('Tipo de instituição não encontrada na data base {}, pulando...'.format(
                data_base))
            print("\n")
            continue

        # itens do relatório
        for tipo_relatorio in tipos_relatorios:
            try:
                browser.find_element_by_id('btnRelatorio').click()
                elem = browser.find_element_by_link_text(tipo_relatorio)
                elem.click()
                processa_relatorio(browser, id_tipo_if, download_folder_path)

            except Exception:
                print('Relatório: {}'.format(tipo_relatorio))
                print(
                    'Tipo de relatório não encontrado ou arquivo já baixado, pulando...')
                print("\n")
                continue

    browser.close()
    browser.quit()
    return True


def prepare_download_folder(folder_name):
    folder_path = os.path.join('downloads', folder_name)
    return prepare_folder(folder_path)


def prepare_folder(folder_path):
    if not os.path.exists(folder_path):
        Path(folder_path).mkdir(parents=True, exist_ok=True)

    return folder_path


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

    xpath = '//*[@id="ulDataBase"]/li[79]/a'
    wait = WebDriverWait(browser, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    botao.click()

    return browser


def get_webdriver():
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    prefs = {"download.default_directory": os.path.join(
        str(os.path.dirname(os.path.abspath(__file__))), 'downloads')}
    options.add_experimental_option("prefs", prefs)

    try:
        browser = webdriver.Chrome(
            options=options,
            executable_path=list(
                filter(lambda _file: 'chrome' in _file, glob.glob(
                    '{0}/{1}/*'.format(os.path.dirname(
                        '/'.join(os.path.abspath(__file__).split('/')[:-1])
                    ), 'resources')
                ))
            )[0]
        )
    except Exception as expt:
        _traceback = traceback.format_exc()
        print(expt, "\n")
        print(_traceback)
        return False

    return browser


def countdown(_time):
    while _time:
        mins, secs = divmod(_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        _time -= 1


def processa_relatorio(browser, id_tipo_if, download_folder_path):
    data_base = browser.execute_script(
        'return document.getElementById("btnDataBase").innerText')
    data_base = data_base.replace("/", "")
    trimestre = data_base[0:2]
    ano = data_base[2:]

    rel = browser.execute_script(
        'return document.getElementById("btnRelatorio").innerText')
    rel = formata_nome_relatorio(rel)

    path_new_file = os.path.join(
        download_folder_path, '{}_{}_{}_{}.csv'.format(ano, trimestre, id_tipo_if, rel))
    path_downloaded_file = os.path.join(
        str(os.path.dirname(os.path.abspath(__file__))), 'downloads', 'dados.csv')

    if os.path.exists(path_new_file):
        print('Arquivo já baixado, pulando')
        print(path_new_file)
        os.remove(path_downloaded_file)
        return False

    print('Aguarda o carregamento do relatório')
    print('{} - {}/{}'.format(rel, trimestre, ano))
    countdown(5)

    wait = WebDriverWait(browser, 120)
    download_link = wait.until(
        EC.element_to_be_clickable((By.ID, "aExportCsv")))
    download_link.click()

    print('Baixa arquivo dados.csv')
    countdown(2)

    shutil.move(
        path_downloaded_file,
        path_new_file
    )

    return True


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
        'carteira de crédito ativa pessoa jurídica -  por atividade econômica (cnae)'.lower(
        ),
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
