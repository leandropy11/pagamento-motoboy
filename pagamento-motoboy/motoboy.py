#Desenvolvido por: Leandro Marques de Assis
#Contato: leandrmarquesassis1407@gmail.com ou (21)96773-9408
'''O código abaixo foi criado para facilitar e agilizar o pagamento dos Motoboys do delivery.
Vale lembrar que ele é baseado no método de pagamento (valores) da loja que eu trabalhei, Marcos é o único motoboy com uma condição especial
que fazia ele receber R$10,00 a mais como extra, por isso a pergunta no input e em caso de retorno positivo o uso da variável "extra"'''
#Motoboy 1
print('Motoboy 1: ')
motoboy1 = str(input('O motoboy 1 é o Marcos?'))
if motoboy1 == 'sim':
        totentregas1 = int(input('Qual foi o total de entregas? '))
        entrega1 = int(input('Quantas entregas de R$20,00? '))
        entrega2 = int(input('Quantas entregas de R$15,00? '))
        entrega3 = int(input('Quantas entregas de R$8,00? '))
        entrega4 = int(input('Quantas entregas de R$6,50? '))
        tottaxa1 = (entrega1 * 17.50) + (entrega2 * 12.50) + (entrega3 * 5.50) + (entrega4 * 5)
        diariamotoboy1 = float(tottaxa1 + 80 + 10)
        print('O total de taxa paga ao Motoboy 1 é: R${:.2f}'.format(tottaxa1))
        print('O pagamento do Motoboy 1 com taxa (R${:.2f}), diária (R${:.2f}) e extra (R${:.2f}) é: R${:.2f}'.format(tottaxa1, 80, 10, diariamotoboy1))
else:
        totentregas1 = int(input('Qual foi o total de entregas? '))
        entrega1 = int(input('Quantas entregas de R$20,00? '))
        entrega2 = int(input('Quantas entregas de R$15,00? '))
        entrega3 = int(input('Quantas entregas de R$8,00? '))
        entrega4 = int(input('Quantas entregas de R$6,50? '))
        tottaxa1 = (entrega1 * 17.50) + (entrega2 * 12.50) + (entrega3 * 5.50) + (entrega4 * 5)
        diariamotoboy1 = float(tottaxa1 + 80)
        print('O total de taxa paga ao Motoboy 1 é: R${:.2f}'.format(tottaxa1))
        print('O pagamento do Motoboy 1 com taxa (R${:.2f}) e diária (R${:.2f}) é: R${:.2f}'.format(tottaxa1, 80, diariamotoboy1))
print('Motoboy 2: ')
motoboy2 = str(input('O motoboy 2 é o Marcos?' ))
if motoboy2 == 'sim':
        totentregas2 = int(input('Qual foi o total de entregas? '))
        entrega5 = int(input('Quantas entregas de R$20,00? '))
        entrega6 = int(input('Quantas entregas de R$15,00? '))
        entrega7 = int(input('Quantas entregas de R$8,00? '))
        entrega8 = int(input('Quantas entregas de R$6,50? '))
        tottaxa2 = (entrega5 * 17.50) + (entrega6 * 12.50) + (entrega7 * 5.50) + (entrega8 * 5)
        diariamotoboy2 = float(tottaxa2 + 40 + 10)
        print('O total de taxa paga ao Motoboy 2 é: R${:.2f}'.format(tottaxa2))
        print('O pagamento do Motoboy 2 com taxa ({:.2f}), diária ({:.2f}) e extra ({:.2f})é: R${:.2f}'.format(tottaxa2, 40, 10, diariamotoboy2))
else:
        totentregas2 = int(input('Qual foi o total de entregas? '))
        entrega5 = int(input('Quantas entregas de R$20,00? '))
        entrega6 = int(input('Quantas entregas de R$15,00? '))
        entrega7 = int(input('Quantas entregas de R$8,00? '))
        entrega8 = int(input('Quantas entregas de R$6,50? '))
        tottaxa2 = (entrega5 * 17.50) + (entrega6 * 12.50) + (entrega7 * 5.50) + (entrega8 * 5)
        diariamotoboy2 = float(tottaxa2 + 40)
        print('O total de taxa paga ao Motoboy 2 é: R${:.2f}'.format(tottaxa2))
        print('O pagamento do Motoboy 2 com taxa ({:.2f}) e diária ({:.2f}) é: R${:.2f}'.format(tottaxa2, 40, diariamotoboy2))
print(input('Digite algo para finalizar o programa'))