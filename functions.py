def welcome_menu():
    print("╔════════════════════════════╗\n║         MAIN MENU          ║\n╚════════════════════════════╝")

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

def check_format(dna):
    valid_characters = ['A','C','T','G']
    count = 0
    size = len(dna)
    dna = list(dna.upper())
    for x in dna:
        if x in valid_characters:
            count += 1
    if size == count:
        print("El format de la seqüencia és vàlida!")
    else:
        print("El format de la seqüencia no és vàlida!")

def greater(main_list):
    greater_value = main_list[0]
    for x in main_list:
        if x > greater_value:
            greater_value = x
    return greater_value

def lower(main_list):
    lower_value = main_list[0]
    for x in main_list:
        if x < lower_value:
            lower_value = x
    return lower_value
