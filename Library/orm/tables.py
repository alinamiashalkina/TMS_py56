from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from db_interaction import engine

Base = declarative_base()     # базовый класс для моделей


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(length=50))
    books = relationship("Book", back_populates="author")

    def __str__(self):
        return f"{self.id}.{self.name}"


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(length=50))
    books = relationship("Book", back_populates="genre")

    def __str__(self):
        return f"{self.id}.{self.name}"


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(length=50))
    publication_year = Column(Integer)
    author_id = Column(Integer, ForeignKey(Author.id))
    genre_id = Column(Integer, ForeignKey(Genre.id))
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")

    def __str__(self):
        return f"'{self.id}.{self.title}', {self.publication_year}"


# создать таблицы в базе данных согласно моделям
# Base.metadata.create_all(engine)
