import pytest
import os

from simcity import City

TEST_CITY_NAME = 'г. Москва'
TEST_STREET_NAME = 'ул. Расковой'
TEST_HOUSE_NAME = 'д. 1'
TEST_POPULATION = 500


@pytest.fixture
def city():
    return City(TEST_CITY_NAME)


@pytest.fixture
def street(city):
    return city.add_street(TEST_STREET_NAME)


@pytest.fixture
def house(street):
    return street.add_house(TEST_HOUSE_NAME, TEST_POPULATION)


def test_empty_city(city):
    assert str(city) == TEST_CITY_NAME
    assert city.population == 0


def test_street(street):
    assert str(street) == TEST_CITY_NAME + ', ' + TEST_STREET_NAME


def test_house(house):
    assert str(house) == ', '.join([TEST_CITY_NAME, TEST_STREET_NAME, TEST_HOUSE_NAME])


@pytest.mark.usefixtures('house')
def test_population(city, street):
    assert street.population == city.population == TEST_POPULATION
    city.remove_street(TEST_STREET_NAME)
    assert city.population == 0


@pytest.mark.usefixtures('house')
def test_save_load(city):
    city.save('test_city.dat')
    assert os.path.isfile('test_city.dat')

    city = City.load('test_city.dat')
    assert city.population == TEST_POPULATION
