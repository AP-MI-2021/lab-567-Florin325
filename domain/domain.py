import copy


def create_transaction(t_id, title, genre, price, discount_type):
    """
    Functia creeaza un dictionar continand detaliile unei tranzactii
    :param t_id: ID-ul tranzactiei
    :param title: Titlul cartii
    :param genre: Genul cartii
    :param price: Pretul cartii
    :param discount_type: Tipul de reducere client
    :return: un dictionar continand detaliile tranzactiei
    """

    return {
        'id': t_id,
        'title': title,
        'genre': genre,
        'price': price,
        'discount_type': discount_type
    }


def create_librarie():
    return {
        'listaCurenta': [],
        'listaUndo': [[]],
        'listaRedo': []
    }


# Getters and setters


def get_id(trans):
    return trans['id']


def get_title(trans):
    return trans['title']


def get_genre(trans):
    return trans['genre']


def get_price(trans):
    return trans['price']


def get_discount_type(trans):
    return trans['discount_type']


def set_genre(trans, val):
    trans['genre'] = val


# Chestii pentru undo si redo


def get_lista_curenta(librarie):
    return librarie['listaCurenta']


def get_lista_undo(librarie):
    return librarie['listaUndo']


def get_lista_redo(librarie):
    return librarie['listaRedo']


def set_lista_curenta(librarie, newCurrentList):
    librarie['listaCurenta'] = newCurrentList


def adaugare_lista_undo(librarie):
    listaCurenta = get_lista_curenta(librarie)
    get_lista_undo(librarie).append(copy.deepcopy(listaCurenta))


def adaugare_lista_redo(librarie):
    listaCurenta = get_lista_curenta(librarie)
    get_lista_redo(librarie).append(copy.deepcopy(listaCurenta))


def clear_redo(librarie):
    get_lista_redo(librarie).clear()


def adaugare_lista_undo_and_clear_redo(librarie):
    adaugare_lista_undo(librarie)
    clear_redo(librarie)

