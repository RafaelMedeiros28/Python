valor = float(input("Dígite o valor em Reais: R$"))

dolar = valor / 5.29
euro = valor / 5.62

print(f'R${valor:.2f} em Dólar é igual a US${dolar:.2f}')
print(f'R${valor:.2f} em Euros é igual a €{euro:.2f}')