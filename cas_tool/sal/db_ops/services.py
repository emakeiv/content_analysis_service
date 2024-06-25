from dal.model import TvShow as Record
from sal.db_ops.uows import AbstractUnitOfWork



def save_record(entity, uow: AbstractUnitOfWork):


    try:
        with uow:
            record = Record(**entity)
            print(f"created record:{record}")
            uow.repos.add(record)
            uow.commit()

    except Exception as e:
        uow.rollback()
        return f"unexpected error: {str(e)}"

def save_many_records(entities, uow: AbstractUnitOfWork):
    try:
        with uow:
            records = [Record(**entity.dict()) for entity in entities]
            uow.repos.bulk_insert(records)
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