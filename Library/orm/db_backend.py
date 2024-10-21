from db_interaction import get_session
from tables import Author, Genre, Book
from sqlalchemy import or_


def _session_wrapper(func):
    def wrapper(*args, **kwargs):
        with get_session() as session:
            return func(session, *args, **kwargs)
    return wrapper


class DBBackend:

    @staticmethod
    @_session_wrapper
    def author_exists(session, author_id):
        exists = session.query(Author).filter(Author.id == author_id).exists()
        return session.query(exists).scalar()    # Вернет True или False

    @staticmethod
    @_session_wrapper
    def genre_exists(session, genre_id):
        exists = session.query(Genre).filter(Genre.id == genre_id).exists()
        return session.query(exists).scalar()     # Вернет True или False

    @staticmethod
    @_session_wrapper
    def book_exists(session, book_id):
        exists = session.query(Book).filter(Book.id == book_id).exists()
        return session.query(exists).scalar()    # Вернет True или False

    @staticmethod
    @_session_wrapper
    def get_book_data(session, book_id):
        return print(session.query(Book).get(book_id))

    @staticmethod
    @_session_wrapper
    def get_books_by_author_id(session, author_id):
        return session.query(Book).filter(Book.author_id == author_id).all()

    @staticmethod
    @_session_wrapper
    def get_books_by_author_name(session, author_name):
        books = session.query(Book).join(Author).filter(
            Author.name.like(f'%{author_name}%')).all()
        if not books:
            print("Книги указанного автора не найдены")
        else:
            for book in books:
                print(book)
        return books

    @staticmethod
    @_session_wrapper
    def get_books_by_genre_id(session, genre_id):
        return session.query(Book).filter(Book.genre_id == genre_id).all()

    @staticmethod
    @_session_wrapper
    def get_books_by_genre(session, genre_name):
        books = session.query(Book).join(Genre).filter(
            Genre.name.like(f'%{genre_name}%')).all()
        if not books:
            print("Книги указанного жанра не найдены")
        else:
            for book in books:
                print(book)
        return books

    @staticmethod
    @_session_wrapper
    def get_books_by_some_match(session, request):
        books = session.query(Book).join(Author).filter(
            or_(Book.title.like(f'%{request}%'),
                Author.name.like(f'%{request}%'))).all()
        if not books:
            print("Совпадений не найдено")
        else:
            for book in books:
                print(book)
        return books

    @staticmethod
    @_session_wrapper
    def get_authors_list(session):
        authors = session.query(Author).all()
        for author in authors:
            print(author)
        return authors

    @staticmethod
    @_session_wrapper
    def get_genres_list(session):
        genres = session.query(Genre).all()
        for genre in genres:
            print(genre)
        return genres

    @staticmethod
    @_session_wrapper
    def add_book(session, title, publication_year, author_id, genre_id):
        new_book = Book(
            title=title,
            publication_year=publication_year,
            author_id=author_id,
            genre_id=genre_id,
        )
        session.add(new_book)
        session.commit()

    @staticmethod
    @_session_wrapper
    def update_book(session, book_id, title=None, publication_year=None,
                    author_id=None, genre_id=None):
        # получаем объект, соответствующий переданному ID
        book = session.query(Book).filter_by(id=book_id).one()

        # обновляем поля объекта на основе переданных аргументов
        if title is not None:
            book.title = title

        if publication_year is not None:
            book.publication_year = publication_year

        if author_id is not None:
            book.author_id = author_id

        if genre_id is not None:
            book.genre_id = genre_id

        session.commit()  # Сохраняем изменения
        return book

    @staticmethod
    @_session_wrapper
    def del_book(session, book_id):
        return session.query(Book).filter_by(id=book_id).delete()

    @staticmethod
    @_session_wrapper
    def add_author(session, name):
        new_author = Author(name=name)
        session.add(new_author)
        session.commit()

    @staticmethod
    @_session_wrapper
    def del_author(session, author_id):
        session.query(Book).filter(Book.author_id == author_id).delete()
        session.query(Author).filter_by(id=author_id).delete()

    @staticmethod
    @_session_wrapper
    def add_genre(session, name):
        new_genre = Genre(name=name)
        session.add(new_genre)
        session.commit()

    @staticmethod
    @_session_wrapper
    def del_genre(session, genre_id):
        session.query(Book).filter(Book.genre_id == genre_id).delete()
        session.query(Genre).filter_by(id=genre_id).delete()
