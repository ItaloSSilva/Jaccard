
from collections import Counter

# Função para calcular o Jaccard 
def similaridade_jaccard(s1, s2):
    set1 = set(s1.split())
    set2 = set(s2.split())
    intersecao_tamanho = len(set1.intersection(set2))
    uniao = len(set1) + len(set2) - intersecao_tamanho
    return intersecao_tamanho / uniao if uniao > 0 else 0.0

# Banco de dados 
dados = [
    "carro",
    "carro 2",
    "outro carro 1",
    # ... adicione mais strings aqui
]

# String de consulta
string = "carro"

# Calcula a similaridade Jaccard entre a string de consulta e todas as strings no banco de dados
similaridades = []
for entrada in dados:
    similaridade = similaridade_jaccard(string, entrada)
    similaridades.append((entrada, similaridade))

# Classifique as similaridades em ordem decrescente
similaridades.sort(key=lambda x: x[1], reverse=True)

# Imprima as strings do banco de dados classificadas por similaridade
for entry, similaridade in similaridades:
    print(f"String de Consulta: {string}")
    print(f"{entrada}: Similaridades entre as strings = {similaridade:.2f}")