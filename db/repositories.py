from .database import session_factory
from .models import SkorozvonOrm
from .schemas import SkorozvonAdd

class SkorozvonRepository:
    @classmethod
    def add_one(cls, data: SkorozvonAdd):
        with session_factory() as session:
            lead_dict = data.model_dump()
            
            lead = SkorozvonOrm(**lead_dict)
            session.add(lead)
            session.commit()
            return lead.call_id
