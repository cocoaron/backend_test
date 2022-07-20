from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(
    "mysql+pymysql://root:mecha07182022!@localhost:3306/dummy?charset=utf8",
    encoding = "utf-8",
    echo = True)

session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = engine
    )
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = session.query_property()
