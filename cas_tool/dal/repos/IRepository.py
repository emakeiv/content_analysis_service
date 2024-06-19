from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional

T = TypeVar("T")

class IRepository(ABC):
    
    @abstractmethod
    def add(self, entity):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, entity_id: int) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[T]:
        raise NotImplementedError


    @abstractmethod
    def update(self, entity_id: int, entity):
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity_id: int):
        raise NotImplementedError