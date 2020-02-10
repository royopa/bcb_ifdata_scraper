# -*- coding: utf-8 -*-
from utils import main


if __name__ == "__main__":
    folder_name = 'instituicoes_operacoes_cambio'
    id_tipo_if = 3
    tipo_instituicao = 'Instituições com Operações de Câmbio'
    tipos_relatorios = [
        'Movimentação de Câmbio no Trimestre'
    ]
    datas_base = range(0, 1)
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base, tipo_instituicao)
