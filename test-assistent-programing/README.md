# Test Assistant Programming 🐍

Um projeto educacional focado em conceitos fundamentais de programação em Python, incluindo clean code, refatoração, tratamento de erros e boas práticas de desenvolvimento.

---

## 📋 Estrutura do Projeto

```
test-assistent-programing/
├── README.md                    # Este arquivo
├── num_primo.py                # Verificador de números primos (Clean Code)
├── explicacao_num_primo.md      # Documentação linha a linha
├── refatoracao.py              # Código refatorado (Estatísticas)
├── explicacao_refatoracao.md    # Explicação da refatoração
├── debug.py                    # Programa com erros propositais
└── explicacao-debug.md          # Documentação dos erros
```

---

## 🎯 Módulos Principais

### 1. **Verificador de Números Primos** (`num_primo.py`)

Um programa interativo que verifica se um número é primo, demonstrando clean code e best practices.

#### Características
- ✅ Type hints para melhor legibilidade
- ✅ Docstring no padrão Google
- ✅ Validação de entrada com exceções
- ✅ Algoritmo otimizado O(√n)
- ✅ Nomes descritivos de variáveis

#### Uso
```bash
python num_primo.py
```

**Exemplo de Entrada:**
```
Digite um número inteiro para verificar se é primo: 17
O número 17 é primo.
```

#### Como Funciona
1. Define a função `is_prime(n)` que:
   - Valida se `n` é um inteiro
   - Retorna `False` se n ≤ 1
   - Verifica divisibilidade até √n
   - Retorna `True` se não houver divisores

2. Captura entrada do usuário com tratamento de erros
3. Exibe resultado formatado

Para mais detalhes, veja [explicacao_num_primo.md](explicacao_num_primo.md).

---

### 2. **Refatoração de Código** (`refatoracao.py`)

Demonstra como transformar código confuso em código limpo e profissional.

#### Comparação

**Antes (Código Original):**
```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn
```

**Depois (Refatorado):**
```python
def calcular_estatisticas(lista):
    """Calcula e retorna o total, média, maior e menor valor de uma lista de números."""
    total = sum(lista)
    media = total / len(lista)
    maior = max(lista)
    menor = min(lista)
    return total, media, maior, menor
```

#### Melhorias Aplicadas
| Aspecto | Antes | Depois |
|---------|-------|--------|
| Nome da função | `c` | `calcular_estatisticas` |
| Variáveis | `l, t, m, mx, mn` | `lista, total, media, maior, menor` |
| Loops | Manuais `for i in range(len(l))` | Built-in `sum()`, `max()`, `min()` |
| Documentação | Nenhuma | Docstring clara |
| Eficiência | Baixa | Alta |

#### Uso
```bash
python refatoracao.py
```

Para análise completa, consulte [explicacao_refatoracao.md](explicacao_refatoracao.md).

---

### 3. **Programa com Erros** (`debug.py`)

Um sistema de cálculo de carrinhos de compras com **erros intencionais** para fins educacionais.

#### Funcionalidade
Calcula o total de uma compra com:
- 3 produtos com quantidades e preços
- Imposto fixo de 10%
- Desconto por cupom
- Recibo formatado

#### Erros Encontrados

| # | Erro | Localização | Solução |
|---|------|-------------|---------|
| 1 | Falta de aspas em prompt | `item1 = float(input(Preço...` | Adicionar aspas: `input("Preço..."` |
| 2 | F-string não formatada | `print(" Item 2: R$ {total_item2..."` | Adicionar `f`: `print(f"... {total_item2:.2f}"` |
| 3 | Falta de aspas em prompt | `item3 = float(input(Preço...` | Adicionar aspas |
| 4 | String comparada com número | `desconto_cupom = input(...)` sem conversão | Converter: `float(input(...))` |
| 5 | Indentação incorreta | Bloco `if desconto_cupom > 0:` | Corrigir indentação |

#### Uso (Com Erros)
```bash
python debug.py
# Resultado: SyntaxError ou TypeError
```

Para detalhes dos erros, veja [explicacao-debug.md](explicacao-debug.md).

---

## 💡 Conceitos-Chave Abordados

### Clean Code 🧹
- Nomes descritivos para funções e variáveis
- Type hints para clareza de tipos
- Docstrings bem estruturadas
- Validação de entrada

### Refatoração 🔄
- Eliminação de código duplicado
- Uso de funções built-in
- Melhor legibilidade
- Manutenibilidade aumentada

### Tratamento de Erros ⚠️
- Try-except para exceções
- Validação com `isinstance()`
- Mensagens de erro claras
- Robustez do programa

### Algoritmos Eficientes ⚡
- Otimização O(√n) para primalidade
- Uso de built-ins (`sum()`, `max()`, `min()`)
- Redução de complexidade

---

## 🚀 Como Usar

### Pré-requisitos
- Python 3.6+

### Executar Exemplos

**1. Verificar um número primo:**
```bash
python num_primo.py
```

**2. Ver cálculo de estatísticas:**
```bash
python refatoracao.py
```

**3. Tentar executar programa com erros:**
```bash
python debug.py
# Resultará em erro - este é o ponto!
```

---

## 📚 Recursos Educacionais

Cada arquivo Python possui uma documentação correspondente em Markdown:

| Arquivo | Documentação |
|---------|--------------|
| `num_primo.py` | `explicacao_num_primo.md` |
| `refatoracao.py` | `explicacao_refatoracao.md` |
| `debug.py` | `explicacao-debug.md` |

**Dica:** Leia as documentações enquanto estuda o código para melhor compreensão!

---

## 🎓 Aprendizados Principais

✅ **Valide sempre suas entradas**
- Use `isinstance()` para verificações de tipo
- Trate exceções com try-except

✅ **Use nomes descritivos**
- Evite abreviações (`c`, `l`, `t`)
- Use nomes que expliquem a intenção

✅ **Aproveite funções built-in**
- `sum()`, `max()`, `min()` vs. loops manuais
- Melhor performance e legibilidade

✅ **Documente seu código**
- Docstrings descrevem função e parâmetros
- Comentários explicam decisões, não óbvios

✅ **Otimize seus algoritmos**
- O(√n) é melhor que O(n) para primalidade
- Sempre questione a complexidade

---

## 📝 Notas

- Este projeto é **educacional** e visa demonstrar conceitos de programação
- Os erros em `debug.py` são **intencionais** para fins de aprendizado
- Todos os exemplos seguem **PEP 8** (padrão de estilo Python)
- Documentação em **português** para melhor compreensão

---

## 📖 Referências

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

## 🤝 Contribuições

Este é um projeto educacional. Sugestões e melhorias são bem-vindas!

---

**Última atualização:** Abril de 2026  
**Status:** ✅ Completo e Funcional
