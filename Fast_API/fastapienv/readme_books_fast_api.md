step 1 : python -m venv fastapienv

cd to \Python\fastapi

fastapienv\Scripts\activate.bat

pip install fastapi

pip install "uvicorn[standard]"

uvicorn books_fast_api:app --reload

1. get all books
Request URI : http://127.0.0.1:8000/books/getall

2. add book to list
Request URI : http://127.0.0.1:8000/book/add

Request Body -
     {
        "id": 7,
        "title": "2 States",
        "author": "Chetan Bhagat",
        "description": "The Story of My Marriage",
        "rating": 4
    }






