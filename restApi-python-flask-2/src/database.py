from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String

engine = create_engine('postgresql://lucas:admin@127.0.0.1:5433/TesteUser')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
        
def init_db():
    Base.metadata.create_all(bind=engine)

class Persons(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    age = Column(Integer)

    def __repr__(self):
        return '<Person {}>'.format(self.name)

class Activities(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    person_id = Column(Integer, ForeignKey('persons.id'))
    persons = relationship('persons')

if __name__ == '__main__':
    init_db()