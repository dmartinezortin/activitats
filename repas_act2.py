import functions as f
MIN = 1
MAX = 145
def main():

    main_list = f.generate_list(MIN, MAX)
    print(main_list[5:])

if __name__ == '__main__':
    main()
