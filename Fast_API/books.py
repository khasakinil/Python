from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title":"All Passion Spent", "author":"Vita Sackville-West", "category":"historical fiction"},
    {"title":"Arms and the Man", "author":"George Bernard Shaw", "category":"Comedy"},
    {"title":"Behold the Man", "author":"Michael Moorcock", "category":"science fiction"},
    {"title":"A Little Learning", "author":"Evelyn Waugh", "category":"Autobiography"},
    {"title":"Number the Stars", "author":"Lois Lowry", "category":"historical fiction"},
    {"title":"The Waste Land", "author":"T. S. Eliot", "category":"poem"}
]

# api with endpoint
@app.get("/books/list")
async def read_all_books():
    return BOOKS

# api with path paramter endpoint
@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            books_to_return.append(book)
    return books_to_return

# api with query parameter endpoint
@app.get("/books/cat/")
async def read_categoty_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# api with path paramter and query parameter endpoint
@app.get("/books/{book_author}/")
async def read_all_books(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold() and book.get('author').casefold() == book_author.casefold():
             books_to_return.append(book)
    return books_to_return


# with body for post request
@app.post("/books/add")
async def add_book_to_collection(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS


# with body for put request
@app.put("/books/update")
async def update_book_in_collection(updated_book=Body()):
    for i in range(len(BOOKS)):
        if(BOOKS[i].get("title").casefold() == updated_book.get("title").casefold()):
            BOOKS[i] = updated_book
    return BOOKS


# delete the record
@app.delete("/books/delete/{book_title}")
async def delete_book_in_collection(book_title : str):
    for i in range(len(BOOKS)):
        if(BOOKS[i].get("title").casefold() == book_title.casefold()):
            BOOKS.pop(i)
            break
    return BOOKS

