def welcome_menu():
    print("╔════════════════════════════════════════════════════════════╗\n"
          "║   _____         .__            _____                       ║\n"
          "║  /     \ _____  |__| ____     /     \   ____   ____  __ __ ║\n"
          "║ /  \ /  \ __  \ |  |/    \   /  \ /  \_/ __ \ /    \|  |  \║\n"
          "║/    Y    \/ __ \|  |   |  \ /    Y    \  ___/|   |  \  |  /║\n"
          "║\____|__  (____  /__|___|  / \____|__  /\___  >___|  /____/ ║\n"
          "║        \/     \/        \/          \/     \/     \/       ║\n"
          "║                                                            ║\n"
          "╚════════════════════════════════════════════════════════════╝")


#Demana un numero del 1 al 10
def request_value():

    value = int(input("Introdueix un numero del 1 al 20: "))
    while value >= 20 or value <= 1:
        value = int(input("Introdueix un numero del 1 al 20: "))
    return value

#Printa els multiples d'un numero fins arribar a 100
def print_multiple(n):
    print([n * x for x in range(100) if (n * x) < 100])

#Quita valors repetits d'una llista
def remove_repeated(a):

    aux = list()
    for x in a:
        if x not in aux:
            aux.append(x)
    return aux

# Demana valors fins rebre un #
def request_values():
    aux_list = list()
    value = ''
    while value != "#":
        value = input("Introdueix un valor(# per finalitzar): ")
        if value != "#":
            aux_list.append(int(value))

    return aux_list

#Comprova si el DNA te un format correcte.

def check_format(string_to_validate, valid_characters):
    count = 0
    size = len(string_to_validate)
    dna = list(string_to_validate.upper())
    for x in string_to_validate:
        if x in valid_characters:
            count += 1
    if size == count:
        print("El format de la seqüencia és vàlida!")
    else:
        print("El format de la seqüencia no és vàlida!")
#Recoge el valor mas grande de una lista
def greater(main_list):
    greater_value = main_list[0]
    for x in main_list:
        if x > greater_value:
            greater_value = x
    return greater_value
#Recoge el valor mas pequeño de una lista
def lower(main_list):
    lower_value = main_list[0]
    for x in main_list:
        if x < lower_value:
            lower_value = x
    return lower_value

def check_user(main_list):
    username = input("Quin es el teu usuari?")
    if username == main_list[2]:
        print("L'usuari coincideix.")
    else:
        print("L'usuari no coincideix.")

def check_perms(main_list):
    perms = main_list[0]
    #Comprova permisos de lectura de usuari
    if perms[1] == 'r':
        print("L'usuari té permisos de lectura")
    else:
        print("/!\ L'usuari no te permisos de lectura")
    #Comprova permisos de escritura de usuari
    if perms[2] == 'w':
        print("L'usuari te permisos de escritura")
    else:
        print("/!\ L'usuari no te permisos de lectura")
    if perms[3] == 'x':
        print("L'usuari te permisos de execució")
    else:
        print("/!\ L'usuari no te permisos de execució")
    if perms[4] == 'r':
        print("El grup te permisos de lectura")
    else:
        print("/!\ El grup no te permisos de lectura")
    #Comprova permisos de escritura de usuari
    if perms[4] == 'w':
        print("El grup te permisos de escritura")
    else:
        print("/!\ El grup no te permisos de lectura")
    if perms[6] == 'x':
        print("El grup te permisos de execució")
    else:
        print("/!\ El grup no te permisos de execució")

def check_filename(main_list):
    filename = input("Quin es el nom del fitxer per revisar permisos: ")
    if filename == main_list[-1]:
        print("El nom del fitxer coincideix")
    else:
        print("/!\ El nom del fitxer no coincideix")

def insert_dictionary(main_dict, total):
    for x in range(total):
        student_id = 0
        while student_id < 1:
            student_id = int(input("ID de l'estudiant? "))
        name = input("Quin es el nom de l'alumne? ")
        last_name = input("Quin es el cognom de l'alumne? ")
        subject = input("Quina es la materia de l'alumne? ")
        grade = input("Quina es la nota de l'alumne? ")
        aux_dict = {x:
                        {'Student_ID': student_id,
                        'first_name': name,
                        'last_name': last_name,
                        'subject': subject,
                        'grade': grade}
                    }
        main_dict.update(aux_dict)
        print(main_dict)
    return main_dict

def print_dict(main_dict):
    print("student_id", "first_name", "last_name", "subject", "grade")
    for key, value in main_dict.items():
        for x, y in value.items():
            print(y, "\t\t", end='')
        print()

def generate_list(min, max):
    generated_list = list([x* 2 if x%2 == 0 else x//5 for x in range(min, max+1)])
    return generated_list
