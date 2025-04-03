salario = float(input("Salário fixo: "))
horas_extra = float(input("Horas extras: "))
valor_hora_extra = float(input("Valor por horas extras: "))
salario_total = salario + horas_extra*valor_hora_extra
print(f"Salário: R${salario_total}")