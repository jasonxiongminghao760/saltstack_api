from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from . import db_conn

# 数据库连接信息

Base = declarative_base()  # 生成orm基类

class Hosts(Base):
    '''存放数据库用户名和密码'''
    __tablename__ = 'hosts'  # 表名

    id = Column(Integer, primary_key=True)
    user = Column(String(32))
    password = Column(String(64))
    host = Column(String(64))

def createDB():
    engine=db_conn.get_db_conn()
    Base.metadata.create_all(engine)  # 创建表结构
