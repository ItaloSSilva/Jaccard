# Jaccard
Experimentando uma forma nova de Data Matching.

Este código fornece uma maneira de calcular a similaridade entre uma string de consulta e uma lista de strings armazenadas em um banco de dados. A similaridade é calculada usando o coeficiente de Jaccard, que mede a sobreposição entre os conjuntos de palavras nas strings.

Função para Calcular a Similaridade de Jaccard:

A função similaridade_jaccard(s1, s2) é usada para calcular a similaridade de Jaccard entre duas strings s1 e s2. Ela segue os seguintes passos:

Divide as duas strings em conjuntos de palavras (set1 e set2).
Calcula o tamanho da interseção (número de palavras comuns) entre os conjuntos.
Calcula o tamanho da união (total de palavras em ambas as strings, descontando as palavras em comum).
Retorna a similaridade de Jaccard, que é a divisão do tamanho da interseção pelo tamanho da união. Se o tamanho da união for zero, a similaridade é definida como 0.0.

Banco de Dados:

O banco de dados é uma lista chamada dados, que contém várias strings que você deseja comparar com a string de consulta. Você pode adicionar quantas strings desejar a essa lista.

String de Consulta:

A string de consulta é aquela que você deseja comparar com as strings no banco de dados. Você pode definir a string de consulta na variável string.

Cálculo da Similaridade:

O código calcula a similaridade de Jaccard entre a string de consulta e todas as strings no banco de dados. As similaridades são armazenadas em uma lista chamada similaridades, onde cada elemento é uma tupla contendo a string do banco de dados e a respectiva similaridade.

Classificação das Similaridades:

As similaridades são classificadas em ordem decrescente, com base na similaridade de Jaccard. Isso significa que as strings do banco de dados com maior similaridade à string de consulta aparecerão primeiro na lista.

Saída:

O código imprime as strings do banco de dados, classificadas por similaridade, juntamente com a similaridade calculada. Isso permite que você veja quais strings do banco de dados são mais semelhantes à sua string de consulta.

Para usar o código, você pode ajustar a variável dados para incluir suas próprias strings e definir a string de consulta em string. Em seguida, execute o código para obter uma lista classificada das strings no banco de dados com base na similaridade com a sua string de consulta.
