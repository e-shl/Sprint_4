import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self,collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две книги
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name', ["A", "AA", "20 тоже может здесь!", "39 символов обязательно должно быть тут", "40 символов обязательно должно быть тута"])
    def test_add_new_book_boundary_name(self,collector,name):
        # добавляем книги
        collector.add_new_book(name)
        # проверяем, что Название книги может содержать максимум 40 символов
        assert collector.books_genre == {name : ""}

    def test_set_book_genre_book_set_genre(self,collector):
        # создаём переменные теста
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        # добавляем книгу
        collector.add_new_book(name)
        # устанавливаем жанр добавленной книге
        collector.set_book_genre(name, genre)
        # проверяем, что у книги установлен жанр
        assert collector.books_genre[name] == genre

    def test_get_book_genre_get_correct_genre(self,collector):
        # создаём переменные теста
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        # добавляем книгу
        collector.add_new_book(name)
        # устанавливаем жанр добавленной книге
        collector.set_book_genre(name, genre)
        # проверяем, что жанр книги получен верно
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_correct_list_book(self,collector):
        # создаём переменные теста
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        # добавляем книгу
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверяем, что по тестовому жанру получен список из одной тестовой книги
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_genre_correct_books_genre(self,collector):
        # создаём переменные теста
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        # добавляем книгу
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверяем, что получаемый словарь books_genre такойже как тестовый
        assert collector.get_books_genre() == {name : genre}

    def test_get_books_for_children_not_age_rating(self,collector):
        # создаём переменные теста
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        # добавляем две книги
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверяем, что что тестовой книги с возрастным рейтингом отсутствует в списке книг для детей
        assert name not in collector.get_books_for_children()

    def test_add_book_in_favorites_book_in_favorites(self,collector):
        # создаём переменные теста
        name = 'Гордость и предубеждение и зомби'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в избранное
        collector.add_book_in_favorites(name)
        # проверяем, что список избранных содержит тестовую книгу
        assert collector.favorites == [name]

    def test_delete_book_from_favorites_favorites_empty(self,collector):
        # создаём переменные теста
        name = 'Гордость и предубеждение и зомби'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в избранное
        collector.add_book_in_favorites(name)
        # удаляем книгу из избранного
        collector.delete_book_from_favorites(name)
        # проверяем, что список избранного пуст
        assert not collector.favorites

    def test_get_list_of_favorites_books_correct_favorites(self,collector):
        # создаём переменные теста
        name = 'Гордость и предубеждение и зомби'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в избранное
        collector.add_book_in_favorites(name)
        # проверяем, что получаемый словарь favorites такойже как тестовый
        assert collector.get_list_of_favorites_books() == [name]