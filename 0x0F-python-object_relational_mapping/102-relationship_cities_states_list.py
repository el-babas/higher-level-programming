#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def mysqlconnect(username, password, database, port=3306):
    """
    Function:
        Connect to MySQL with sqlalchemy.

    Args:
        username (str): username to connect to MySQL.
        password (str): password to connect to MySQL.
        database (str): database to connect to MySQL.
        port (int): port to connect to MySQL.

    Return:
        Connect to MySQL (session) use sqlalchemy.
    """
    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
                            username,
                            password,
                            port,
                            database),
                    pool_pre_ping=True)

    # INFO! Create object if not exit in database.
    Base.metadata.create_all(engine)
    bd_session = sessionmaker(bind=engine)
    return bd_session()


if __name__ == '__main__':
    bd_session = mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3])
    states = bd_session.query(State).join(City).order_by(City.id).all()

    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
