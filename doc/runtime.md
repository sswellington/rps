# Runtime

## Dataframe
O teste é constituído pela execução do programa que realizar a leitura e carregamento do arquivo csv da memória secundária para primária.
Então, o teste é repetido 1000 vezes a fim de obter dados para calcular a média aritmética.
A linguagem Julia `1.6.1` obteve a média aritmética de 0.023850916827999953 segundos, porém a primeira execução foi necessário compilar o programa, sendo o valor de 22.471821446 segundos, o que interferiu na média de forma negativa.
Já a linguagem Python `3.9.0` obteve a média aritmética de 0.009266181707382201 segundos, mantendo os valores próximos a média durante todas iterações do programa.
Logo, a execução do programa é realizado apenas uma vez e a escolhe neste trabalho é a linguagem Python.
 