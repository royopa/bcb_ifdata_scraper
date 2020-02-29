# -*- coding: utf-8 -*-
from utils import main

if __name__ == "__main__":
    datas_base = range(0, 79)
    
    folder_name = 'conglomerados_prudenciais'
    id_tipo_if = 0
    tipo_instituicao = 'Conglomerados Prudenciais e Instituições Independentes'
    tipos_relatorios = [
        'Resumo',
        'Ativo',
        'Passivo',
        'Demonstração de Resultado',
        'Informações de Capital',
        'Segmentação',
    ]
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base, tipo_instituicao)

    folder_name = 'conglomerados_financeiros'
    id_tipo_if = 1
    tipo_instituicao = 'Conglomerados Financeiros e Instituições Independentes'
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
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base, tipo_instituicao)
    
    folder_name = 'conglomerados_prudenciais'
    id_tipo_if = 0
    tipo_instituicao = 'Conglomerados Prudenciais e Instituições Independentes'
    tipos_relatorios = [
        'Resumo',
        'Ativo',
        'Passivo',
        'Demonstração de Resultado',
        'Informações de Capital',
        'Segmentação',
    ]
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base, tipo_instituicao)
    
    folder_name = 'instituicoes_individuais'
    id_tipo_if = 2
    tipo_instituicao = 'Instituições Individuais'
    tipos_relatorios = [
        'Resumo',
        'Ativo',
        'Passivo',
        'Demonstração de Resultado'
    ]
    
    # de 0 a 23 instituicoes individuais é 2
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base, tipo_instituicao)
    
    folder_name = 'instituicoes_operacoes_cambio'
    id_tipo_if = 3
    tipo_instituicao = 'Instituições com Operações de Câmbio'
    tipos_relatorios = [
        'Movimentação de Câmbio no Trimestre'
    ]
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base, tipo_instituicao)    
