from dal.model import TvShow as Record
from sal.db_ops.uows import AbstractUnitOfWork



def save_record(entity, uow: AbstractUnitOfWork):
    try:
        with uow:
            record = Record(**entity.dict())
            uow.repos.add(record)
            uow.commit()

    except Exception as e:
        uow.rollback()
        return f"unexpected error: {str(e)}"

def save_many_records(entities, uow: AbstractUnitOfWork):
    records =[]
    duplicates = set()
    try:
        with uow():
            for i, entity in entities.iterrows():
                        record_id = (i, entity.asset_id)
                        if record_id not in duplicates:
                            entity["id"] = i
                            record = Record(**entity)
                            records.append(record.dict())
                            duplicates.add(record_id)
                            print(f"{i} record added wit id: {record.id}")
                            #uow.repos.add(record)
                            
                            if i > 100:
                                break
            # if records :
            #     uow.repos.bulk_insert(records)
            #     uow.commit()
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