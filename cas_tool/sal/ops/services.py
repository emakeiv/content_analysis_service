from dal.model import TvShow as Record
from dal.adapters.repository import AbstracRepository
from sal.ops.uows import AbstractUnitOfWork


class InvalidRecord(Exception):
    pass


def store_record(record: Record, uow: AbstractUnitOfWork):
    try:
        with uow:
            uow.repos.add(record)
            uow.commit()
    except InvalidRecord as e:
        return str(e)

    except Exception as e:
        uow.rollback()
        return f"Unexpected error: {str(e)}"
