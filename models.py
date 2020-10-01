from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///programming-languages.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

base = declarative_base()
base.query = db_session.query_property()

class ProgrammingLanguages(base):
    __tablename__='programminglanguages'
    id      = Column(Integer, primary_key=True)
    name    = Column(String(40), index=True)

    def __repr__(self):
        return '<Programming_Language: {}>' .format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Related(base):
    __tablename__='related'
    id      = Column(Integer, primary_key=True)
    name    = Column(String(40), index=True)
    programming_id = Column(Integer, ForeignKey('programminglanguages.id')) 
    programminglanguages = relationship('ProgrammingLanguages')

    def __repr__(self):
        return '<Related: {}>' .format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Users(base):
    __tablename__='users'
    login       = Column(String(20), primary_key=True)
    password    = Column(String(40))

    def __repr__(self):
        return '<User: {}>' .format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()