from stdnum import iban

def main():
    tilinumero = input("Anna IBAN-tilinumero: ")
    on_oikea_iban = iban.is_valid(tilinumero)
    if on_oikea_iban:
        print(f"Antamasi tilinumero '{tilinumero}' on oikea IBAN. ")
    else:
        print(f"Antamasi tilinumero '{tilinumero}' ei ole IBAN")


if __name__ == '__main__':
    main()