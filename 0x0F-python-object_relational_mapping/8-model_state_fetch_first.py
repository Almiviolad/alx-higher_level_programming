#!/usr/bin/python3
"""prints first states objects from database hbtn_0e_6_usa"""
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
    f_state = session.query(State).order_by(State_id).first()
    if (state is not None):
        print("{}: {}".format(f_state.id, f_state.name))
    else:
        print("Nothing")
