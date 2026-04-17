def is_prime(n: int) -> bool:
    """
    Verifica se um número é primo.

    Um número primo é maior que 1 e não tem divisores positivos além de 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        ValueError: Se a entrada não for um inteiro.
    """
    if not isinstance(n, int):
        raise ValueError("A entrada deve ser um inteiro")
    if n <= 1:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True

# Solicitar entrada do usuário e verificar se é primo
try:
    num = int(input("Digite um número inteiro para verificar se é primo: "))
    if is_prime(num):
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")