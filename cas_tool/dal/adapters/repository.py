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
        self.session.add(record)

    def get(self, reference):
        return self.session.query(model.TvShow).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.TvShow).all()

    def bulk_insert(self, records: List[dict]):
        self.session.bulk_insert_mappings(self.entity, records)

    def update(self, entity_id: int, entity):
        pass

    def delete(self, entity_id: int):
        pass
