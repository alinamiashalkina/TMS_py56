from db_backend import DBBackend


class Librarian:

    @staticmethod
    def display_menu():
        print("Выберите опцию:")
        print("1. Получить данные о книге")
        print("-1. Изменить данные о книге")
        print("2. Добавить книгу")
        print("-2. Удалить книгу")
        print("3. Получить список авторов")
        print("4. Получить список жанров")
        print("5. Добавить автора")
        print("-5. Удалить автора")
        print("6. Добавить жанр")
        print("-6. Удалить жанр")
        print("7. Получить книги по автору")
        print("8. Получить книги по жанру")
        print("9. Получить книги по частичному совпадению в названии книги "
              "или имени автора")
        print("0. Выход")

    @staticmethod
    def main():
        while True:
            Librarian.display_menu()
            choice = input("Введите номер операции: ")

            if choice == "1":
                book_id = int(input("Введите ID книги: "))
                if not DBBackend.book_exists(book_id):
                    print("Книга не найдена")
                else:
                    print(DBBackend.get_book_data(book_id))

            elif choice == "-1":
                book_id = int(input("Введите ID книги: "))
                if not DBBackend.book_exists(book_id):
                    print("Книга не найдена")
                else:
                    print(
                        "Введите новые данные о книге "
                        "(оставьте значение пустым, если не хотите обновлять):")

                    title = input("Новое название книги: ")
                    if title == "":
                        title = None

                    publication_year = int(input("Новый год публикации: "))
                    if publication_year == "":
                        publication_year = None
                    else:
                        publication_year = int(publication_year)

                    author_id = input("Новый ID автора: ")
                    if author_id == "":
                        author_id = None
                    else:
                        author_id = int(author_id)

                    genre_id = input("Новый ID жанра: ")
                    if genre_id == "":
                        genre_id = None
                    else:
                        genre_id = int(genre_id)

                    DBBackend.update_book(book_id, title, publication_year,
                                          author_id, genre_id)
                    print("Данные книги обновлены.")

            elif choice == "2":
                while True:
                    try:
                        title = input("Введите название книги: ")
                        publication_year = int(input("Введите "
                                                     "год публикации: "))
                        while True:
                            author_id = int(input("Введите ID автора: "))
                            if not DBBackend.author_exists(author_id):
                                print("Автора с указанным ID не существует. "
                                      "Пожалуйста, попробуйте снова.")
                                continue  # Запросить ID снова.
                            break  # Выход из цикла, если автор существует.
                        while True:
                            genre_id = int(input("Введите ID жанра: "))
                            if not DBBackend.genre_exists(genre_id):
                                print("Жанра с указанным ID не существует. "
                                      "Пожалуйста, попробуйте снова.")
                                continue  # Запросить ID снова.
                            break  # Выход из цикла, если жанр существует.
                        DBBackend.add_book(title, publication_year, author_id,
                                           genre_id)
                        print("Книга добавлена.")
                    except ValueError:
                        print("Некорректный ввод. Введенное значение должно "
                              "быть числом. Добвьте книгу заново.")
                        continue
                    break

            elif choice == "-2":
                book_id = int(input("Введите ID книги, "
                                    "которую хотите удалить: "))
                if not DBBackend.book_exists(book_id):
                    print("Книга не найдена")
                else:
                    DBBackend.del_book(book_id)
                    print("Книга удалена.")

            elif choice == "3":
                authors = DBBackend.get_authors_list()
                for author in authors:
                    print(f"ID: {author[0]}, Имя: {author[1]}")

            elif choice == "4":
                genres = DBBackend.get_genres_list()
                for genre in genres:
                    print(f"ID: {genre[0]}, Название: {genre[1]}")

            elif choice == "5":
                name = input("Введите имя автора: ")
                DBBackend.add_author(name)
                print(f"Автор {name} добавлен.")

            elif choice == "-5":
                print("ВНИМАНИЕ! При удалении автора будут удалены все книги"
                      "этого автора. Продолжить?")
                yes_no = input("Введите  1, чтобы продолжить, "
                               "2, чтобы выйти в главное меню: ")
                if yes_no == "1":
                    while True:
                        del_author_id = input("Введите ID автора:  ")
                        if not DBBackend.author_exists(del_author_id):
                            print("Автора с указанным ID не существует. "
                                  "Пожалуйста, попробуйте снова.")
                            continue  # Запросить ID снова.
                        break  # Выход из цикла, если автор существует.
                    books = DBBackend.get_books_by_author_id(del_author_id)
                    DBBackend.del_author(del_author_id)
                    print("Автор удален.")
                    if books:
                        print("Удалены следующие книги:")
                        for book in books:
                            print(book)
                    else:
                        print("У данного автора не было книг.")
                else:
                    print("Вы вернулись в главное меню")

            elif choice == "6":
                name = input("Введите название жанра: ")
                DBBackend.add_genre(name)
                print("Жанр добавлен.")

            elif choice == "-6":
                print("ВНИМАНИЕ! При удалении жанра будут удалены все книги"
                      "этого жанра. Продолжить?")
                yes_no = input("Введите  1, чтобы продолжить, "
                               "2, чтобы выйти в главное меню: ")
                if yes_no == "1":
                    while True:
                        del_genre_id = input("Введите ID жанра:  ")
                        if not DBBackend.genre_exists(del_genre_id):
                            print("Жанра с указанным ID не существует. "
                                  "Пожалуйста, попробуйте снова.")
                            continue  # Запросить ID снова.
                        break  # Выход из цикла, если автор существует.
                    books = DBBackend.get_books_by_genre_id(del_genre_id)
                    DBBackend.del_genre(del_genre_id)
                    print("Жанр удален.")
                    if books:
                        print("Удалены следующие книги:")
                        for book in books:
                            print(book)

            elif choice == "7":
                author_name = input("Введите имя автора для поиска книг: ")
                books = DBBackend.get_books_by_author_name(author_name)
                if books:
                    for book in books:
                        print(book)
                else:
                    print("Книги указанного автора не найдены.")

            elif choice == "8":
                genre_name = input("Введите название жанра для поиска книг: ")
                books = DBBackend.get_books_by_genre(genre_name)
                if books:
                    for book in books:
                        print(book)
                else:
                    print("Книги указанного жанра не найдены.")

            elif choice == "9":
                request = input("Введите запрос для поиска совпадений: ")
                books = DBBackend.get_books_by_some_match(request)
                if books:
                    for book in books:
                        print(book)
                else:
                    print("Совпадений не найдено.")

            elif choice == "0":
                print("Выход из приложения.")
                break

            else:
                print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    Librarian.main()
