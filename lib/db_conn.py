from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_conn():
    engine = create_engine("mysql+pymysql://root:123456@10.0.0.171/cmdb",max_overflow=5)
    return engine


def get_db_session():
    engine = create_engine("mysql+pymysql://root:123456@10.0.0.171/cmdb",max_overflow=5)
    Seeion = sessionmaker(bind=engine)
    session = Seeion()
    return session
