# -*- coding: utf-8 -*-
from utils import main

if __name__ == "__main__":
    FOLDER_NAME = 'conglomerados_financeiros'
    ID_TIPO_IF = 1
    TIPO_INSTITUICAO = 'Conglomerados Financeiros e Instituições Independentes'
    tipos_relatorios = [
        'Resumo',
        'Ativo',
        'Passivo',
        'Demonstração de Resultado',
        'Carteira de crédito ativa Pessoa Física - modalidade e prazo de vencimento',
        'Carteira de crédito ativa Pessoa Jurídica - modalidade e prazo de vencimento',
        'Carteira de crédito ativa Pessoa Jurídica -  por atividade econômica (CNAE)',
        'Carteira de crédito ativa Pessoa Jurídica - por porte do tomador',
        'Carteira de crédito ativa - quantidade de clientes e de operações',
        'Carteira de crédito ativa - por nível de risco da operação',
        'Carteira de crédito ativa - por indexador',
        'Carteira de crédito ativa - por região geográfica'
    ]
    datas_base = range(0, 1)

    main(
        FOLDER_NAME,
        ID_TIPO_IF,
        tipos_relatorios,
        datas_base,
        TIPO_INSTITUICAO
    )
