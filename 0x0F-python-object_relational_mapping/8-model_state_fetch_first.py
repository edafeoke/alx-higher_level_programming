#!/usr/bin/python3
'''
Task 8
'''

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    ses = session.query(State).order_by(State.id).one()
    if ses:
        print("{}: {}".format(ses.id, ses.name))
    else:
        print("Nothing")
    session.close()
