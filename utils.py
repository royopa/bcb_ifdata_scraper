# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import os
import shutil
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def processa_relatorio(browser, id_tipo_if, download_folder_path):
    data_base = browser.execute_script('return document.getElementById("btnDataBase").innerText')
    data_base = data_base.replace("/","")
    trimestre = data_base[0:2]
    ano = data_base[2:]

    rel = browser.execute_script('return document.getElementById("btnRelatorio").innerText')
    rel = formata_nome_relatorio(rel)
    print('Aguarda o carregamento do relatório {} - {}/{}'.format(rel, trimestre, ano))
    countdown(5)

    wait = WebDriverWait(browser, 120)
    download_link = wait.until(EC.element_to_be_clickable((By.ID, "aExportCsv")))
    download_link.click()

    print('Baixa arquivo dados.csv')
    countdown(2)

    shutil.move(
        os.path.join(os.sep,'home','rodrigo','Downloads','dados.csv'),
        os.path.join(download_folder_path, '{}_{}_{}_{}.csv'.format(ano, trimestre, id_tipo_if, rel))
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
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome('chromedriver', options=options)
    
    return browser


def prepare_download_folder(folder_name):
    download_folder_path = os.path.join('downloads', folder_name)

    if not os.path.exists(download_folder_path):
        Path(download_folder_path).mkdir(parents=True, exist_ok=True)

    return download_folder_path


def get_browser_ifdata():
    browser = get_webdriver()
    print('Acessa a página e aguarda o carregamento do combo de datas base')
    url = 'https://www3.bcb.gov.br/ifdata/index.html'
    browser.get(url)
    countdown(60)

    botao = browser.find_element_by_id('btnDataBase')
    botao.click()

    # última data disponível no combo, a partir que ela estiver visível
    # quer dizer que a página carregou completamente
    xpath = '//*[@id="ulDataBase"]/li[79]/a'
    wait = WebDriverWait(browser, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    
    botao.click()

    return browser


def main(folder_name, id_tipo_if, tipos_relatorios, datas_base):
    download_folder_path = prepare_download_folder(folder_name)
    browser = get_browser_ifdata()

    # baixa todas as bases de dados (de 0 a 78 em 08/02/2020)
    browser.implicitly_wait(10)
    for id_data_base in datas_base:
        print('Seleciona data-base', id_data_base)
        browser.execute_script('selectDataBase(' + str(id_data_base) + ')')
        countdown(1)

        print('Seleciona tipo instituição')
        browser.execute_script('selectTipoInst(' + str(id_tipo_if) + ')')
        countdown(1)

        # itens do relatório
        for tipo_relatorio in tipos_relatorios:
            try:
                browser.find_element_by_id('btnRelatorio').click()
                elem = browser.find_element_by_link_text(tipo_relatorio)
                elem.click()
                processa_relatorio(browser, id_tipo_if, download_folder_path)
            except:
                continue

    browser.close()
    browser.quit()
