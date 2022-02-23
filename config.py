def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el documento config.txt!")

if __name__ == '__main__':
    main()