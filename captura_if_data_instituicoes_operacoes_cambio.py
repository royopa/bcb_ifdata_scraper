# -*- coding: utf-8 -*-
from utils import main


if __name__ == "__main__":
    FOLDER_NAME = 'instituicoes_operacoes_cambio'
    ID_TIPO_IF = 3
    TIPO_INSTITUICAO = 'Instituições com Operações de Câmbio'
    tipos_relatorios = [
        'Movimentação de Câmbio no Trimestre'
    ]
    datas_base = range(0, 1)
    main(FOLDER_NAME, ID_TIPO_IF, tipos_relatorios, datas_base, TIPO_INSTITUICAO)
