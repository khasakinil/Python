step 1 : python -m venv fastapienv
cd to \Python\fastapi
fastapienv\Scripts\activate.bat
pip install fastapi
pip install "uvicorn[standard]"

uvicorn books:app --reload

