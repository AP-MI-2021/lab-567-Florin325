from logic.logic import *


def test_all():
    test_add_transaction()
    test_undo_redo()
    test_change_genre()
    test_get_each_min_price()
    test_get_ordered_list()
    test_get_distinct_genre_titles()
    test_delete_transaction()
    test_program()


def test_add_transaction():
    librarie = create_librarie()
    add_transaction(get_lista_curenta(librarie), '1', 'dss', 'dsdsd', '1', 'gold')

    try:
        add_transaction(get_lista_curenta(librarie), '1', 'dss', 'dsdsd', '2', 'gold')
    except (ValueError, AssertionError, KeyError):
        pass

    try:
        add_transaction(get_lista_curenta(librarie), '1', 'dss', 'dsdsd', '3', 'fdfef')
    except (ValueError, AssertionError, KeyError):
        pass

    try:
        add_transaction(get_lista_curenta(librarie), '1', 'dss', 'dsdsd', 'dfdf', 'fdfef')
    except (ValueError, AssertionError, KeyError):
        pass

    assert get_lista_curenta(librarie) == [create_transaction(1, 'dss', 'dsdsd', 0.9, 'gold')]


def test_undo_redo():
    librarie = create_librarie()
    add_transaction(get_lista_curenta(librarie), 65, 'awfda', 'afaddf', 34, 'gold')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 46, 'shfhd', 'jsqea', 42, 'silver')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 57, 'tregs', 'sgsdg', 23, 'silver')
    save_transactions_list(librarie)

    change_genre(get_lista_curenta(librarie), 65, 'newg')
    save_transactions_list(librarie)

    undo_operation(librarie)

    assert get_lista_curenta(librarie) == [create_transaction(65, 'awfda', 'afaddf', 30.6, 'gold'),
                                           create_transaction(46, 'shfhd', 'jsqea', 39.9, 'silver'),
                                           create_transaction(57, 'tregs', 'sgsdg', 21.85, 'silver')]

    redo_operation(librarie)

    assert get_lista_curenta(librarie) == [create_transaction(65, 'awfda', 'newg', 30.6, 'gold'),
                                           create_transaction(46, 'shfhd', 'jsqea', 39.9, 'silver'),
                                           create_transaction(57, 'tregs', 'sgsdg', 21.85, 'silver')]


def test_change_genre():
    librarie = create_librarie()
    add_transaction(get_lista_curenta(librarie), 65, 'awfda', 'afaddf', 34, 'gold')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 46, 'shfhd', 'jsqea', 42, 'silver')
    save_transactions_list(librarie)

    change_genre(get_lista_curenta(librarie), 65, 'abc')

    assert get_lista_curenta(librarie) == [create_transaction(65, 'awfda', 'abc', 30.6, 'gold'),
                                           create_transaction(46, 'shfhd', 'jsqea', 39.9, 'silver')]


def test_get_each_min_price():
    librarie = create_librarie()
    add_transaction(get_lista_curenta(librarie), 65, 'awfda', 'afaddf', 34, 'gold')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 46, 'shfhd', 'jsqea', 42, 'silver')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 54, 'awf', 'afaddf', 30, 'none')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 12, 'fda', 'afaddf', 40, 'silver')
    save_transactions_list(librarie)

    assert get_each_min_price(get_lista_curenta(librarie)) == {'afaddf': 30.0, 'jsqea': 39.9}


def test_get_ordered_list():
    librarie = create_librarie()
    add_transaction(get_lista_curenta(librarie), 65, 'awfda', 'afaddf', 34, 'gold')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 46, 'shfhd', 'jsqea', 42, 'silver')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 54, 'awf', 'afaddf', 30, 'none')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 12, 'fda', 'afaddf', 40, 'silver')
    save_transactions_list(librarie)

    assert get_ordered_list(get_lista_curenta(librarie)) == [
        create_transaction(54, 'awf', 'afaddf', 30, 'none'),
        create_transaction(65, 'awfda', 'afaddf', 30.6, 'gold'),
        create_transaction(12, 'fda', 'afaddf', 38, 'silver'),
        create_transaction(46, 'shfhd', 'jsqea', 39.9, 'silver')
    ]


def test_get_distinct_genre_titles():
    librarie = create_librarie()
    add_transaction(get_lista_curenta(librarie), 65, 'awfda', 'afaddf', 34, 'gold')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 46, 'shfhd', 'jsqea', 42, 'silver')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 54, 'awf', 'afaddf', 30, 'none')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 12, 'fda', 'afaddf', 40, 'silver')
    save_transactions_list(librarie)

    assert get_distinct_genre_titles(get_lista_curenta(librarie)) == {'afaddf': ['awfda', 'awf', 'fda'],
                                                                      'jsqea': ['shfhd']}


def test_delete_transaction():
    librarie = create_librarie()
    add_transaction(get_lista_curenta(librarie), 65, 'awfda', 'afaddf', 34, 'gold')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 46, 'shfhd', 'jsqea', 42, 'silver')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 54, 'awf', 'afaddf', 30, 'none')
    save_transactions_list(librarie)
    add_transaction(get_lista_curenta(librarie), 12, 'fda', 'afaddf', 40, 'silver')
    save_transactions_list(librarie)

    delete_transaction(get_lista_curenta(librarie), 46)

    assert get_lista_curenta(librarie) == [create_transaction(65, 'awfda', 'afaddf', 30.6, 'gold'),
                                           create_transaction(54, 'awf', 'afaddf', 30, 'none'),
                                           create_transaction(12, 'fda', 'afaddf', 38, 'silver')
                                           ]


def test_program():
    librarie = create_librarie()

    add_transaction(get_lista_curenta(librarie), 1, 't1', 'g1', 10, 'none')
    save_transactions_list(librarie)

    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none')]
    add_transaction(get_lista_curenta(librarie), 2, 't2', 'g2', 20, 'none')
    save_transactions_list(librarie)

    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(2, 't2', 'g2', 20, 'none')]
    add_transaction(get_lista_curenta(librarie), 3, 't3', 'g3', 30, 'none')
    save_transactions_list(librarie)

    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(2, 't2', 'g2', 20, 'none'),
                                           create_transaction(3, 't3', 'g3', 30, 'none')]
    undo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(2, 't2', 'g2', 20, 'none')]
    undo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none')]
    undo_operation(librarie)

    assert get_lista_curenta(librarie) == []

    undo_operation(librarie)
    assert get_lista_curenta(librarie) == []

    add_transaction(get_lista_curenta(librarie), 1, 't1', 'g1', 10, 'none')
    save_transactions_list(librarie)

    add_transaction(get_lista_curenta(librarie), 2, 't2', 'g2', 20, 'none')
    save_transactions_list(librarie)

    add_transaction(get_lista_curenta(librarie), 3, 't3', 'g3', 30, 'none')
    save_transactions_list(librarie)

    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(2, 't2', 'g2', 20, 'none'),
                                           create_transaction(3, 't3', 'g3', 30, 'none')]

    redo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(2, 't2', 'g2', 20, 'none'),
                                           create_transaction(3, 't3', 'g3', 30, 'none')]

    undo_operation(librarie)
    undo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none')]

    redo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(2, 't2', 'g2', 20, 'none')]

    redo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(2, 't2', 'g2', 20, 'none'),
                                           create_transaction(3, 't3', 'g3', 30, 'none')]

    undo_operation(librarie)
    undo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none')]

    add_transaction(get_lista_curenta(librarie), 4, 't4', 'g4', 40, 'none')
    save_transactions_list(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(4, 't4', 'g4', 40, 'none')]

    redo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(4, 't4', 'g4', 40, 'none')]

    undo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none')]

    undo_operation(librarie)
    assert get_lista_curenta(librarie) == []

    redo_operation(librarie)
    redo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(4, 't4', 'g4', 40, 'none')]

    redo_operation(librarie)
    assert get_lista_curenta(librarie) == [create_transaction(1, 't1', 'g1', 10, 'none'),
                                           create_transaction(4, 't4', 'g4', 40, 'none')]
