valor = float(input("Dígite o valor em Reais: R$"))

dolar = valor / 5.29 #Cotação de 16/04/2024
euro = valor / 5.62 #Cotação de 16/04/2024

print(f'R${valor:.2f} em Dólar é igual a US${dolar:.2f}')
print(f'R${valor:.2f} em Euros é igual a €{euro:.2f}')

    #Feito por Rafael Medeiros.