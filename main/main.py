from logic.logic import *
import copy
from user_interface.user_interface import *
from tests.tests import test_all


def start():
    librarie = create_librarie()

    while True:
        print_menu()

        operation = input('command> ')

        try:
            if operation == '1':
                t_id, title, genre, price, discount_type = get_insert_transaction_data()
                add_transaction(get_lista_curenta(librarie), t_id, title, genre, price, discount_type)
            elif operation == '2':
                t_id = get_delete_transaction_data()
                delete_transaction(get_lista_curenta(librarie), t_id)
            elif operation == '3':
                t_id, genre = get_change_genre_data()
                change_genre(get_lista_curenta(librarie), t_id, genre)
            elif operation == '4':
                filtered_list = get_each_min_price(get_lista_curenta(librarie))
                print_genre_min_price(filtered_list)
            elif operation == '5':
                ordered_list = get_ordered_list(get_lista_curenta(librarie))
                print_transactions(ordered_list)
            elif operation == '6':
                computed_list = get_distinct_genre_titles(get_lista_curenta(librarie))
                print_number_distinct_genre_titles(computed_list)
            elif operation == '7':
                print_transactions(get_lista_curenta(librarie))
            elif operation == '8':
                undo_operation(librarie)
            elif operation == '9':
                redo_operation(librarie)
            elif operation == '10':
                return
            else:
                print('Optiune invalida')

            save_transactions_list(librarie)
        except ValueError:
            print_invalid_input()
        except AssertionError:
            print_invalid_input()
        except KeyError as ke:
            print(ke)


test_all()
start()
