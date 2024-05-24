import os

# a lista de tarefas
tarefas = []

while True:
    # informa o nome da nova fruta 
    nova_tarefa = input('\nInsira o nome da nova tarefa: ').upper()

    if nova_tarefa !='':
    # adiciona o item na lista
        tarefas.append(nova_tarefa)
        continue
    else:
        break

os.system('cls')

# print(f'{'-'*30} LISTA DE TAREFAS {'-'*30}\n')
print(f'LISTA DE TAREFAS')

# exibe a lista ao final
for tarefa in tarefas:
    print(tarefa)