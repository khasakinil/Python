from fastapi import FastAPI, Body

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
async def add_new_books(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS