from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title":"All Passion Spent", "Author":"Vita Sackville-West", "Category":"fiction novel"},
    {"title":"Arms and the Man", "Author":"George Bernard Shaw", "Category":"Comedy"},
    {"title":"Behold the Man", "Author":"Michael Moorcock", "Category":"science fiction"},
    {"title":"A Little Learning", "Author":"Evelyn Waugh", "Category":"Autobiography"},
    {"title":"Number the Stars", "Author":"Lois Lowry", "Category":"historical fiction"},
    {"title":"The Waste Land", "Author":"T. S. Eliot", "Category":"poem"}
]

@app.get("/books/list")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
