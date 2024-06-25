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
    records = []
    duplicates = set()

    for i, entity in entities.iterrows():
        record_id = (i, entity.asset_id)
        if record_id not in duplicates:
            entity["id"] = str(i)
            record = Record(**entity)
            records.append(record.dict())
            duplicates.add(record_id)
            try:
                with uow:
                    print(f"{i} record added wit id: {record.id}")
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
