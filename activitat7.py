import functions as f

def main():

    output = input("Introdueix el missatge: ").split()
    f.check_user(output)
    f.check_perms(output)
    f.check_filename(output)
    print(output[3], "es el grup d'usuari")

if __name__ == '__main__':
    main()
