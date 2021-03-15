def request_num():
    value = int(input("Introdueix un numero del 1 al 20: "))
    while value >= 20 or value <= 1:
        value = int(input("Introdueix un numero del 1 al 20: "))
    return value


def print_multiple(n):
    print([n * x for x in range(100) if (n * x) < 100])


def main():

    n = request_num()
    print_multiple(n)

if __name__ == '__main__':
    main()
