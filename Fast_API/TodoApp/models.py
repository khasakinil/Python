from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class UserPosts(Base):
    __tablename__ = 'user_posts'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    user_user_id = Column(Integer)


