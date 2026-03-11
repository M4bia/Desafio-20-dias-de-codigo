nome = input()
salario_fixo = float(input())
total_vendas = float(input())

comissao = total_vendas * 0.15
total = salario_fixo + comissao

print("TOTAL = R$ {:.2f}".format(total))