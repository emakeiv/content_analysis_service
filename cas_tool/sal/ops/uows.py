from abc import ABC, abstractmethod
from dal.adapters import repository
from db import factory


class AbstractUnitOfWork(ABC):
    repos: repository.RecordsRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class SqlUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=factory.DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.repos = repository.RecordsRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        print(self.session)
        self.session.commit()

    def rollback(self):
        self.session.rollback()
