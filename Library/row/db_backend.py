from db_interaction import (
    author_exists,
    genre_exists,
    book_exists,
    get_book_data,
    get_books_by_author_name,
    get_books_by_author_id,
    get_books_by_genre,
    get_books_by_genre_id,
    get_books_by_some_match,
    get_authors_list,
    get_genres_list,
    add_book,
    update_book,
    del_book,
    add_author,
    del_author,
    add_genre,
    del_genre
)


class DBBackend:

    @staticmethod
    def author_exists(author_id):
        return author_exists(author_id)

    @staticmethod
    def genre_exists(genre_id):
        return genre_exists(genre_id)

    @staticmethod
    def book_exists(book_id):
        return book_exists(book_id)

    @staticmethod
    def get_book_data(book_id):
        return get_book_data(book_id)

    @staticmethod
    def get_books_by_author_name(author_name):
        return get_books_by_author_name(author_name)

    @staticmethod
    def get_books_by_author_id(author_id):
        return get_books_by_author_id(author_id)

    @staticmethod
    def get_books_by_genre(genre_name):
        return get_books_by_genre(genre_name)

    @staticmethod
    def get_books_by_genre_id(genre_id):
        return get_books_by_genre_id(genre_id)

    @staticmethod
    def get_books_by_some_match(request):
        return get_books_by_some_match(request)

    @staticmethod
    def get_authors_list():
        return get_authors_list()

    @staticmethod
    def get_genres_list():
        return get_genres_list()

    @staticmethod
    def add_book(title, publication_year, author_id, genre_id):
        return add_book(title, publication_year, author_id, genre_id)

    @staticmethod
    def update_book(id, title, publication_year, author_id, genre_id):
        return update_book(id, title, publication_year, author_id, genre_id)

    @staticmethod
    def del_book(book_id):
        return del_book(book_id)

    @staticmethod
    def add_author(name):
        return add_author(name)

    @staticmethod
    def del_author(author_id):
        return del_author(author_id)

    @staticmethod
    def add_genre(name):
        return add_genre(name)

    @staticmethod
    def del_genre(genre_id):
        return del_genre(genre_id)
