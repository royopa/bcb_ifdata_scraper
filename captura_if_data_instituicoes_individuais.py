# -*- coding: utf-8 -*-
from utils import main


if __name__ == "__main__":
    folder_name = 'instituicoes_individuais'
    id_tipo_if = 2
    tipos_relatorios = [
        'Resumo',
        'Ativo',
        'Passivo',
        'Demonstração de Resultado'
    ]
    datas_base = range(30, 79)
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base)
