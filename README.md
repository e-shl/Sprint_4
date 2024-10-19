# qa_python
# проверяем, что добавилось именно две книги
tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED     [ 11%]
# проверяем, что у книги установлен жанр
tests.py::TestBooksCollector::test_set_book_genre_book_set_genre PASSED  [ 22%]
# проверяем, что жанр книги получен верно
tests.py::TestBooksCollector::test_get_book_genre_get_correct_genre PASSED [ 33%]
# проверяем, что по тестовому жанру получен список из одной тестовой книги
tests.py::TestBooksCollector::test_get_books_with_specific_genre_correct_list_book PASSED [ 44%]
# проверяем, что получаемый словарь books_genre такойже как тестовый
tests.py::TestBooksCollector::test_get_books_genre_correct_books_genre PASSED [ 55%]
# проверяем, что что тестовой книги с возрастным рейтингом отсутствует в списке книг для детей
tests.py::TestBooksCollector::test_get_books_for_children_not_age_rating PASSED [ 66%]
# проверяем, что список избранных содержит тестовую книгу
tests.py::TestBooksCollector::test_add_book_in_favorites_book_in_favorites PASSED [ 77%]
# проверяем, что список избранного пуст
tests.py::TestBooksCollector::test_delete_book_from_favorites_favorites_empty PASSED [ 88%]
# проверяем, что получаемый словарь favorites такойже как тестовый
tests.py::TestBooksCollector::test_get_list_of_favorites_books_correct_favorites PASSED [100%]
