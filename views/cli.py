# Comand Line Interface
class CLI:
    def __init__(self):
        
        while True:
            line = input()

            if line == "":
                exit(0)
            
            # "DTL Bob ShoppingList"
            commands = line.split(" ")

            if commands[0] == "CU":
                user_name = commands[1]

            elif commands[0] == "LU":
                pass

            elif commands[0] == "DU":
                user_name = commands[1]

            elif commands[0] == "CTL":
                user_name = commands[1]
                task_list_name = commands[2]

            elif commands[0] == "DTL":
                user_name = commands[1]
                task_list_name = commands[2]

            elif commands[0] == "CT":
                user_name = commands[1]
                task_list_name = commands[2]
                task_id = commands[3]
                task_description = commands[4]

            elif commands[0] == "DT":
                user_name = commands[1]
                task_list_name = commands[2]
                task_id = commands[3]

            elif commands[0] == "ET":
                user_name = commands[1]
                task_list_name = commands[2]
                task_id = commands[3]
                task_description = commands[4]

            elif commands[0] == "LTL":
                user_name = commands[1]

            elif commands[0] == "LTTL":
                user_name = commands[1]
                task_list_name = commands[2]

            elif commands[0] == "CTS":
                user_name = commands[1]
                task_list_name = commands[2]
                task_id = commands[3]

            elif commands[0] == "S":
                filename = commands[1]

            elif commands[0] == "L":
                filename = commands[1]
