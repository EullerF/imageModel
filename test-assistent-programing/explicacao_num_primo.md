### Explicação linha a linha do código em num_primo.py

O código define uma função `is_prime(n)` que verifica se um número inteiro `n` é primo, com melhorias de clean code (type hints, validação de entrada, nomes descritivos), seguido de um programa interativo que solicita entrada do usuário e verifica se o número é primo. Aqui vai a explicação técnica e didática, linha por linha:

1. **`def is_prime(n: int) -> bool:`**  
   Define uma função chamada `is_prime` com type hints: `n` deve ser `int`, e retorna `bool`. Isso melhora a legibilidade e permite verificações estáticas.

2. **`"""`**  
   Inicia uma docstring detalhada, seguindo convenções como Google/NumPy style, incluindo Args, Returns e Raises.

3. **`Verifica se um número é primo.`**  
   Parte da docstring: explica o objetivo da função.

4. **`Um número primo é maior que 1 e não tem divisores positivos além de 1 e ele mesmo.`**  
   Define tecnicamente um número primo.

5. **`Args:`**  
   Seção da docstring para argumentos.

6. **`n (int): O número a ser verificado.`**  
   Descreve o parâmetro `n`.

7. **`Returns:`**  
   Seção para retorno.

8. **`bool: True se o número for primo, False caso contrário.`**  
   Descreve o valor de retorno.

9. **`Raises:`**  
   Seção para exceções.

10. **`ValueError: Se a entrada não for um inteiro.`**  
    Descreve a exceção lançada.

11. **`"""`**  
    Fecha a docstring.

12. **`if not isinstance(n, int):`**  
    Valida se `n` é um inteiro usando `isinstance`. Isso trata entradas inválidas (ex.: floats, strings), lançando erro se não for int.

13. **`raise ValueError("A entrada deve ser um inteiro")`**  
    Lança `ValueError` com mensagem clara se a validação falhar.

14. **`if n <= 1:`**  
    Verifica se `n` ≤ 1. Números ≤ 1 não são primos.

15. **`return False`**  
    Retorna `False` para casos não primos.

16. **`for divisor in range(2, int(n**0.5) + 1):`**  
    Loop `for` com variável `divisor` (mais descritiva que `i`). Itera de 2 até √n, otimizando a busca por divisores.

17. **`if n % divisor == 0:`**  
    Verifica se `n` é divisível por `divisor` (resto zero).

18. **`return False`**  
    Retorna `False` se encontrar divisor.

19. **`return True`**  
    Retorna `True` se nenhum divisor for encontrado.

20. **`# Solicitar entrada do usuário e verificar se é primo`**  
    Comentário indicando o início do programa interativo.

21. **`try:`**  
    Inicia bloco try-except para tratar erros de entrada.

22. **`num = int(input("Digite um número inteiro para verificar se é primo: "))`**  
    Solicita entrada do usuário como string, converte para int. Se não for número, lança ValueError.

23. **`if is_prime(num):`**  
    Chama a função is_prime com o número inserido.

24. **`print(f"O número {num} é primo.")`**  
    Imprime mensagem se for primo.

25. **`else:`**  
    Caso contrário.

26. **`print(f"O número {num} não é primo.")`**  
    Imprime mensagem se não for primo.

27. **`except ValueError:`**  
    Captura ValueError (de int() ou de is_prime, mas is_prime lança se não int, mas aqui num já é int).

28. **`print("Entrada inválida. Por favor, digite um número inteiro.")`**  
    Imprime mensagem de erro para entrada inválida.

Este código segue princípios de clean code: legível, robusto (validação), documentado e eficiente (O(√n)). O programa agora interage com o usuário em vez de usar testes fixos.