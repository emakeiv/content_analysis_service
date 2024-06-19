from dal.repos.IRepository import IRepository
import dal.model as model


class DataRepository(IRepository):

    def __init__(self, session):
        self.session = session

    def add(self, record):
        self.session.add(record)

    def get(self, reference):
        return self.session.query(model.TvShow).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.TvShow).all()

    def update(self, entity_id: int, entity):
        pass

    def delete(self, entity_id: int):
        pass
