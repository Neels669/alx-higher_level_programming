#!/usr/bin/python3
""" this module adds a new object to states table in the database"""
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
    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    print(new.id)
    session.close()


if __name__ == '__main__' and len(sys.argv) == 4:
    main(sys.argv)
