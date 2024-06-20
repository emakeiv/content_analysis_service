from dal.model import TvShow as Record
from dal.adapters.repository import AbstracRepository
from sal.ops.uows import AbstractUnitOfWork

import logging

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

def get_records(uow: AbstractUnitOfWork):
    try:
        with uow:
           
            items = uow.repos.list()


            return items
    except Exception as e:
            uow.rollback()
            return f"Unexpected error: {str(e)}"