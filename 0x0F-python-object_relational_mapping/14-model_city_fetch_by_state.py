#!/usr/bin/python3
"""prints states that matches 4th arg"""
from model_state import Base, State
from model_city import City
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
    cities = session.query(City, State).join(State)
    for city, state in cities.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
        session.commit()
        session.close()
