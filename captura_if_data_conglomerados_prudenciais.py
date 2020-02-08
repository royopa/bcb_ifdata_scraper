# -*- coding: utf-8 -*-
from utils import main

if __name__ == "__main__":
    folder_name = 'conglomerados_prudenciais'
    id_tipo_if = 0
    tipos_relatorios = [
        'Resumo',
        'Ativo',
        'Passivo',
        'Demonstração de Resultado',
        'Informações de Capital',
        'Segmentação',
    ]
    datas_base = range(3, 79)
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base)
