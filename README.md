# Projeto_SCTEC
Projeto avaliativo para o curso analise de dados SCTEC


Para o desenvolvimento das consultar, foram criados 2 arquivos query de consulta SQL, o primero arquivo "query_1" foi criado para a consulta dos salarios por departamento.

A pesquisa é feita em cima do banco de funcionarios(HR.EMPLOYEES e), conectados através do left join, com o banco de departamentos(HR.DEPARTMENTS d), e o de trabalhos(HR.JOBS j)

Para ser feito o devido filtro de valores nulos, foi criado um where para salarios maiores que 0, e departamentos com que não são nulos, para garantir a visualização apenas de valores validos.

Para a segunda pesquisa "query_2" foi feito a pesquisa ainda por funcionario para garantir a informação de salario, para a pesquisa de salarios por região, cidade, estado e pais.

Na query_2 os departamentos carregam a chave extrangeira de localização (LOCATION_ID), onde se conecta com o banco HR.LOCATIONS, nos trazendo a informação da cidade, para o banco de pais HR.COUNTRIES, se contecta ao de localição que carrega a chave COUNTRY_ID, nos dados os paizes, e finalizando a de região, conectada a de pais HR.REGIONS r on r.REGION_ID = c.REGION_ID, que nos concede o estado.

Mantive no where o salario maior que 0 e departamento is not null, para garantir a visualização, e adicionado region is not null, para garantir a vizualização apenas de regiões validas, como a região, cidade e estado estão conectados, foi necessário apenas a de região.