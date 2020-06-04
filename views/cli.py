from controllers.task_list_controller import TaskListController

# Comand Line Interface
class CLI:
    def __init__(self):
        controller = TaskListController()

        while True:
            line = input()

            if line == "":
                exit(0)
            
            commands = line.split(" ")

            if commands[0] == "CU":
                user_name = commands[1]
                if controller.has_user(user_name):
                    print("Utilizador existente.")
                else:
                    controller.create_user(user_name)
                    print("Utilizador registado com sucesso.")

            elif commands[0] == "LU":
                if controller.has_users():
                    print("Sem utilizadores registados.")
                else:
                    ## lista de nomes de utilizadores
                    # user_names = controller.get_users()
                    # it = user_names.iterator()
                    # while it.has_next():
                    #     print(it.get_next())
                    
                    # lista de utilizadores
                    users = controller.get_users()
                    it = users.iterator()
                    while it.has_next():
                        print(it.get_next().get_name())

            elif commands[0] == "DU":
                user_name = commands[1]
                if not controller.has_user(user_name):
                    print("Utilizador inexistente.")
                else:
                    controller.remove_user(user_name)
                    print("Utilizador removido com sucesso.")
                
            elif commands[0] == "CTL":
                user_name = commands[1]
                task_list_name = commands[2]
                if not controller.has_user(user_name):
                    print("Utilizador inexistente.")
                elif controller.has_task_list(user_name, task_list_name):
                    print("Lista de tarefas existente.")
                else:
                    controller.create_task_list(user_name, task_list_name)
                    print("Lista de tarefas criada com sucesso.")

            elif commands[0] == "DTL":
                user_name = commands[1]
                task_list_name = commands[2]
                if not controller.has_user(user_name):
                    print("Utilizador inexistente.")
                elif not controller.has_task_list(user_name, task_list_name):
                    print("Lista de tarefas inexistente.")
                else:
                    controller.remove_task_list(user_name, task_list_name)
                    print("Lista de tarefas eliminada com sucesso.")

            elif commands[0] == "CT":
                user_name = commands[1]
                task_list_name = commands[2]
                task_id = commands[3]
                task_description = commands[4]
                if not controller.has_user(user_name):
                    print("Utilizador inexistente.")
                elif not controller.has_task_list(user_name, task_list_name):
                    print("Lista de tarefas inexistente.")
                elif controller.has_task(user_name, task_list_name, task_id):
                    print("Tarefa existente.")
                else:
                    controller.create_task(user_name, task_list_name, task_id, task_description)
                    print("Tarefa criada com sucesso.")

            elif commands[0] == "DT":
                user_name = commands[1]
                task_list_name = commands[2]
                task_id = commands[3]
                if not controller.has_user(user_name):
                    print("Utilizador inexistente.")
                elif not controller.has_task_list(user_name, task_list_name):
                    print("Lista de tarefas inexistente.")
                elif not controller.has_task(user_name, task_list_name, task_id):
                    print("Tarefa inexistente.")
                else:
                    controller.remove_task(user_name, task_list_name, task_id)
                    print("Tarefa eliminada com sucesso.")

            elif commands[0] == "ET":
                user_name = commands[1]
                task_list_name = commands[2]
                task_id = commands[3]
                task_description = commands[4]
                if not controller.has_user(user_name):
                    print("Utilizador inexistente.")
                elif not controller.has_task_list(user_name, task_list_name):
                    print("Lista de tarefas inexistente.")
                elif not controller.has_task(user_name, task_list_name, task_id):
                    print("Tarefa inexistente.")
                else:
                    controller.edit_task(user_name, task_list_name, task_id, task_description)
                    print("Tarefa alterada com sucesso.")

            elif commands[0] == "LTL":
                user_name = commands[1]
                if not controller.has_user(user_name):
                    print("Utilizador inexistente.")
                elif not controller.has_task_lists(user_name):
                    print("Utilizador sem lista de tarefas.")
                else:
                    task_lists = controller.get_task_lists(user_name)
                    it = task_lists.iterator()
                    while it.has_next():
                        print(it.get_next().get_name()) 

            elif commands[0] == "LTTL":
                user_name = commands[1]
                task_list_name = commands[2]
                if not controller.has_user(user_name):
                    print("Utilizador inexistente.")
                elif not controller.has_task_lists(user_name):
                    print("Utilizador sem lista de tarefas.")
                elif not controller.has_task_list(user_name, task_list_name):
                    print("Lista de tarefas inexistente.")
                elif not controller.has_tasks(user_name, task_list_name):
                    print("Lista de tarefas sem tarefas.")
                else:
                    tasks = controller.get_tasks(user_name, task_list_name)
                    it = tasks.iterator()
                    while it.has_next():
                        task = it.get_next() 
                        print(f"{task.get_id()} - {task.get_state()} - {task.get_description()}")

            elif commands[0] == "CTS":
                user_name = commands[1]
                task_list_name = commands[2]
                task_id = commands[3]
                if not controller.has_user(user_name):
                    print("Utilizador inexistente.")
                elif not controller.has_task_list(user_name, task_list_name):
                    print("Lista de tarefas inexistente.")
                elif not controller.has_task(user_name, task_list_name, task_id):
                    print("Tarefa inexistente.")
                else:
                    controller.toggle_task(user_name, task_list_name, task_id)
                    print("Estado de tarefa alterado com sucesso.")

            elif commands[0] == "S":
                filename = commands[1]

            elif commands[0] == "L":
                filename = commands[1]
