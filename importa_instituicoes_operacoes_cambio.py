import os
import shutil
import pandas as pd
from sqlalchemy import create_engine
from utils import processa_import

from dotenv import load_dotenv
from dotenv import find_dotenv
load_dotenv(find_dotenv())


nome_relatorio = 'inst_op_cambio_mov_trimestre'

a_excluir = {
    'Unnamed: 0',
    'Unnamed: 31'
}

a_renomear = {
    'Instituição financeira':'nome_if',
    'Código':'co_if',
    'TCB':'tp_consolidado_bancario',
    'Segmento':'segmento',
    'TD':'tp_consolidacao',
    'SR':'segmento',
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
    'Unnamed: 30':'total_valor'
}

processa_import(nome_relatorio, a_excluir, a_renomear)
