from fastapi import FastAPI

#used for validation on data
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(title="id is not needed", default=0)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=5, max_length=50)
    rating: int = Field(gt=-1, lt=6)
    published_date : int =Field(gt=1980, lt=2024)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new Book',
                'author': 'Book Author',
                'description': 'A new description of a Book',
                'rating': 5,
                'published_date': 2022
                }
        }



BOOKS = [Book(1, "All Passion Spent", "Vita Sackville-West", "category of historical fiction", 5, 1999),
         Book(2,"The Waste Land", "T. S. Eliot", "category of  Poem", 5, 2007), 
         Book(3, "Number the Stars", "Lois Lowry", "category of historical fiction", 5, 1991),
         Book(4, "A Little Learning", "Evelyn Waugh", "category of Autobiography", 5, 2017),
         Book(5, "Behold the Man", "Michael Moorcock", "category of science fiction", 4, 2009),
         Book(6, "Arms and the Man", "George Bernard Shaw", "category of Comedy", 4, 2000)
         ]

@app.get("/book/getall")
async def read_all_books():
    return BOOKS

@app.get("/book/id/{bookid}")
async def get_book_by_id(bookid: int):
    for book in BOOKS:
        if book.id == bookid :
            return book
        
@app.get("/book/rating/{book_rating}")
async def get_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating :
            books_to_return.append(book)
    return books_to_return

@app.post("/book/add")
async def add_new_books(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_by_id(new_book))
    return new_book

@app.put("/book/update")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id :
            BOOKS[i]=book
            break
    return book


def find_book_by_id(book:Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.delete("/book/delete/{book_id}")
async def delete_book_by_id(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break

@app.get("/book/pubdate/{published_date}")
async def get_book_by_rating(published_date: int):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date :
            books_to_return.append(book)
    return books_to_return

