import functions as f

def main():
    llista = [5, 10, 15, 2, 25, 30, 35, 40]
    value1 = f.greater(llista)
    value2 = f.lower(llista)
    print("El valor mes gran es ", value1, "I el mes petit es ", value2)

if __name__ == '__main__':
    main()
