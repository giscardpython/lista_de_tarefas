
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

# exibe a lista ao final
print('\nLista de Tarefas do dia: ')
for tarefa in tarefas:
    print(tarefa)