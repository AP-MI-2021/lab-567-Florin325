from domain.domain import *


def print_menu():
    print('1. Adaugare tranzactie')
    print('2. Stergere tranzactie')
    print('3. Modificare gen tranzactie')
    print('4. Determinare pret minim pentru fiecare gen')
    print('5. Ordonare tranzactii crescator dupa pret')
    print('6. Afisare numar de titluri distincte pentru fiecare gen')
    print('7. Afiseaza toate tranzactiile')
    print('8. Undo')
    print('9. Redo')
    print('10. Iesire')


def print_invalid_input():
    print('Date incorecte!')


def get_insert_transaction_data():
    t_id = input('ID-ul tranzactiei: ')
    title = input('Titlul cartii: ')
    genre = input('Genul cartii: ')
    price = input('Pretul cartii: ')
    discount_type = input('Tip reducere client: ')

    return t_id, title, genre, price, discount_type


def get_delete_transaction_data():
    t_id = input('ID-ul tranzactiei care sa fie stearsa: ')

    return t_id


def get_change_genre_data():
    t_id = input('ID-ul tranzactiei: ')
    new_genre = input('Noul gen: ')

    return t_id, new_genre


def print_genre_min_price(filtered_list):
    for entry in filtered_list:
        print(entry, filtered_list[entry])


def display_transaction(entry):
    print('ID:', get_id(entry),
          '| Titlu:', get_title(entry),
          '| Gen:', get_genre(entry),
          '| Pret:', get_price(entry),
          '| Tip reducere:', get_discount_type(entry))


def print_transactions(ordered_list):
    for entry in ordered_list:
        display_transaction(entry)


def print_number_distinct_genre_titles(computed_list):
    for entry in computed_list:
        print(entry, len(computed_list[entry]))
