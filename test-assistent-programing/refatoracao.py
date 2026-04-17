def calcular_estatisticas(lista):
    """
    Calcula e retorna o total, média, maior e menor valor de uma lista de números.
    """
    total = sum(lista)
    media = total / len(lista)
    maior = max(lista)
    menor = min(lista)
    return total, media, maior, menor

# Lista de números para teste
numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# Chamada da função e desempacotamento dos resultados
total, media, maior, menor = calcular_estatisticas(numeros)

# Impressão dos resultados
print("total:", total)
print("media:", media)
print("maior:", maior)
print("menor:", menor)