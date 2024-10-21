from __constants import DB_CONNECTION
from db_connect import DBConnect

db = DBConnect(**DB_CONNECTION)


def _add_cursor_wrapper(func):
    def wrapper(*args, **kwargs):
        with db.get_connection().cursor() as cur:
            return func(cur, *args, **kwargs)
    return wrapper


@_add_cursor_wrapper
def author_exists(cur, author_id):
    cur.execute(
        '''
        SELECT COUNT(*) FROM author 
        WHERE id = %s
        ''',
        (author_id,)
    )
    exists = cur.fetchone()[0] > 0
    return exists


@_add_cursor_wrapper
def genre_exists(cur, genre_id):
    cur.execute(
        '''
        SELECT COUNT(*) FROM genre 
        WHERE id = %s
        ''',
        (genre_id,)
    )
    exists = cur.fetchone()[0] > 0
    return exists


@_add_cursor_wrapper
def book_exists(cur, book_id):
    cur.execute(
        '''
        SELECT COUNT(*) FROM book 
        WHERE id = %s
        ''',
        (book_id,)
    )
    exists = cur.fetchone()[0] > 0
    return exists


@_add_cursor_wrapper
def get_book_data(cur, book_id):
    cur.execute(
        '''
        SELECT book.title, book.publication_year,
        author.name AS author,
        genre.name AS genre 
        FROM book
        LEFT JOIN author ON author.id = book.author_id
        LEFT JOIN genre ON genre.id = book.genre_id
        WHERE book.id = %s
        ''',
        (book_id,)
    )
    return cur.fetchone()


@_add_cursor_wrapper
def get_books_by_author_name(cur, author_name):
    cur.execute(
        '''
        SELECT CONCAT(book.title, ', ', book.publication_year) AS book, 
        genre.name AS genre 
        FROM author
        LEFT JOIN book ON author.id = book.author_id
        LEFT JOIN genre ON genre.id = book.genre_id 
        WHERE author.name LIKE %s
        ''',
        ('%' + author_name + '%',)
    )
    return cur.fetchall()


@_add_cursor_wrapper
def get_books_by_author_id(cur, author_id):
    cur.execute(
        '''
        SELECT CONCAT(book.title, ', ', book.publication_year) AS book, 
        genre.name AS genre 
        FROM author
        LEFT JOIN book ON author.id = book.author_id
        LEFT JOIN genre ON genre.id = book.genre_id 
        WHERE author.id = %s
        ''',
        (author_id,)
    )
    return cur.fetchall()


@_add_cursor_wrapper
def get_books_by_genre(cur, genre_name):
    cur.execute(
        '''
        SELECT CONCAT(book.title, ', ', book.publication_year) AS book, 
        author.name AS author 
        FROM genre
        LEFT JOIN book ON genre.id = book.genre_id
        LEFT JOIN author ON author.id = book.author_id
        WHERE genre.name = %s
        ''',
        (genre_name,)
    )
    return cur.fetchall()


@_add_cursor_wrapper
def get_books_by_genre_id(cur, genre_id):
    cur.execute(
        '''
        SELECT CONCAT(book.title, ', ', book.publication_year) AS book, 
        author.name AS author 
        FROM genre
        LEFT JOIN book ON genre.id = book.genre_id
        LEFT JOIN author ON author.id = book.author_id 
        WHERE genre.id = %s
        ''',
        (genre_id,)
    )
    return cur.fetchall()


@_add_cursor_wrapper
def get_books_by_some_match(cur, request):
    cur.execute(
        '''
        SELECT author.name AS author, 
        CONCAT(book.title, ', ', book.publication_year) AS book, 
        genre.name AS genre 
        FROM book
        LEFT JOIN author ON author.id = book.author_id
        LEFT JOIN genre ON genre.id = book.genre_id 
        WHERE book.title LIKE %s OR author.name LIKE %s
        ''',
        ('%' + request + '%', '%' + request + '%')
    )
    return cur.fetchall()


@_add_cursor_wrapper
def get_authors_list(cur):
    cur.execute(
        '''
        SELECT id, name
        FROM author
        order by id
        ''',
        ()
    )
    return cur.fetchall()


@_add_cursor_wrapper
def get_genres_list(cur):
    cur.execute(
        '''
        SELECT id, name
        FROM genre
        order by id
        ''',
        ()
    )
    return cur.fetchall()


@_add_cursor_wrapper
def add_book(cur, title, publication_year, author_id, genre_id):
    cur.execute(
        f'''
        INSERT INTO book(title, publication_year, author_id, genre_id)
        VALUES(%s, %s, %s, %s)
        ''',
        (title, publication_year, author_id, genre_id)
    )


@_add_cursor_wrapper
def update_book(cur, id, title=None, publication_year=None, author_id=None,
                genre_id=None, ):
    # Общее начало SQL-запроса для обновления данных
    sql = "UPDATE book SET "
    parameters = []

    # Проверяем, какие параметры были переданы для обновления
    # и формируем основную часть SQL-запроса
    if title is not None:
        sql += "title = %s, "
        parameters.append(title)
    if publication_year is not None:
        sql += "publication_year = %s, "
        parameters.append(publication_year)
    if author_id is not None:
        sql += "author_id = %s, "
        parameters.append(author_id)
    if genre_id is not None:
        sql += "genre_id = %s, "

    # Удаляем последнюю запятую и добавляем условие WHERE
    sql = sql.rstrip(', ')
    sql += " WHERE id = %s"
    parameters.append(id)
    cur.execute(sql, tuple(parameters))


@_add_cursor_wrapper
def del_book(cur, book_id):
    cur.execute(
        f'''
        DELETE FROM book
        WHERE id = %s
        ''',
        (book_id,)
    )


@_add_cursor_wrapper
def add_author(cur, name):
    cur.execute(
        f'''
        INSERT INTO author(name)
        VALUES(%s)
        ''',
        (name,)
    )


@_add_cursor_wrapper
def del_author(cur, author_id):
    cur.execute(
        f'''
        DELETE FROM book
        WHERE author_id = %s
        ''',
        (author_id,)
    )

    cur.execute(
        f'''
        DELETE FROM author
        WHERE id = %s
        ''',
        (author_id,)
    )


@_add_cursor_wrapper
def add_genre(cur, name):
    cur.execute(
        f'''
        INSERT INTO genre(name)
        VALUES(%s)
        ''',
        (name,)
    )


@_add_cursor_wrapper
def del_genre(cur, genre_id):
    cur.execute(
        f'''
            DELETE FROM book
            WHERE genre_id = %s
            ''',
        (genre_id,)
    )
    cur.execute(
        f'''
        DELETE FROM genre
        WHERE id = %s
        ''',
        (genre_id,)
    )
