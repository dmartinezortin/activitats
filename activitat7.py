import functions as f

def main():

    output = input("Introdueix el missatge")
    output = list(output)
    filter('',output)
    print(output)
if __name__ == '__main__':
    main()
