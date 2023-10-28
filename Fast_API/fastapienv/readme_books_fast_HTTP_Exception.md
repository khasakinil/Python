step 1 : python -m venv fastapienv

cd to \Python\fastapi

fastapienv\Scripts\activate.bat

pip install fastapi

pip install "uvicorn[standard]"

uvicorn books_fast_HTTP_Exception:app --reload

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

3. get books by rating
Reques URI : http://127.0.0.1:8000/book/rating/4

4. update book
Reques URI : http://127.0.0.1:8000/book/update

Request Body -
    {
        "id": 3,
        "title": "Number the Stars",
        "author": "Lois Lowry",
        "description": "description - historical fiction",
        "rating": 4
    }

5. Data validation with path parameters and query parameters
Reques URI : http://127.0.0.1:8000/book/pubdate/?published_date=2017
http://127.0.0.1:8000/book/rating/query/?book_rating=4


