#!/usr/bin/python3
"""Module deletes an object in the table 'states'in the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def main(argv):
    """ main function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(State).filter(State.name.like('%a%')).all()
    for each in instances:
        session.delete(each)
    session.commit()
    session.close()


if __name__ == '__main__' and len(sys.argv) == 4:
    main(sys.argv)
