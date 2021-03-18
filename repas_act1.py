import functions as f

def main():
    main_dict = dict()
    total = 0

    while total < 1:
        total = int(input("Quants vols introduir? "))

    main_dict = f.insert_dictionary(main_dict, total)
    f.print_dict(main_dict)

if __name__ == '__main__':
        main()