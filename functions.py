def welcome_menu():
    print("╔════════════════════════════╗\n║         MAIN MENU          ║\n╚════════════════════════════╝")

#Demana un numero del 1 al 10
def request_num():

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

