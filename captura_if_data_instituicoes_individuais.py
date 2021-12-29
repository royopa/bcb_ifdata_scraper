# -*- coding: utf-8 -*-
from utils import main


if __name__ == "__main__":
    FOLDER_NAME = 'instituicoes_individuais'
    ID_TIPO_IF = 2
    TIPO_INSTITUICAO = 'Instituições Individuais'
    tipos_relatorios = [
        'Resumo',
        'Ativo',
        'Passivo',
        'Demonstração de Resultado'
    ]

    # de 23 a 79 instituicoes individuais é 1
    datas_base = range(0, 1) # range(0, 1) é o primeiro relatório da lista disponível
    # de 0 a 23 instituicoes individuais é 2
    main(FOLDER_NAME, ID_TIPO_IF, tipos_relatorios, datas_base, TIPO_INSTITUICAO)
