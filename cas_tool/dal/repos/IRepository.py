from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional

T = TypeVar("T")

class IRepository(Generic[T], ABC):
    
    @abstractmethod
    def get(self, entity_id: int) -> Optional[T]:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[T]:
        raise NotImplementedError()
    