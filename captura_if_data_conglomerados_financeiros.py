# -*- coding: utf-8 -*-
from utils import main


if __name__ == "__main__":
    folder_name = 'conglomerados_financeiros'
    id_tipo_if = 1
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
    datas_base = range(0, 79)
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base)
