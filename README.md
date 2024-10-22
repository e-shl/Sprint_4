# qa_python
# проверяем, что добавилось именно две книги
tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED     [  7%]
# проверяем, что Название книги может содержать максимум 40 символов
tests.py::TestBooksCollector::test_add_new_book_boundary_name[A] PASSED  [ 14%]
tests.py::TestBooksCollector::test_add_new_book_boundary_name[AA] PASSED [ 21%]
tests.py::TestBooksCollector::test_add_new_book_boundary_name[20] PASSED [ 28%]
tests.py::TestBooksCollector::test_add_new_book_boundary_name[39] PASSED [ 35%]
tests.py::TestBooksCollector::test_add_new_book_boundary_name[40] PASSED [ 42%]
# проверяем, что у книги установлен жанр
tests.py::TestBooksCollector::test_set_book_genre_book_set_genre PASSED  [ 50%]
# проверяем, что жанр книги получен верно
tests.py::TestBooksCollector::test_get_book_genre_get_correct_genre PASSED [ 57%]
# проверяем, что по тестовому жанру получен список из одной тестовой книги
tests.py::TestBooksCollector::test_get_books_with_specific_genre_correct_list_book PASSED [ 64%]
# проверяем, что получаемый словарь books_genre такойже как тестовый
tests.py::TestBooksCollector::test_get_books_genre_correct_books_genre PASSED [ 71%]
# проверяем, что что тестовой книги с возрастным рейтингом отсутствует в списке книг для детей
tests.py::TestBooksCollector::test_get_books_for_children_not_age_rating PASSED [ 78%]
# проверяем, что список избранных содержит тестовую книгу
tests.py::TestBooksCollector::test_add_book_in_favorites_book_in_favorites PASSED [ 85%]
# проверяем, что список избранного пуст
tests.py::TestBooksCollector::test_delete_book_from_favorites_favorites_empty PASSED [ 92%]
# проверяем, что получаемый словарь favorites такойже как тестовый
tests.py::TestBooksCollector::test_get_list_of_favorites_books_correct_favorites PASSED [100%]
