import functions as f

def main():

    valid_characters = ['A','C','T','G']
    dna = input("Introdueix el DNA: ")

    f.check_format(dna, valid_characters)

if __name__ == '__main__':
    main()
