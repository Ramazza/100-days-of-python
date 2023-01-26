print('Bem vindo ao Tip Calculator.')
valor_total = input('Qual foi o valor total da conta? R$ ')
num_pessoas = input('Com quantas pessoas a conta vai ser dividida? ')
percentual = input('Qual o percentual de gorjeta que será utilizado? ')

gorjeta = ((float(percentual) / 100) * float(valor_total)) / float(num_pessoas)

valor_a_pagar = float(valor_total) / int(num_pessoas)

print(f'Cada pessoa deverá pagar: R$ {round(gorjeta + valor_a_pagar, 2)}')
