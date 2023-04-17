#!/usr/bin/python3
"""prints states that matches 4th arg"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """connect to database and return query"""
    db_link = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_link)
    Session = sessionmaker(bind=eng)

    session = Session()
    state = session.query(State).filter(State.name.contains('a'))
    if (state is not None):
        for st in state:
            session.delete(st)
        session.commit()
        session.close()
