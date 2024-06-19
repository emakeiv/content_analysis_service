from dal.model import TvShow as Record
from dal.repos.IRepository import IRepository
from sqlalchemy.exc import DatabaseError

class InvalidRecord(Exception):
    pass

def store_record(record: Record, repo: IRepository, session) -> str:
    try:
        if not record.name or len(record.name) < 5:
            raise InvalidRecord("")
        with session.begin():
            repo.add(record)

        return f"record: {record.id} -- stored into db."

    except InvalidRecord as e:
        return str(e)

    except Exception as e:   
        session.rollback()
        return f"Unexpected error: {str(e)}"
