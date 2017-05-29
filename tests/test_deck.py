import pytest

from deck import Deck, Card


@pytest.mark.parametrize('size', (36, 52))
def test_deck_create(size):
    deck = Deck(size)
    assert len(deck) == size


@pytest.mark.parametrize('size', (1, 10, 600))
def test_deck_create_error(size):
    with pytest.raises(Exception):
        _ = Deck(size)


def test_shuffle():
    deck = Deck(52)
    temp_items = deck.items[:]  # Используем slice для полного копирования списка
    deck.shuffle()
    assert temp_items != deck.items


def test_get_card():
    deck = Deck(36)
    l = len(deck)
    card = deck.get_card()
    # Проверка, что карта была удалена из колоды
    assert len(deck) == l - 1
    # Проверка, что такой карты больше нет в колоде
    assert card not in deck.items


def test_get_card_fail():
    deck = Deck(52)
    while len(deck):
        deck.get_card()

    with pytest.raises(Exception):
        # Попытка взять карту из пустой колоды
        deck.get_card()


def test_card_cmp():
    card1, card2 = Card(2, 4), Card(10, 2)
    assert card1 < card2
    assert card2 > card1


@pytest.mark.parametrize(('val', 'colour', 'name'), [(2, 0, '2 Черви'),
                                                     (11, 3, 'Валет Крести')])
def test_card_str(val, colour, name):
    card = Card(val, colour)
    assert str(card) == name
