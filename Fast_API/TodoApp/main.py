from fastapi import FastAPI, Depends
import models 
from models import UserPosts 
from database import engine, SessionLocal
import psycopg2
import logging
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/records/all")
async def get_all_records(db:Annotated[Session, Depends(get_db)] ):
    return db.query(UserPosts).all()



    # db_connection = get_db_connection()
    # cursor = db_connection.cursor()

    # postgres_query = f"select * from User_Details"

    # try:
    #     cursor.execute(postgres_query)
    #     postgres_response = cursor.fetchall()
    #     for record in postgres_response :
    #           logging.info(record)
    #           logging.info("___________________________________")
    #     # logging.info(postgres_response)
    # except psycopg2.Error as postgres_error:
    #         logging.error(postgres_error)
    # finally:
    #         cursor.close()
    #         db_connection.close()

    


# def get_db_connection():
#     try:
#         print("creating connection object to database")
#         db_host = "jdbc:mysql://localhost:3306"
#         db_name = "social_media_database"
#         db_user = "root"
#         db_password = "Welcome@24"
#         conn = psycopg2.connect(
#             host=db_host,
#             database=db_name,
#             user=db_user,
#             password=db_password
#             )
#         print("created connection object to database")
#         return conn
        
#     except Exception as e:
#         logging.error(e)




