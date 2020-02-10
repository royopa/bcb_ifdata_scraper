# -*- coding: utf-8 -*-
from utils import main


if __name__ == "__main__":
    folder_name = 'instituicoes_individuais'
    id_tipo_if = 2
    tipo_instituicao = 'Instituições Individuais'
    tipos_relatorios = [
        'Resumo',
        'Ativo',
        'Passivo',
        'Demonstração de Resultado'
    ]
    
    # de 23 a 79 instituicoes individuais é 1
    datas_base = range(0, 1)
    # de 0 a 23 instituicoes individuais é 2
    main(folder_name, id_tipo_if, tipos_relatorios, datas_base, tipo_instituicao)
