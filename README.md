# bcb_ifdata_scraper

Captura e faz o download dos relatórios do [BACEN IFDATA](https://www3.bcb.gov.br/ifdata/index.html).

## Iniciando

Para iniciar o processo primeiro é necessario a criação de um ambiente virtual no pipenv e instalação das dependências, que pode ser feita com o comando abaixo:

´´´
> pipenv install
> pipenv shell
´´´

## Capturando arquivos

A Captura dos arquivos do site é realizada de acordo com o tipo de instituição financeira, através dos scripts abaixo:

´´´
> python captura_if_data_instituicoes_individuais.py
> python captura_if_data_conglomerados_financeiros.py
> python captura_if_data_conglomerados_prudenciais.py
> python captura_if_data_instituicoes_operacoes_cambio.py
´´´


