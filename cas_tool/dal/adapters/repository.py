from typing import List
import dal.model as model
from abc import ABC, abstractmethod


class AbstracRepository(ABC):

    @abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abstractmethod
    def get(self, entity_id: int):
        raise NotImplementedError

    @abstractmethod
    def list(self):
        raise NotImplementedError

    @abstractmethod
    def update(self, entity_id: int, entity):
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity_id: int):
        raise NotImplementedError


class RecordsRepository(AbstracRepository):

    def __init__(self, session):
        self.session = session

    def add(self, record):
        print(f'record:{record}')
        self.session.add(record)
        
    def get(self, reference):
        return self.session.query(model.TvShow).filter_by(reference=reference).one()
    
    def list(self, offset: int = None, limit: int = None, **query_conditions):
        query = self.session.query(model.TvShow).all()
        
        for key, value in query_conditions.items():
            query = query.filter(getattr(model.TvShow, key) == value)

        if offset is not None:
            query = query.offset(offset)
        if limit is not None:
            query = query.limit(limit)

        return [entity.dict() for entity in query]
    

    def bulk_insert(self, records: List[dict]):
        self.session.bulk_insert_mappings(self.entity, records)

    def update(self, entity_id: int, entity):
        pass

    def delete(self, entity_id: int):
        pass
