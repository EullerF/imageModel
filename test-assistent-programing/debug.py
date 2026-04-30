#                                      CÓDIGO COM ERROS                           
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
# Calcula o total de cada item antes de compor o subtotal
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

# Subtotal é a soma dos totais individuais de cada produto
subtotal = total_item1 + total_item2 + total_item3
# Imposto fixo de 10% sobre o subtotal, usado para compor o total final
imposto = subtotal * 0.10  # Calcula o imposto de 10% sobre o subtotal

# DESCONTO
# Lê o percentual do cupom; 0 indica ausência de desconto
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
# Converte o percentual em valor absoluto de desconto sobre o subtotal
desconto = subtotal * (desconto_cupom / 100)  # Aplica desconto percentual ao subtotal

# TOTAL FINAL
total = subtotal + imposto - desconto  # Total final após adicionar imposto e subtrair desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# Exibe desconto apenas se o percentual informado for maior que zero
if desconto_cupom > 0:  # Só exibe desconto se houver cupom
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
# Usa round para garantir formatação correta do total final
print(f" TOTAL:         R$ {round(total, 2):.2f}")  # Arredonda para 2 casas decimais antes de formatar
print(linha)