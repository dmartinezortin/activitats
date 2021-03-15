def request_values():
    aux_list = list()
    value = ''
    while value != "#":
        value = input("Introdueix un valor(# per finalitzar): ")
        if value != "#":
            aux_list.append(int(value))

    return aux_list


def main():

    main_list = request_values()

    print(sum(main_list))

if __name__ == '__main__':
    main()

