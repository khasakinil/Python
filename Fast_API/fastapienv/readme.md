step 1 : python -m venv fastapienv

cd to \Python\fastapi

fastapienv\Scripts\activate.bat

pip install fastapi

pip install "uvicorn[standard]"

uvicorn books:app --reload

http://127.0.0.1:8000/books/list

for swagger url => http://127.0.0.1:8000/docs

Path parameter => http://127.0.0.1:8000/books/The%20Waste%20Land

Query parameter => http://127.0.0.1:8000/books/cat/?category=Autobiography 

with path paramter and query parameter => http://127.0.0.1:8000/books/George%20Bernard%20Shaw/?category=Comedy

post request : http://127.0.0.1:8000/book/add
    body :  {"title":"The Two Towers", "author":"J. R. R. Tolkien", "category":"historical fiction"}

put request : http://127.0.0.1:8000/book/update
    body : {"title":"The Waste Land", "author":"T. S. Eliot", "category":"Autobiography"}

delete request : http://127.0.0.1:8000/book/delete/The%20Waste%20Land

