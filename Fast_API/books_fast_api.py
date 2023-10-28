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

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=5, max_length=50)
    rating: int = Field(gt=-1, lt=6)


BOOKS = [Book(1, "All Passion Spent", "Vita Sackville-West", "category of historical fiction", 5),
         Book(2,"The Waste Land", "T. S. Eliot", "category of  Poem", 5), 
         Book(3, "Number the Stars", "Lois Lowry", "category of historical fiction", 5),
         Book(4, "A Little Learning", "Evelyn Waugh", "category of Autobiography", 5),
         Book(5, "Behold the Man", "Michael Moorcock", "category of science fiction", 4),
         Book(6, "Arms and the Man", "George Bernard Shaw", "category of Comedy", 4)
         ]

@app.get("/book/getall")
async def read_all_books():
    return BOOKS

@app.post("/book/add")
async def add_new_books(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_by_id(new_book))
    return new_book


def find_book_by_id(book:Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

