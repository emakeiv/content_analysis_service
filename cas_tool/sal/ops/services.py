from dal.model import TvShow as Record
from sal.ops.uows import AbstractUnitOfWork



def save_record(entity, uow: AbstractUnitOfWork):
    try:
        with uow:
            record = Record(**entity.dict())
            uow.repos.add(record)
            uow.commit()

    except Exception as e:
        uow.rollback()
        return f"unexpected error: {str(e)}"

def get_records(uow: AbstractUnitOfWork):
    try:
        with uow:
            return uow.repos.list()
       
    except Exception as e:
            uow.rollback()
            return f"unexpected error: {str(e)}"