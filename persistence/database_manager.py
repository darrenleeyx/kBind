from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from persistence.base import Base
from config import DATABASE_URL

class DatabaseManager:
    @staticmethod
    def setup_database():
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        return sessionmaker(bind=engine)()

    @staticmethod
    def teardown_database(engine):
        Base.metadata.drop_all(engine)

    #create a static method to insert some records into the database
    @staticmethod
    def insert_records(session):
        from persistence.bindings.binding import Binding
        session.add(Binding("CustomT", ["t"], ["f", "v"]))
        session.commit()
        session.close()