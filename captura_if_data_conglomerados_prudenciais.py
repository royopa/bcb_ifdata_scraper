# -*- coding: utf-8 -*-
from utils import main

if __name__ == "__main__":
    FOLDER_NAME = 'conglomerados_prudenciais'
    ID_TIPO_IF = 0
    TIPO_INSTITUICAO = 'Conglomerados Prudenciais e Instituições Independentes'
    tipos_relatorios = [
        'Resumo',
        'Ativo',
        'Passivo',
        'Demonstração de Resultado',
        'Informações de Capital',
        'Segmentação',
    ]
    datas_base = range(0, 1)
    main(FOLDER_NAME, ID_TIPO_IF, tipos_relatorios, datas_base, TIPO_INSTITUICAO)
