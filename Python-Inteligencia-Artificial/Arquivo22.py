funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carros = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#Funcionários que tem carro e trabalha a noite
print(set(tem_carros).intersection(turno_noite))

#Funcionários que tem carro e trabalha durante o dia
print(set(tem_carros).intersection(turno_dia))

#Funcionarios que trabalha e não tem carro
print(set(funcionarios).difference(tem_carros))