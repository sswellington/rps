# RPS

## Introdução 

Variação sazonal da hidroquímica e transporte de materiais dissolvidos na foz do Rio Paraíba do Sul.
Portanto, a observação é segmentada por estação.

* Verão: Janeiro a Março
* Outuno: Abril a Junho
* Inverno: Julho a Setembro
* Primavera: Outubro a Dezembro

### Referência
* [USP](https://www.iag.usp.br/astronomia/inicio-das-estacoes-do-ano)
* [Fiocruz](http://www.fiocruz.br/biosseguranca/Bis/infantil/estacoes-ano.htm#:~:text=Todo%20mundo%20j%C3%A1%20sabe%20que,do%20sol%2C%20dura%20um%20ano.)

## Mineração de dados
Originou como área de pesquisa e aplicação independente em meados da década de 1990. 
Entretanto, as suas origens na matemática, estatística e computação são muito anteriores a esse período ¹.

Objetivo é a preparação e análise das grandes massas de dados, tendo a finalidade de encontrar o conhecimento, tal finalidade é realizada junto ao especialista do domínio dos dados.

Destarte, a área de mineração de dados é segmentada em dados, pré-processamento dos dados; mineração de dados e avaliação.

* **Dados:** conjunto de dados organizados de forma *qualitativa* ou *quantitativa* sobre determinado tema, no qual possibilidade a extração de informação que pode resultar em conhecimento.
* **Pré-processamento dos dados:** selecionar os dados de acordo com a demanda do estudo, descartando assim dados irrelevantes, a fim de tornar a análise dos eficiente e eficaz. 
As etapas são distribuídas:
    * **Limpeza:** remoção de ruídos de dados inconsistentes e ausentes;
    * **Integração:** combinação dos dados de diferentes fontes;
    * **Seleção:** escolha de dados relevantes à análise; e
    * **Transformação:** consolidação dos dados em formato apropriado.
* **Mineração de dados:** utilização de métricas e medidas estatísticas, para representar o conjunto de dados e a sua distribuição. 
Tais medidas são análise descritiva, agrupamento, predição, associação e detecção de anomalias.
* **Avaliação:** identificar os padrões obtidos pela representação do conhecimento são válidos, ou seja, representativo.

--- 

### Dados
Representa a variação sazonal da hidroquímica diluídas na água do Rio Paraíba do Sul no município de Campos dos Goytacazes.
Assim, descrever e encontrar padrões para fundamentar a tomada de decissão. 

Futuramente pode ser implementar algoritmos de mineração que buscam conclusões que extrapolam os dados e permitem inferir predições.
Logo, analise descritiva descreve as características dos dado e a mineração geralmente usada em análise mais abrangentes visando a predição ¹.
Entretanto, precisa ficar atento com falsas correlaçoẽs e predições dos dados ¹.

Análise descritiva permite descrever a distribuição e a correlação dos atributos, utilzando medidas estatísticas, como distribuição de frequência, tendência central e visualização gráfica, sendo para atributos univariada e para bivariada relações entre atributos. 

### Pré-processamento dos dados

#### Limpeza de dados
A baixa qualidade dos dados é um problema que afeta a maior parte das bases de dados reais. 
Assim, as ferramentas para a limpeza de dados atuam no sentido de imputar valores ausentes, suavizar ruídos, identificar valores discrepantes (outliers) e corrigir
inconsistências.

O Método tradicional de imputação de valores ausentes adotado neste trabalho foi o **avestruz**, que descarta os objetos que possuem atributos ausentes.

O Método de redução de dados é adotado a redução de dimensionalidade, em outros termos, descartando atributos irrelevante.

A Transformação dos dados é a padronização das escalas e unidades em bases compatíveis

A visualização de dados é realizado por intermédio de medidas de tendência central, variação e associação, essas métricas são ilustradas por meio de histogramas e gráficos.

## Referência

1. FERRARI, DANIEL GOMES, and LEANDRO NUNES DE CASTRO SILVA. Introdução a mineração de dados. Saraiva Educação SA, 2017.
2. McKinney, Wes. Python for data analysis: Data wrangling with Pandas, NumPy, and IPython. " O'Reilly Media, Inc.", 2012.
3. [OpenStax College. Introductory Statistics. Rice University, 2013](https://openstax.org/details/books/introductory-statistics)
4. Devore, Jay. PROBABILIDADE E ESTATÍSTICA PARA ENGENHARIA E CIÊNCIAS. 6th ed., CENGAGE Learning, 2004. 708 p.
5. Bruce, Peter, Andrew Bruce, and Peter Gedeck. Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python. O'Reilly Media, 2020.
