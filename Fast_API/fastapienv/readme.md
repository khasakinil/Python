step 1 : python -m venv fastapienv
cd to \Python\fastapi
fastapienv\Scripts\activate.bat
pip install fastapi
pip install "uvicorn[standard]"

uvicorn books:app --reload

http://127.0.0.1:8000/books/list

for swagger url => http://127.0.0.1:8000/docs

Path parameter => http://127.0.0.1:8000/books/The%20Waste%20Land

