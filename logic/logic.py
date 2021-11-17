
from domain.domain import *


def add_transaction(tr_list, t_id, title, genre, price, discount_type):
    """
    Adauga o tranzactie noua in lista de tranzactii
    :param tr_list: Lista de tranzactii
    :param t_id: ID-ul tranzactiei
    :param title: Titlul cartii
    :param genre: Genul cartii
    :param price: Pretul cartii
    :param discount_type: Tip reducere
    :return: eroare daca datele nu sunt bune
    """
    try:
        t_id = int(t_id)
        assert title is not None
        assert genre is not None
        price = float(price)
        assert discount_type in ['none', 'silver', 'gold']
    except ValueError as ve:
        raise ve
    except AssertionError as ae:
        raise ae

    if discount_type == 'silver':
        price = price - 5 * price / 100
    elif discount_type == 'gold':
        price = price - price / 10

    for trans in tr_list:
        if get_id(trans) == t_id:
            raise KeyError('Deja exista o tranzactie cu acest ID')

    tr_list.append(create_transaction(t_id, title, genre, price, discount_type))


def delete_transaction(transactions, t_id):
    """
    Sterge o tranzactie din lista de tranzactii
    :param transactions: Lista de tranzactii
    :param t_id: ID_ul tranzactiei
    :return: eroare daca datele nu sunt bune
    """
    try:
        t_id = int(t_id)
    except ValueError as ve:
        raise ve

    for trans in transactions:
        if get_id(trans) == t_id:
            transactions.remove(trans)
            return


def change_genre(transactions, t_id, genre):
    """
    Schimba genul unei carti dintr-o tranzactie
    :param transactions: Lista de tranzactii
    :param t_id: ID-ul tranzactiei
    :param genre: Genul nou
    :return: eroare daca datele nu sunt bune
    """
    try:
        t_id = int(t_id)
        assert genre is not None
    except ValueError as ve:
        raise ve
    except AssertionError as ae:
        raise ae

    for trans in transactions:
        if get_id(trans) == t_id:
            set_genre(trans, genre)
            return


def get_each_min_price(transactions):
    """
    Compune un dictionar in care se retine pt fiecare gen pretul minim al unei carti
    :param transactions: Lista de tranzactii
    :return: dictionarul creat
    """
    computed_list = {}

    for trans in transactions:
        if not get_genre(trans) in computed_list.keys():
            computed_list[get_genre(trans)] = get_price(trans)
        else:
            computed_list[get_genre(trans)] = min(computed_list[get_genre(trans)], get_price(trans))

    return computed_list


def get_ordered_list(transactions):
    """
    :param transactions: Lista de tranzactii
    :return: o lista de tranzactii sortata crescator dupa pret
    """
    return sorted(transactions, key=get_price)


def get_distinct_genre_titles(transactions):
    """
    Compune un dictionar in care se retine pt fiecare gen ce carti sunt
    :param transactions: Lista de tranzactii
    :return: dictionarul creat
    """
    computed_list = {}

    for trans in transactions:
        if not get_genre(trans) in computed_list.keys():
            computed_list[get_genre(trans)] = [get_title(trans)]
        elif not get_title(trans) in computed_list[get_genre(trans)]:
            computed_list[get_genre(trans)].append(get_title(trans))

    return computed_list


def undo_operation(librarie):
    """
    Restaureaza penultima lista de tranzactii
    :param librarie: libraria in care sunt retinute listele de tranzactii, de undo si de redo
    :return: nothing
    """
    lista_undo = get_lista_undo(librarie)

    if len(lista_undo) > 1:
        adaugare_lista_redo(librarie)
        lista_undo.pop()
        set_lista_curenta(librarie, copy.deepcopy(lista_undo[-1]))
    else:
        set_lista_curenta(librarie, [])


def redo_operation(librarie):
    lista_redo = get_lista_redo(librarie)

    if len(lista_redo) > 0:
        adaugare_lista_undo(librarie)
        set_lista_curenta(librarie, copy.deepcopy(lista_redo[-1]))
        lista_redo.pop()


def save_transactions_list(librarie):
    """
    Adauga lista curenta de tranzactii in lista istoricului de tranzactii
    :param librarie: libraria in care sunt retinute listele de tranzactii, de undo si de redo
    :return: nimic
    """
    list_history = get_lista_undo(librarie)
    transactions_list = get_lista_curenta(librarie)

    pairs = zip(list_history[-1], transactions_list)

    if len(list_history[-1]) != len(transactions_list) or any(x != y for x, y in pairs):
        adaugare_lista_undo_and_clear_redo(librarie)
