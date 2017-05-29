import random


class Deck:
    def __init__(self, num):
        self._items = []
        if num == 52:
            # Создать колоду, начиная с двойки
            self._create_deck(2)
        elif num == 36:
            # Создать колоду, начиная с шестерки
            self._create_deck(6)
        else:
            raise Exception('Неверный размер колоды. Используйте 52 или 36')

    def _create_deck(self, n, m=15, z=4):
        """
        Инициализация колоды
        :param n: int Номер стартовой карты
        :param m: int Номер последней карты
        :param z: int Число мастей в колоде
        :return: None
        """
        # Перебор весов карт
        for i in range(n, m):
            # Перебор мастей карт
            for j in range(z):
                self._items.append(Card(i, j))

    def shuffle(self):
        """
        Перемешивание колоды
        :return: None
        """
        random.shuffle(self._items)

    def get_card(self):
        # Получение размера колоды и проверка на пустоту
        l = len(self)
        if l <= 0:
            raise Exception('Колода пуста!')
        # Выбор индекса карты, которая будет выдана
        i = random.randint(0, l - 1)
        # Выдача карты с одновременным удалением из колоды
        return self._items.pop(i)

    @property
    def items(self):
        return self._items

    def __len__(self):
        """
        Получение оставшегося числа карт в колоде
        :return: integer
        """
        return len(self._items)


class Card:
    _STR_MAP = {
        11: 'Валет',
        12: 'Дама',
        13: 'Король',
        14: 'Туз'
    }

    _COLOUR_MAP = {
        0: 'Черви',
        1: 'Пики',
        2: 'Бубны',
        3: 'Крести'
    }

    def __init__(self, val, colour):
        self.val = val
        self.colour = colour

    def __str__(self):
        val = self._STR_MAP.get(self.val, self.val)
        colour = self._COLOUR_MAP[self.colour]
        return '{} {}'.format(val, colour)

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val
