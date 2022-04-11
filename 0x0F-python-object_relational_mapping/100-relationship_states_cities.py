#!/usr/bin/python3
"""
Save them as relationship_city.py and relationship_state.py
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
    bd_session = sessionmaker(bind=engine)
    return bd_session()


if __name__ == '__main__':
    bd_session = mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3])

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    bd_session.add(new_state)
    bd_session.add(new_city)
    bd_session.commit()
