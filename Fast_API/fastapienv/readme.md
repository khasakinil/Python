step 1 : python -m venv fastapienv
cd to \Python\fastapi
fastapienv\Scripts\activate.bat
pip install fastapi
pip install "uvicorn[standard]"

uvicorn books:app --reload

http://127.0.0.1:8000/books/list

http://127.0.0.1:8000/docs => for swagger url



