def remove_repeated(a):
    aux = list()
    for x in a:
        if x not in aux:
            aux.append(x)
    return aux

def main():

    a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

    a = remove_repeated(a)
    print(a)

if __name__ == '__main__':
    main()

