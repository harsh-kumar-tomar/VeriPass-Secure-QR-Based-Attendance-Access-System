from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime, Integer , String , ForeignKey
from datetime import datetime
from enum import Enum

class Base(DeclarativeBase):
    pass
    

class DBProfessor(Base):
    __tablename__ = "professors"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    dob = Column()
    created_at = Column(DateTime,default=datetime.utcnow)




class DBCourse(Base):
    __tablename__ = "courses"
    id = Column(Integer,primary_key=True,autoincrement=True)
    course = Column(String)
    branch = Column(String)
    duration = Column(Integer)


class DBStudent(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    phone_num = Column(Integer)
    email = Column(String)
    batch = Column(Integer)
    dob = Column()
    course_id = Column(Integer,ForeignKey("courses.id"))
    created_at = Column(DateTime,default=datetime.utcnow)


class Session(Base):
    pass
